import os
from PyQt5.QtCore import Qt, QRect, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget, \
    QSizePolicy, QStackedWidget, QGraphicsDropShadowEffect
from PyQt5 import QtCore, QtGui, QtWidgets

from .AccountPage import AccountPage
from .DoctorDashboard import DoctorDashboard
from .DoctorMap import DoctorMap
from .DoctorScheduleWindow import DoctorScheduleWindow
from .PageManager import PageManager, FrameLayoutManager
from .model import Doctor
from .DoctorMyAppointment import DoctorMyAppointmentWindow
from .DoctorPatientRecord import DoctorPatientRecordWindow

class DoctorHomepage(QMainWindow):
    def __init__(self, sessionID):
        super().__init__()
        self.pageManager = PageManager()
        self.frameLayoutManager = FrameLayoutManager()
        self.doctor = Doctor.getDoctorfromID(sessionID)
        self.frameLayoutManager.add(0)
        self.frameLayoutManager.setBasePages(6)
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setStyleSheet(f"QMainWindow {{background-color: white;}}")
        self.setupUi(self)

    def goToDashboard(self):
        self.setButtonHighlight(self.dashboardButton)
        self.doctorDashboard.setSchedule()
        self.frameLayoutManager.backToBasePage(0)
        self.frameLayout.setCurrentIndex(0)

    def gotoSchedule(self):
        self.setButtonHighlight(self.scheduleButton)
        self.doctorScheduleWindow.setSchedule()
        self.frameLayoutManager.backToBasePage(1)
        self.frameLayout.setCurrentIndex(1)

    def gotoPatientRecord(self):
        self.setButtonHighlight(self.patientRecordButton)
        self.frameLayoutManager.backToBasePage(2)
        self.frameLayout.setCurrentIndex(2)

    def gotoMyAppointment(self):
        self.setButtonHighlight(self.myAppointmentButton)
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

        self.centralwidget = QtWidgets.QWidget(MainWindow)

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
        self.sideLayout.setContentsMargins(10,10,10,10)

        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)

        # Label, Icon and Button for Schedule
        self.scheduleButton = QPushButton()
        self.scheduleButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-calendar-64.png")
        self.scheduleIcon = QIcon(filepath)
        self.scheduleButton.setFont(font)
        self.scheduleButton.setText("My Schedule")
        self.scheduleButton.setIconSize(QSize(35, 35))
        self.scheduleButton.setIcon(self.scheduleIcon)
        self.scheduleButton.clicked.connect(self.gotoSchedule)
        self.scheduleButton.setStyleSheet(stylesheet)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.scheduleButton.setGraphicsEffect(effect)

        self.dashboardButton = QPushButton()
        self.dashboardButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-house-64 (1).png")
        self.dashboardIcon = QIcon(filepath)
        self.dashboardButton.setFont(font)
        self.dashboardButton.setText("Dashboard")
        self.dashboardButton.setIconSize(QSize(35, 35))
        self.dashboardButton.setIcon(self.dashboardIcon)
        self.dashboardButton.clicked.connect(self.goToDashboard)
        self.dashboardButton.setStyleSheet(stylesheet)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.dashboardButton.setGraphicsEffect(effect)

        # Button, Label and Icon for Patient Record
        self.patientRecordButton = QPushButton()
        self.patientRecordButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")
        self.patientRecordIcon = QIcon(filepath)
        self.patientRecordButton.setFont(font)
        self.patientRecordButton.setText("Patient Record")
        self.patientRecordButton.setIconSize(QSize(35, 35))
        self.patientRecordButton.setIcon(self.patientRecordIcon)
        self.patientRecordButton.clicked.connect(self.gotoPatientRecord)
        self.patientRecordButton.setStyleSheet(stylesheet)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.patientRecordButton.setGraphicsEffect(effect)

        self.myAppointmentButton = QPushButton()
        self.myAppointmentButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-appointment-50.png")
        self.myAppointmentIcon = QIcon(filepath)
        self.myAppointmentButton.setFont(font)
        self.myAppointmentButton.setText("My Appointment")
        self.myAppointmentButton.setIconSize(QSize(35, 35))
        self.myAppointmentButton.setIcon(self.myAppointmentIcon)
        self.myAppointmentButton.clicked.connect(self.gotoMyAppointment)
        self.myAppointmentButton.setStyleSheet(stylesheet)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.myAppointmentButton.setGraphicsEffect(effect)

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

        self.myAccountButton = QPushButton()
        self.myAccountButton.setFixedSize(280, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-customer-30.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(35, 35))
        self.myAccountButton.setFont(font)
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.clicked.connect(self.goToAccountPage)
        self.myAccountButton.setStyleSheet(stylesheet)
        self.myAccountButton.setText("My Account")
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
        self.logoutButton.setFont(font)
        self.logoutButton.setText("Log Out")
        self.logoutButton.setStyleSheet(stylesheet)
        self.logoutButton.setIcon(self.logoutIcon)
        self.logoutButton.clicked.connect(self.logout)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.logoutButton.setGraphicsEffect(effect)

        self.highlightButtonList = list()
        self.highlightButtonList.append(self.myAccountButton)
        self.highlightButtonList.append(self.myAppointmentButton)
        self.highlightButtonList.append(self.scheduleButton)
        self.highlightButtonList.append(self.dashboardButton)
        self.highlightButtonList.append(self.patientRecordButton)
        self.highlightButtonList.append(self.mapButton)

        self.sideLayout.addWidget(self.topLeftLogo)
        spacer1 = QWidget()
        spacer1.setFixedHeight(50)
        self.sideLayout.addWidget(spacer1)
        self.sideLayout.addWidget(self.dashboardButton)
        self.sideLayout.addWidget(self.scheduleButton)
        self.sideLayout.addWidget(self.patientRecordButton)
        self.sideLayout.addWidget(self.myAppointmentButton)
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
        self.doctorDashboard = DoctorDashboard(self.doctor) # index 0
        self.doctorScheduleWindow = DoctorScheduleWindow(self.doctor) # index 1
        self.doctorPatientRecord = DoctorPatientRecordWindow(self.doctor) # index 2
        self.doctorMyAppointment = DoctorMyAppointmentWindow(self.doctor) # index 3
        self.doctorMap = DoctorMap(self.doctor) # index 4
        self.accountPage = AccountPage() # index 5
        self.accountPage.setUser("Doctor", self.doctor)

        self.frameLayout.addWidget(self.doctorDashboard)
        self.frameLayout.addWidget(self.doctorScheduleWindow)
        self.frameLayout.addWidget(self.doctorPatientRecord)
        self.frameLayout.addWidget(self.doctorMyAppointment)
        self.frameLayout.addWidget(self.doctorMap)
        self.frameLayout.addWidget(self.accountPage)

        self.frameLayoutManager.setFrameLayout(self.frameLayout)

        self.mainLayout.addWidget(self.frameLayout, 11)

        self.centralwidget.setLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):

        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation", "Are you sure you want to logout",
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
