import os
import sys

from .AccountPage import AccountPage
from .ClinicMap import ClinicMap
from .ClinicDashboard import ClinicDashboard
from .ClinicDoctorList import ClinicDoctorList
from .ClinicRequestReview import ClinicRequestReview
from .model import Clinic
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QSizePolicy, QStackedWidget, QGraphicsDropShadowEffect
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
        self.setStyleSheet(f"QMainWindow {{background-color: white;}}")
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
        stylesheet = """
                    QPushButton
                    {
                       background-color: transparent;
                       border-radius: 10px;
                       color: white;
                       text-align: left; 
                       padding-left: 10px;
                    }
                    QPushButton:pressed
                    {
                      background-color: #190482;     
                      text-align: left; 
                      padding-left: 10px;
                    }
                    QPushButton:hover
                    {
                      background-color: #7752FE;
                    }
                    """
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)

        self.mainLayout = QHBoxLayout()
        self.sideLayoutWidget = QWidget()
        self.sideLayoutWidget.setObjectName("sideBar")
        self.sideLayoutWidget.setStyleSheet("""QWidget#sideBar {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                stop: 0 rgba(25, 4, 130, 255), 
                                                stop: 1 rgba(119, 82, 254, 255)
                                            );
                                            border-radius: 10px;
                                        }""")
        self.sideLayout = QVBoxLayout(self.sideLayoutWidget)
        self.sideLayout.setContentsMargins(10, 10, 10, 10)

        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)

        self.dashboardButton = QPushButton()
        self.dashboardButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-house-64 (1).png")
        self.dashboardIcon = QIcon(filepath)
        self.dashboardButton.setFont(font)
        self.dashboardButton.setIconSize(QSize(35, 35))
        self.dashboardButton.setText("Dashboard")
        self.dashboardButton.setIcon(self.dashboardIcon)
        self.dashboardButton.setStyleSheet("""
                                            QPushButton
                                            {
                                               background-color: #190482;
                                               border-radius: 10px;
                                               color: white;
                                               text-align: left; 
                                               padding-left: 10px;
                                            }
                                            """)
        self.dashboardButton.clicked.connect(self.goToDashboard)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.dashboardButton.setGraphicsEffect(effect)

        self.manageScheduleButton = QPushButton(self.centralwidget)
        self.manageScheduleButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-calendar-64.png")
        self.scheduleIcon = QIcon(filepath)
        self.manageScheduleButton.setIconSize(QSize(35, 35))
        self.manageScheduleButton.setIcon(self.scheduleIcon)
        self.manageScheduleButton.setFont(font)
        self.manageScheduleButton.setText("Schedule")
        self.manageScheduleButton.setStyleSheet(stylesheet)
        self.manageScheduleButton.clicked.connect(self.goToManageSchedule)

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.manageScheduleButton.setGraphicsEffect(effect)

        self.doctorListButton = QPushButton(self.centralwidget)
        self.doctorListButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-doctor-64.png")
        self.doctorIcon = QIcon(filepath)
        self.doctorListButton.setIconSize(QSize(35, 35))
        self.doctorListButton.setFont(font)
        self.doctorListButton.setIcon(self.doctorIcon)
        self.doctorListButton.setText("Doctor List")
        self.doctorListButton.setStyleSheet(stylesheet)
        self.doctorListButton.clicked.connect(self.goToDoctorList)

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.doctorListButton.setGraphicsEffect(effect)

        self.requestReviewButton = QPushButton(self.centralwidget)
        self.requestReviewButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")
        self.requestReviewIcon = QIcon(filepath)
        self.requestReviewButton.setIconSize(QSize(35, 35))
        self.requestReviewButton.setFont(font)
        self.requestReviewButton.setIcon(self.requestReviewIcon)
        self.requestReviewButton.setText("Request Review")
        self.requestReviewButton.setStyleSheet(stylesheet)
        self.requestReviewButton.clicked.connect(self.goToRequestReview)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.requestReviewButton.setGraphicsEffect(effect)

        self.mapButton = QPushButton(self.centralwidget)
        self.mapButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-location-48.png")
        self.mapIcon = QIcon(filepath)
        self.mapButton.setIconSize(QSize(35, 35))
        self.mapButton.setText("Map")
        self.mapButton.setFont(font)
        self.mapButton.setIcon(self.mapIcon)
        self.mapButton.setStyleSheet(stylesheet)
        self.mapButton.clicked.connect(self.goToMapPage)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.mapButton.setGraphicsEffect(effect)

        self.topLeftLogo = QLabel()
        self.topLeftLogo.setFixedSize(280, 150)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(150, 150)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)
        self.topLeftLogo.setStyleSheet("margin-left: 60px;")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-customer-30.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(35, 35))
        self.myAccountButton.setFont(font)
        self.myAccountButton.setStyleSheet(stylesheet)
        self.myAccountButton.setText("My Account")
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.clicked.connect(self.goToAccountPage)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.myAccountButton.setGraphicsEffect(effect)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-logout-64.png")
        self.logoutIcon = QIcon(filepath)
        self.logoutButton.setIconSize(QSize(35, 35))
        self.logoutButton.setIcon(self.logoutIcon)
        self.logoutButton.setFont(font)
        self.logoutButton.setText("Log Out")
        self.logoutButton.setStyleSheet(stylesheet)
        self.logoutButton.clicked.connect(self.logout)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.logoutButton.setGraphicsEffect(effect)

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
        spacer2.setFixedHeight(30)
        self.sideLayout.addWidget(spacer2)
        self.sideLayout.addWidget(self.myAccountButton)
        self.sideLayout.addWidget(self.logoutButton)
        bottomSpacer = QWidget()
        bottomSpacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sideLayout.addWidget(bottomSpacer)

        self.mainLayout.addWidget(self.sideLayoutWidget, 4)

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
                button.setStyleSheet("background-color: #190482; border-radius: 10px; text-align: left; padding-left: 10px; color: white;")
            else:
                buttonTemp.setStyleSheet("""
                    QPushButton
                    {
                       background-color: transparent;
                       border-radius: 10px;
                       color: white;
                       text-align: left; 
                       padding-left: 10px;
                    }
                    QPushButton:pressed
                    {
                      background-color: #190482;    
                      text-align: left; 
                      padding-left: 10px; 
                    }
                    QPushButton:hover
                    {
                      background-color: #7752FE;
                    }
                    """)
