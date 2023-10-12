import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from model import Clinic


class PatientClinicsNearbyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clinics Nearby")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.ui = init_ui()
        self.ui.setupUi(self)

class init_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PatientClinicsNearby")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # header (probably reused in most files)
        self.topLeftLogo = QLabel()
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setFixedSize(60, 60)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.headerTitle = QLabel()
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setText("Welcome! [name]")
        self.headerTitle.setAlignment(Qt.AlignCenter)

        self.myAccountButton = QPushButton()
        self.myAccountButton.setFixedSize(70,70)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton()
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)

        headerLayout = QHBoxLayout()
        headerLayout.addWidget(self.topLeftLogo)
        headerLayout.addWidget(self.headerTitle)
        headerLayout.addWidget(self.myAccountButton)
        headerLayout.addWidget(self.backButton)

        buttonContainer = QVBoxLayout()
        buttonContainer.setContentsMargins(60,5,5,5)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        clinicList = list()

        clinic1 = Clinic("c0001", "Clinic 1","clinic 1 description", "clinic 1 address")
        clinic2 = Clinic("c0002", "Clinic 2", "clinic 2 description", "clinic 2 address")
        clinic3 = Clinic("c0003", "Clinic 3", "clinic 3 description", "clinic 3 address")

        clinicList.append(clinic1)
        clinicList.append(clinic2)
        clinicList.append(clinic3)
        print("clinic list size" , len(clinicList))

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, clinic in enumerate(clinicList):
            self.clinicButton = QPushButton()
            self.clinicButton.setText(clinic.getClinicID() + " - " + clinic.getClinicName())
            self.clinicButton.setFont(buttonFont)
            self.clinicButton.setFixedSize(QSize(800,150))
            self.clinicButton.clicked.connect(lambda checked, clinic=clinic: self.clinicButtonFunction(clinic))
            buttonContainer.addWidget(self.clinicButton)

        boxScrollArea.setLayout(buttonContainer)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(headerLayout)
        mainLayout.addWidget(boxScrollArea)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def clinicButtonFunction(self, clinic):
        # update the clinic details page here according to button click
        print(clinic.getClinicID())
        print(clinic.getClinicName())
        print(clinic.getClinicDescription())
        print(clinic.getClinicAddress())

def runthiswindow():
    app = QApplication(sys.argv)
    window = PatientClinicsNearbyWindow()
    window.show()
    sys.exit(app.exec_())

runthiswindow()