import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Clinic
from .PatientSendRequest import PatientSendRequest
from .PageManager import PageManager



class PatientClinicDetailsWindow(QMainWindow):

    def __init__(self, clinicTemp, patient):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        self.patient = patient
        print(self.clinic.getClinicID(), self.clinic.getClinicName(), self.clinic.getClinicAddress(), self.clinic.getClinicContact())
        self.setWindowTitle("Clinics Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("clinic_details")
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
        self.headerTitle.setText(self.clinic.getClinicName())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setFixedSize(70, 70)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.clinicPictureLabel = QLabel(self.centralwidget)
        self.clinicPictureLabel.setGeometry(QRect(180, 220, 400, 200))
        self.clinicPictureLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.clinicPicture = QPixmap(filepath)
        self.clinicPictureLabel.setPixmap(self.clinicPicture)

        self.clinicDescriptionLabel = QLabel(self.centralwidget)
        self.clinicDescriptionLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clinicDescriptionLabel.setFont(font)
        self.clinicDescriptionLabel.setText(self.clinic.getClinicName()+ "\n" + self.clinic.getClinicContact())
        self.clinicDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.clinicAddressLabel = QLabel(self.centralwidget)
        self.clinicAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clinicAddressLabel.setFont(font)
        self.clinicAddressLabel.setText(self.clinic.getClinicAddress())
        self.clinicAddressLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.sendRequestButton = QPushButton(self.centralwidget)
        self.sendRequestButton.setGeometry(QRect(710, 545, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.sendRequestButton.setFont(font)
        self.sendRequestButton.setLayoutDirection(Qt.LeftToRight)
        self.sendRequestButton.setText("Send Request")
        self.sendRequestButton.clicked.connect(self.sendRequestFunction)

        self.sendRequestLabel = QLabel(self.centralwidget)
        self.sendRequestLabel.setGeometry(QRect(730, 570, 50, 50))
        self.sendRequestLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.sendRequestIcon = QPixmap(filepath)
        self.sendRequestIcon = self.sendRequestIcon.scaled(50, 50)
        self.sendRequestLabel.setPixmap(self.sendRequestIcon)

        self.clinicDetailsContainer = QLabel(self.centralwidget)
        self.clinicDetailsContainer.setFixedSize(1000,500)
        self.clinicDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.clinicDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)
        self.sendRequestButton.raise_()

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def sendRequestFunction(self):
        self.patientSendRequest = PatientSendRequest(self.clinic, self.patient)
        self.pageManager.add(self.patientSendRequest)
        print("pageManager Size", self.pageManager.size())

    def backButtonFunction(self):
        self.pageManager.goBack()
