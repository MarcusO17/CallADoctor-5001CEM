import os
import sys

from .AccountPage import AccountPage
from .ClinicMap import ClinicMap
from .ClinicDashboard import ClinicDashboard
from .ClinicDoctorList import ClinicDoctorList
from .ClinicRequestReview import ClinicRequestReview
from .model import Clinic
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QSizePolicy, QStackedWidget
from PyQt5 import QtWidgets
from .ClinicManageSchedule import ClinicManageSchedule
from .PageManager import PageManager, FrameLayoutManager


class ClinicHomepage(QMainWindow):
    def __init__(self, clinicID):
        super().__init__()
        self.clinic = Clinic.getClinicfromID(clinicID)
        self.pageManager = PageManager()
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayoutManager.add(0)
        self.frameLayoutManager.setBasePages(6)
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setStyleSheet(f"QMainWindow {{background-color: #B6FFFA;}}")
        self.setupUi(self)

    def goToDashboard(self):
        self.setButtonHighlight(self.dashboardButton)
        self.frameLayoutManager.backToBasePage(0)
        self.frameLayout.setCurrentIndex(0)
    def goToManageSchedule(self):
        self.setButtonHighlight(self.manageScheduleButton)
        self.frameLayoutManager.backToBasePage(1)
        self.frameLayout.setCurrentIndex(1)

    def goToDoctorList(self):
        self.setButtonHighlight(self.doctorListButton)

        self.frameLayout.widget(2).generateDoctorButtons()
        self.frameLayoutManager.backToBasePage(2)
        self.frameLayout.setCurrentIndex(2)

    def goToRequestReview(self):
        self.setButtonHighlight(self.requestReviewButton)
        self.frameLayoutManager.backToBasePage(3)
        self.frameLayout.setCurrentIndex(3)

    def goToMapPage(self):
        self.setButtonHighlight(self.mapButton)
        self.frameLayoutManager.backToBasePage(4)
        self.frameLayout.setCurrentIndex(4)

    def goToAccountPage(self):
        self.setButtonHighlight(self.myAccountButton)
        self.frameLayoutManager.backToBasePage(5)
        self.frameLayout.setCurrentIndex(5)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        stylesheet = """
                    QPushButton
                    {
                       background-color: #C2D9FF;
                       border-radius: 10px;
                    }
                    QPushButton:pressed
                    {
                      background-color: #8E8FFA;     
                    }
                    QPushButton:hover
                    {
                      background-color: #7752FE;
                    }
                    """

        self.centralwidget = QWidget(MainWindow)

        self.mainLayout = QHBoxLayout()
        self.sideLayoutWidget = QWidget()
        self.sideLayoutWidget.setStyleSheet("background-color: white; border-radius: 10px;")
        self.sideLayout = QVBoxLayout(self.sideLayoutWidget)
        self.sideLayout.setContentsMargins(10, 10, 10, 10)
        self.sideLayout.setSpacing(30)
        self.sideLayout.setAlignment(Qt.AlignHCenter)

        self.dashboardButton = QPushButton()
        self.dashboardButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\dashboard.png")
        self.dashboardIcon = QIcon(filepath)
        self.dashboardButton.setIconSize(QSize(20, 20))
        self.dashboardButton.setIcon(self.dashboardIcon)
        self.dashboardButton.setStyleSheet(stylesheet)
        self.dashboardButton.clicked.connect(self.goToDashboard)

        self.manageScheduleButton = QPushButton(self.centralwidget)
        self.manageScheduleButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\schedule.png")
        self.scheduleIcon = QIcon(filepath)
        self.manageScheduleButton.setIconSize(QSize(20, 20))
        self.manageScheduleButton.setIcon(self.scheduleIcon)
        self.manageScheduleButton.setStyleSheet(stylesheet)
        self.manageScheduleButton.clicked.connect(self.goToManageSchedule)

        self.doctorListButton = QPushButton(self.centralwidget)
        self.doctorListButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\doctor.png")
        self.doctorIcon = QIcon(filepath)
        self.doctorListButton.setIconSize(QSize(20, 20))
        self.doctorListButton.setIcon(self.doctorIcon)
        self.doctorListButton.setStyleSheet(stylesheet)
        self.doctorListButton.clicked.connect(self.goToDoctorList)

        self.requestReviewButton = QPushButton(self.centralwidget)
        self.requestReviewButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\request.png")
        self.requestReviewIcon = QIcon(filepath)
        self.requestReviewButton.setIconSize(QSize(15, 15))
        self.requestReviewButton.setIcon(self.requestReviewIcon)
        self.requestReviewButton.setStyleSheet(stylesheet)
        self.requestReviewButton.clicked.connect(self.goToRequestReview)

        self.mapButton = QPushButton(self.centralwidget)
        self.mapButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\map.png")
        self.mapIcon = QIcon(filepath)
        self.mapButton.setIconSize(QSize(20, 20))
        self.mapButton.setIcon(self.mapIcon)
        self.mapButton.setStyleSheet(stylesheet)
        self.mapButton.clicked.connect(self.goToMapPage)

        self.topLeftLogo = QLabel()
        self.topLeftLogo.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(50, 50)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\account.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(20, 20))
        self.myAccountButton.setStyleSheet(stylesheet)
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setFixedSize(50, 50)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logout.png")
        self.logoutIcon = QIcon(filepath)
        self.logoutButton.setIconSize(QSize(20, 20))
        self.logoutButton.setIcon(self.logoutIcon)
        self.logoutButton.setStyleSheet(stylesheet)
        self.logoutButton.clicked.connect(self.logout)

        self.highlightButtonList = list()
        self.highlightButtonList.append(self.myAccountButton)
        self.highlightButtonList.append(self.requestReviewButton)
        self.highlightButtonList.append(self.doctorListButton)
        self.highlightButtonList.append(self.dashboardButton)
        self.highlightButtonList.append(self.manageScheduleButton)
        self.highlightButtonList.append(self.mapButton)

        self.sideLayout.addWidget(self.topLeftLogo)
        spacer1 = QWidget()
        spacer1.setFixedHeight(50)
        self.sideLayout.addWidget(spacer1)
        self.sideLayout.addWidget(self.dashboardButton)
        self.sideLayout.addWidget(self.manageScheduleButton)
        self.sideLayout.addWidget(self.doctorListButton)
        self.sideLayout.addWidget(self.requestReviewButton)
        self.sideLayout.addWidget(self.mapButton)
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sideLayout.addWidget(spacer2)
        self.sideLayout.addWidget(self.myAccountButton)
        self.sideLayout.addWidget(self.logoutButton)
        bottomSpacer = QWidget()
        bottomSpacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sideLayout.addWidget(bottomSpacer)

        self.mainLayout.addWidget(self.sideLayoutWidget, 1)

        # THIS QSTACKEDWIDGET IS ONLY FOR QWIDGET SWITCHING
        self.frameLayout = QStackedWidget()
        self.frameLayout.setStyleSheet(f"QStackedWidget {{background-color: transparent;}}")
        # start and set all pages to the framelayout
        self.clinicDashboard = ClinicDashboard(self.clinic)  # index 0
        self.clinicManageSchedule = ClinicManageSchedule(self.clinic)  # index 1
        self.clinicDoctorList = ClinicDoctorList(self.clinic)  # index 2
        self.clinicRequestReview = ClinicRequestReview(self.clinic)  # index 3
        self.clinicMap = ClinicMap(self.clinic) # index 4
        self.accountPage = AccountPage()  # index 5
        self.accountPage.setUser("Clinic", self.clinic)

        self.frameLayout.addWidget(self.clinicDashboard)
        self.frameLayout.addWidget(self.clinicManageSchedule)
        self.frameLayout.addWidget(self.clinicDoctorList)
        self.frameLayout.addWidget(self.clinicRequestReview)
        self.frameLayout.addWidget(self.clinicMap)
        self.frameLayout.addWidget(self.accountPage)

        self.frameLayoutManager.setFrameLayout(self.frameLayout)

        self.mainLayout.addWidget(self.frameLayout, 11)

        self.centralwidget.setLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):

        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation",
                                               "Are you sure you want to logout",
                                               QMessageBox.Yes | QMessageBox.No)
        if logoutDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()
            self.frameLayoutManager.back()

    def setButtonHighlight(self, button):
        for buttonTemp in self.highlightButtonList:
            if buttonTemp == button:
                button.setStyleSheet("background-color: #8E8FFA; border-radius: 10px;")
            else:
                buttonTemp.setStyleSheet("""
                    QPushButton
                    {
                       background-color: #C2D9FF;
                       border-radius: 10px;
                    }
                    QPushButton:pressed
                    {
                      background-color: #8E8FFA;     
                    }
                    QPushButton:hover
                    {
                      background-color: #7752FE;
                    }
                    """)
