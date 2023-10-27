import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Patient
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .PageManager import PageManager


class DoctorPatientRecordWindow(QMainWindow):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.setWindowTitle("Patient Record (Doctor)")
        self.pageManager = PageManager()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DocPatientRecord")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # header (probably reused in most files)
        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Patient Record")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.docMyAccountButton = QPushButton(self.centralwidget)
        self.docMyAccountButton.setFixedSize(70,70)
        self.docMyAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.docMyAccountIcon = QIcon(filepath)
        self.docMyAccountButton.setIconSize(QSize(70, 70))
        self.docMyAccountButton.setIcon(self.docMyAccountIcon)
        self.docMyAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.docBackButton = QPushButton(self.centralwidget)
        self.docBackButton.setFixedSize(70, 70)
        self.docBackButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.docBackIcon = QIcon(filepath)
        self.docBackButton.setIconSize(QSize(70, 70))
        self.docBackButton.setIcon(self.docBackIcon)
        self.docBackButton.clicked.connect(self.backButtonFunction)

        buttonContainer = QVBoxLayout()
        buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        patientList = list()


        patient1 = Patient("p0001", "Patient 1", "Patient 1 description", "Patient 1 address", "ABC", "Indian")
        patient2 = Patient("p0002", "Patient 2", "Patient 2 description", "Patient 2 address", "ABC", "Indian")
        patient3 = Patient("p0003", "Patient 3", "Patient 3 description", "Patient 3 address", "ABC", "Indian")

        patientList.append(patient1)
        patientList.append(patient2)
        patientList.append(patient3)
        print("patient list size" , len(patientList))

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, patient in enumerate(patientList):
            self.patientButton = QPushButton()
            self.patientButton.setText(patient.getPatientID() + " - " + patient.getPatientName())
            self.patientButton.setFont(buttonFont)
            self.patientButton.setFixedSize(QSize(950,150))
            self.patientButton.clicked.connect(lambda checked, patient=patient: self.patientButtonFunction(patient, self.doctor))
            buttonContainer.addWidget(self.patientButton)

        boxScrollArea.setLayout(buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(20)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def patientButtonFunction(self, patient, doctor):
        # update the clinic details page here according to button click
        self.patientHistoryWindow = DoctorPatientHistoryWindow(patient, doctor)
        self.pageManager.add(self.patientHistoryWindow)
        print(self.pageManager.size())

    def backButtonFunction(self):
        self.pageManager.goBack()

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Doctor", self.doctor)
        self.pageManager.add(self.accountPage)
