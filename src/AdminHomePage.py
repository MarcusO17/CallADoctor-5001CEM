import os
import sys

#Need to Import the pages for buttons as per what I create

from .model import Clinic
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QMessageBox
from PyQt5 import QtWidgets
from .ClinicManageSchedule import ClinicManageSchedule
from .AdminViewApprovals import AdminViewApprovalsWindow
from .AdminViewClinics import AdminViewClinicsWindow
from .PageManager import PageManager



class AdminHomepageWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.pageManager = PageManager()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.setupUi(self)

    def goToViewClinics(self):
        self.viewClinics = AdminViewClinicsWindow(self.clinic)
        self.pageManager.add(self.viewClinics)

    def goToViewApprovals(self):
        self.viewApprovals = AdminViewApprovalsWindow(self.clinic)
        self.pageManager.add(self.viewApprovals)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Homepage (Admin)")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.viewClinicsButton = QPushButton(self.centralwidget)
        self.viewClinicsButton.setGeometry(QRect(150, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.viewClinicsButton.setFont(font)
        self.viewClinicsButton.setText("View Clinics")
        # self.viewClinicsButton.clicked.connect(self.goToViewClinics)

        self.viewClinicsLabel = QLabel(self.centralwidget)
        self.viewClinicsLabel.setGeometry(QRect(170, 225, 50, 50))
        self.viewClinicsLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.viewClinicsIcon = QPixmap(filepath)
        self.viewClinicsIcon = self.viewClinicsIcon.scaled(50, 50)
        self.viewClinicsLabel.setPixmap(self.viewClinicsIcon)


        self.viewApprovalsButton = QPushButton(self.centralwidget)
        self.viewApprovalsButton.setGeometry(QRect(700, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.viewApprovalsButton.setFont(font)
        self.viewApprovalsButton.setLayoutDirection(Qt.LeftToRight)
        self.viewApprovalsButton.setText("View Approvals")
        # self.viewApprovalsButton.clicked.connect(self.goToViewApprovals)

        self.viewApprovalsLabel = QLabel(self.centralwidget)
        self.viewApprovalsLabel.setGeometry(QRect(720, 225, 50, 50))
        self.viewApprovalsLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.viewApprovalsIcon = QPixmap(filepath)
        self.viewApprovalsIcon = self.viewApprovalsIcon.scaled(50, 50)
        self.viewApprovalsLabel.setPixmap(self.viewApprovalsIcon)


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
        self.homepageTitle.setText("Welcome Admin!")
        self.homepageTitle.setAlignment(Qt.AlignCenter)


        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QRect(1150, 40, 70, 70))
        self.logoutButton.setIconSize(QSize(70, 70))
        self.logoutButton.setText("Log out")
        self.logoutButton.clicked.connect(self.logout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):

        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation", "Are you sure you want to logout",
                                               QMessageBox.Yes | QMessageBox.No)
        if logoutDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()