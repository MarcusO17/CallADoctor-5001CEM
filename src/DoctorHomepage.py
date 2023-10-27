import os
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget, \
    QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets

from .AccountPage import AccountPage
from .DoctorDashboard import DoctorDashboard
from .DoctorScheduleWindow import DoctorScheduleWindow
from .PageManager import PageManager
from .model import Doctor
from .DoctorMyAppointment import DoctorMyAppointmentWindow
from .DoctorPatientRecord import DoctorPatientRecordWindow

class DoctorHomepage(QMainWindow):
    def __init__(self, sessionID):
        super().__init__()
        self.pageManager = PageManager()
        self.doctor = Doctor.getDoctorfromID(sessionID)
        # not implemented yet
        #self.doctor = Doctor.getDoctorfromID(sessionID)
        self.setWindowTitle("Doctor Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def gotoSchedule(self):
        #doctor1 = Doctor("D0001", "Doctor 1", "c0001", "AVAILABLE", "Junior", "0123456789", "030102091820", 2)
        self.doctorScheduleWindow = DoctorScheduleWindow(self.doctor)
        self.pageManager.add(self.doctorScheduleWindow)
        print(self.pageManager.size())

    def gotoPatientRecord(self):
        #self.doctor = Doctor("D0001", "Doctor 1", "C0001", "status", "doctortype", "doctorContact", "doctorICNUmber", 5)
        self.patientRecord = DoctorPatientRecordWindow(self.doctor)
        self.pageManager.add(self.patientRecord)
        print(self.pageManager.size())

    def gotoMyAppointment(self):
        #self.doctor = Doctor("D0001", "Doctor 1", "C0001", "status", "doctortype", "doctorContact", "doctorICNUmber", 5)
        self.myAppointment = DoctorMyAppointmentWindow(self.doctor)
        self.pageManager.add(self.myAppointment)
        print(self.pageManager.size())

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Doctor", self.doctor)
        self.pageManager.add(self.accountPage)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QHBoxLayout()
        self.sideLayoutWidget = QWidget()
        self.sideLayoutWidget.setStyleSheet("background-color: #dcdcdc;")
        self.sideLayout = QVBoxLayout(self.sideLayoutWidget)
        self.sideLayout.setContentsMargins(10,10,10,10)

        # Label, Icon and Button for Schedule
        self.scheduleButton = QPushButton()
        self.scheduleButton.setFixedSize(70, 70)
        self.scheduleButton.setText("Schedule")
        self.scheduleButton.clicked.connect(self.gotoSchedule)

        self.dashboardButton = QPushButton()
        self.dashboardButton.setFixedSize(70, 70)
        self.dashboardButton.setText("DashBoard")

        # Button, Label and Icon for Patient Record
        self.patientRecordButton = QPushButton()
        self.patientRecordButton.setFixedSize(70, 70)
        self.patientRecordButton.setText("Patient Record")
        self.patientRecordButton.clicked.connect(self.gotoPatientRecord)

        self.myAppointmentButton = QPushButton()
        self.myAppointmentButton.setFixedSize(70, 70)
        self.myAppointmentButton.setText("My Appointments")
        self.myAppointmentButton.clicked.connect(self.gotoMyAppointment)

        self.topLeftLogo = QLabel()
        self.topLeftLogo.setGeometry(QRect(20, 10, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(70, 70)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.myAccountButton = QPushButton()
        self.myAccountButton.setFixedSize(70, 70)
        self.myAccountButton.setText("My Account")
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setFixedSize(70, 70)
        self.logoutButton.setText("Log Out")
        self.logoutButton.clicked.connect(self.logout)

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

        # THIS LAYOUT IS ONLY FOR QWIDGET SWITCHING
        self.frameLayout = QVBoxLayout()

        doctorDashboard = DoctorDashboard(self.doctor)
        self.frameLayout.addWidget(doctorDashboard)

        self.mainLayout.addLayout(self.frameLayout, 11)

        self.centralwidget.setLayout(self.mainLayout)


        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):

        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation", "Are you sure you want to logout",
                                               QMessageBox.Yes | QMessageBox.No)
        if logoutDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()
