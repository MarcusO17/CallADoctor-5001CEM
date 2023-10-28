import os
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget, \
    QSizePolicy, QStackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from .AccountPage import AccountPage
from .DoctorDashboard import DoctorDashboard
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
        self.setWindowTitle("Doctor Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def goToDashboard(self):
        self.setButtonHighlight(self.dashboardButton)
        self.doctorDashboard.setSchedule()
        self.frameLayout.setCurrentIndex(0)
        self.frameLayoutManager.backToBasePage(0)

    def gotoSchedule(self):
        self.setButtonHighlight(self.scheduleButton)
        self.doctorScheduleWindow.setSchedule()
        self.frameLayout.setCurrentIndex(1)
        self.frameLayoutManager.backToBasePage(1)

    def gotoPatientRecord(self):
        self.setButtonHighlight(self.patientRecordButton)
        self.frameLayout.setCurrentIndex(2)
        self.frameLayoutManager.backToBasePage(2)

    def gotoMyAppointment(self):
        self.setButtonHighlight(self.myAppointmentButton)
        self.frameLayout.setCurrentIndex(3)
        self.frameLayoutManager.backToBasePage(3)

    def goToAccountPage(self):
        self.setButtonHighlight(self.myAccountButton)
        self.frameLayout.setCurrentIndex(4)
        self.frameLayoutManager.backToBasePage(4)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.mainLayout = QHBoxLayout()
        self.sideLayoutWidget = QWidget()
        self.sideLayoutWidget.setStyleSheet("background-color: #E6EBF5; border-radius: 10px;")
        self.sideLayout = QVBoxLayout(self.sideLayoutWidget)
        self.sideLayout.setContentsMargins(10,10,10,10)

        # Label, Icon and Button for Schedule
        self.scheduleButton = QPushButton()
        self.scheduleButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\schedule.png")
        self.scheduleIcon = QIcon(filepath)
        self.scheduleButton.setIconSize(QSize(35, 35))
        self.scheduleButton.setIcon(self.scheduleIcon)
        self.scheduleButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.scheduleButton.clicked.connect(self.gotoSchedule)

        self.dashboardButton = QPushButton()
        self.dashboardButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\dashboard.png")
        self.dashboardIcon = QIcon(filepath)
        self.dashboardButton.setIconSize(QSize(35, 35))
        self.dashboardButton.setIcon(self.dashboardIcon)
        self.dashboardButton.setStyleSheet("background-color: #3872E8; border-radius: 10px;")
        self.dashboardButton.clicked.connect(self.goToDashboard)

        # Button, Label and Icon for Patient Record
        self.patientRecordButton = QPushButton()
        self.patientRecordButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\record.png")
        self.patientRecordIcon = QIcon(filepath)
        self.patientRecordButton.setIconSize(QSize(35, 35))
        self.patientRecordButton.setIcon(self.patientRecordIcon)
        self.patientRecordButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.patientRecordButton.clicked.connect(self.gotoPatientRecord)

        self.myAppointmentButton = QPushButton()
        self.myAppointmentButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\appointment.png")
        self.myAppointmentIcon = QIcon(filepath)
        self.myAppointmentButton.setIconSize(QSize(35, 35))
        self.myAppointmentButton.setIcon(self.myAppointmentIcon)
        self.myAppointmentButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.myAppointmentButton.clicked.connect(self.gotoMyAppointment)

        self.topLeftLogo = QLabel()
        self.topLeftLogo.setGeometry(QRect(20, 10, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(70, 70)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.myAccountButton = QPushButton()
        self.myAccountButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\account.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(35, 35))
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logout.png")
        self.logoutIcon = QIcon(filepath)
        self.logoutButton.setIconSize(QSize(35, 35))
        self.logoutButton.setIcon(self.logoutIcon)
        self.logoutButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.logoutButton.clicked.connect(self.logout)

        self.highlightButtonList = list()
        self.highlightButtonList.append(self.myAccountButton)
        self.highlightButtonList.append(self.myAppointmentButton)
        self.highlightButtonList.append(self.scheduleButton)
        self.highlightButtonList.append(self.dashboardButton)
        self.highlightButtonList.append(self.patientRecordButton)

        self.sideLayout.addWidget(self.topLeftLogo)
        spacer1 = QWidget()
        spacer1.setFixedHeight(100)
        self.sideLayout.addWidget(spacer1)
        self.sideLayout.addWidget(self.dashboardButton)
        self.sideLayout.addWidget(self.scheduleButton)
        self.sideLayout.addWidget(self.patientRecordButton)
        self.sideLayout.addWidget(self.myAppointmentButton)
        spacer2 = QWidget()
        spacer2.setFixedHeight(100)
        self.sideLayout.addWidget(spacer2)
        self.sideLayout.addWidget(self.myAccountButton)
        self.sideLayout.addWidget(self.logoutButton)
        bottomSpacer = QWidget()
        bottomSpacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sideLayout.addWidget(bottomSpacer)

        self.mainLayout.addWidget(self.sideLayoutWidget, 1)

        # THIS QSTACKEDWIDGET IS ONLY FOR QWIDGET SWITCHING
        self.frameLayout = QStackedWidget()
        # start and set all pages to the framelayout
        self.doctorDashboard = DoctorDashboard(self.doctor) # index 0
        self.doctorScheduleWindow = DoctorScheduleWindow(self.doctor) # index 1
        self.doctorPatientRecord = DoctorPatientRecordWindow(self.doctor) # index 2
        self.doctorMyAppointment = DoctorMyAppointmentWindow(self.doctor) # index 3
        self.accountPage = AccountPage() # index 4
        self.accountPage.setUser("Doctor", self.doctor)

        self.frameLayout.addWidget(self.doctorDashboard)
        self.frameLayout.addWidget(self.doctorScheduleWindow)
        self.frameLayout.addWidget(self.doctorPatientRecord)
        self.frameLayout.addWidget(self.doctorMyAppointment)
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
                button.setStyleSheet("background-color: #3872E8; border-radius: 10px;")
            else:
                buttonTemp.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
