import os
import sys

from .AccountPage import AccountPage
from .ClinicDoctorList import ClinicDoctorList
from .ClinicRequestReview import ClinicRequestReview
from .model import Clinic
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QMessageBox
from PyQt5 import QtWidgets
from .ClinicManageSchedule import ClinicManageSchedule
from .PageManager import PageManager



class ClinicHomepage(QMainWindow):
    def __init__(self, clinicID):
        super().__init__()
        self.clinic = Clinic.getClinicfromID(clinicID)
        self.pageManager = PageManager()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.setupUi(self)

    def goToManageSchedule(self):
        self.clinicManageSchedule = ClinicManageSchedule(self.clinic)
        self.pageManager.add(self.clinicManageSchedule)

    def goToDoctorList(self):
        self.doctorListPage = ClinicDoctorList(self.clinic)
        self.pageManager.add(self.doctorListPage)

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Clinic", self.clinic)
        self.pageManager.add(self.accountPage)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Homepage")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.manageScheduleButton = QPushButton(self.centralwidget)
        self.manageScheduleButton.setGeometry(QRect(150, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.manageScheduleButton.setFont(font)
        self.manageScheduleButton.setText("Manage Schedule")
        self.manageScheduleButton.clicked.connect(self.goToManageSchedule)

        self.manageScheduleLabel = QLabel(self.centralwidget)
        self.manageScheduleLabel.setGeometry(QRect(170, 225, 50, 50))
        self.manageScheduleLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.manageScheduleIcon = QPixmap(filepath)
        self.manageScheduleIcon = self.manageScheduleIcon.scaled(50, 50)
        self.manageScheduleLabel.setPixmap(self.manageScheduleIcon)


        self.doctorListButton = QPushButton(self.centralwidget)
        self.doctorListButton.setGeometry(QRect(700, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.doctorListButton.setFont(font)
        self.doctorListButton.setLayoutDirection(Qt.LeftToRight)
        self.doctorListButton.setText("Doctor List")
        self.doctorListButton.clicked.connect(self.goToDoctorList)

        self.doctorListLabel = QLabel(self.centralwidget)
        self.doctorListLabel.setGeometry(QRect(720, 225, 50, 50))
        self.doctorListLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.doctorListIcon = QPixmap(filepath)
        self.doctorListIcon = self.doctorListIcon.scaled(50, 50)
        self.doctorListLabel.setPixmap(self.doctorListIcon)


        self.requestReviewButton = QPushButton(self.centralwidget)
        self.requestReviewButton.setGeometry(QRect(150, 400, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.requestReviewButton.setFont(font)
        self.requestReviewButton.setText("Request Review")
        self.requestReviewButton.clicked.connect(self.gotoRequestReview)

        self.requestReviewLabel = QLabel(self.centralwidget)
        self.requestReviewLabel.setGeometry(QRect(175, 425, 50, 50))
        self.requestReviewLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.requestReviewIcon = QPixmap(filepath)
        self.requestReviewIcon = self.requestReviewIcon.scaled(50, 50)
        self.requestReviewLabel.setPixmap(self.requestReviewIcon)

        self.patientListButton = QPushButton(self.centralwidget)
        self.patientListButton.setGeometry(QRect(700, 400, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.patientListButton.setFont(font)
        self.patientListButton.setText("Patient List")

        self.patientListLabel = QLabel(self.centralwidget)
        self.patientListLabel.setGeometry(QRect(725, 425, 50, 50))
        self.patientListLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.patientListIcon = QPixmap(filepath)
        self.patientListIcon = self.patientListIcon.scaled(50, 50)
        self.patientListLabel.setPixmap(self.patientListIcon)


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
        self.homepageTitle.setText(self.clinic.getClinicName())
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70,70))
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.clicked.connect(self.goToAccountPage)

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

    def gotoRequestReview(self):
        self.requestReview = ClinicRequestReview(self.clinic)
        self.pageManager.add(self.requestReview)
