import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication
from PyQt5 import QtWidgets


class PatientHomepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.ui = init_ui()
        self.ui.setupUi(self)

class init_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Homepage")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.clinicNearbyButton = QPushButton(self.centralwidget)
        self.clinicNearbyButton.setGeometry(QRect(150, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.clinicNearbyButton.setFont(font)
        self.clinicNearbyButton.setObjectName("schedule")
        self.clinicNearbyButton.setText("Clinics Nearby")

        self.clinicNearbyLabel = QLabel(self.centralwidget)
        self.clinicNearbyLabel.setGeometry(QRect(170, 225, 50, 50))
        self.clinicNearbyLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.clinicNearbyIcon = QPixmap(filepath)
        self.clinicNearbyIcon = self.clinicNearbyIcon.scaled(50, 50)
        self.clinicNearbyLabel.setPixmap(self.clinicNearbyIcon)


        self.myPrescriptionButton = QPushButton(self.centralwidget)
        self.myPrescriptionButton.setGeometry(QRect(700, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.myPrescriptionButton.setFont(font)
        self.myPrescriptionButton.setLayoutDirection(Qt.LeftToRight)
        self.myPrescriptionButton.setText("My Prescription")

        self.myPrescriptionLabel = QLabel(self.centralwidget)
        self.myPrescriptionLabel.setGeometry(QRect(720, 225, 50, 50))
        self.myPrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myPrescriptionIcon = QPixmap(filepath)
        self.myPrescriptionIcon = self.myPrescriptionIcon.scaled(50, 50)
        self.myPrescriptionLabel.setPixmap(self.myPrescriptionIcon)


        self.myAppointmentsButton = QPushButton(self.centralwidget)
        self.myAppointmentsButton.setGeometry(QRect(150, 400, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.myAppointmentsButton.setFont(font)
        self.myAppointmentsButton.setText("My Appointments")

        self.myAppointmentsLabel = QLabel(self.centralwidget)
        self.myAppointmentsLabel.setGeometry(QRect(175, 425, 50, 50))
        self.myAppointmentsLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAppointmentsIcon = QPixmap(filepath)
        self.myAppointmentsIcon = self.myAppointmentsIcon.scaled(50, 50)
        self.myAppointmentsLabel.setPixmap(self.myAppointmentsIcon)


        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.homepageTitle = QLabel(self.centralwidget)
        self.homepageTitle.setGeometry(QRect(200, 40, 800, 70))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.homepageTitle.setFont(font)
        self.homepageTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.homepageTitle.setText("Welcome! [name]")
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70,70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.logoutIcon = QIcon(filepath)
        self.logoutButton.setIconSize(QSize(70, 70))
        self.logoutButton.setIcon(self.logoutIcon)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)