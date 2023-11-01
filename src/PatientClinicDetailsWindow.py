import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Clinic
from .PatientSendRequest import PatientSendRequest
from .PageManager import PageManager, FrameLayoutManager


class PatientClinicDetailsWindow(QWidget):

    def __init__(self, clinicTemp, patient):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        self.patient = patient
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(self.clinic.getClinicName())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
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
        self.clinicDescriptionLabel.setText(f"{self.clinic.getClinicName()} \n {str(self.clinic.getClinicContact())}")
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

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        self.sendRequestButton.raise_()

        self.setLayout(mainLayout)


    def sendRequestFunction(self):
        self.patientSendRequest = PatientSendRequest(self.clinic, self.patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientSendRequest)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
