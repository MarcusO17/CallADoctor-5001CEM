import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication
from PyQt5 import QtWidgets
from model import Clinic


class PatientHomepage(QMainWindow):
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

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        buttonContainer = QVBoxLayout()

        clinicList = list()

        for count, clinic in enumerate(clinicList):
            self.clinicButton = QPushButton(self.centralwidget)
            self.clinicButton.setFrameShape(QtWidgets.QFrame.Box)
            self.clinicButton.setFixedSize(800, 200)







        # header (probably reused in most files)
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

