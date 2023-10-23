import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets

from .ClinicDoctorDetails import ClinicDoctorDetails
from .model import Clinic
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .model import Doctor
from .PageManager import PageManager


class ClinicAddDoctor(QMainWindow):
    def __init__(self, clinic):
        super().__init__()
        self.setWindowTitle("Add Doctor")
        self.clinic = clinic
        self.pageManager = PageManager()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
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
        self.headerTitle.setText("Add Doctor")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.buttonContainer = QVBoxLayout()
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        self.doctorList = list()

        self.generateDoctorButtons()

        boxScrollArea.setLayout(self.buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def doctorButtonFunction(self, doctor, clinic):
        self.doctorDetails = ClinicDoctorDetails(doctor, clinic)
        self.doctorDetails.setMode("Add")
        self.pageManager.add(self.doctorDetails)

    def backButtonFunction(self):
        self.pageManager.getPreviousPage().generateDoctorButtons()
        self.pageManager.goBack()


    def generateDoctorButtons(self):

        # delete and clear the buttons, generating back later
        for i in range(self.buttonContainer.count()):
            widget = self.buttonContainer.itemAt(0).widget()
            self.buttonContainer.removeWidget(widget)
            print("in the loop ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget")

        self.doctorList.clear()

        # Query and get the doctor list here
        doctor1 = Doctor("D0001", "Doctor 1", "", "AVAILABLE", "Junior", "0123456789",
                         "030102091820", 2)
        doctor2 = Doctor("D0002", "Doctor 2", "", "AVAILABLE", "Senior", "0198765432",
                         "090502873626", 5)
        doctor3 = Doctor("D0003", "Doctor 3", "", "AVAILABLE", "Junior", "0123456787",
                         "030102091821", 2)

        self.doctorList.append(doctor1)
        self.doctorList.append(doctor2)
        self.doctorList.append(doctor3)
        print("doctor list size", len(self.doctorList))

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, doctor in enumerate(self.doctorList):
            doctorButton = QPushButton()
            doctorButton.setText(doctor.getDoctorID() + " - " + doctor.getDoctorName())
            doctorButton.setFont(buttonFont)
            doctorButton.setFixedSize(QSize(950, 150))
            doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))
            self.buttonContainer.addWidget(doctorButton)