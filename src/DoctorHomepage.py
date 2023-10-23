import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, \
    QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore

from .DoctorScheduleWindow import DoctorScheduleWindow
from .PageManager import PageManager
from .model import Doctor
from .DocMyAppointment import DocMyAppointmentWindow
from .DocPatientRecord import DocPatientRecordWindow



class DoctorHomepage(QMainWindow):
    def __init__(self, sessionID):
        super().__init__()
        self.pageManager = PageManager()
        # not implemented yet
        #self.doctor = Doctor.getDoctorfromID(sessionID)
        self.setWindowTitle("Doctor Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def gotoSchedule(self):
        self.doctorScheduleWindow = DoctorScheduleWindow()
        self.pageManager.add(self.doctorScheduleWindow)
        print(self.pageManager.size())

    def gotoPatientRecord(self):
        self.doctor = Doctor("D0001", "Doctor 1", "C0001", "status", "doctortype", "doctorContact", "doctorICNUmber", 5)
        self.docPatientRecord = DocPatientRecordWindow(self.doctor)
        self.pageManager.add(self.docPatientRecord)
        print(self.pageManager.size())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DoctorHomepage")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label, Icon and Button for Schedule
        self.scheduleButton = QtWidgets.QPushButton(self.centralwidget)
        self.scheduleButton.setGeometry(QtCore.QRect(150, 200, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.scheduleButton.setFont(font)
        self.scheduleButton.setObjectName("schedule")
        self.scheduleButton.setText("Schedule")
        self.scheduleButton.clicked.connect(self.gotoSchedule)

        self.scheduleLabel = QtWidgets.QLabel(self.centralwidget)
        self.scheduleLabel.setGeometry(QtCore.QRect(170, 225, 50, 50))
        self.scheduleLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.scheduleIcon = QPixmap(filepath)
        self.scheduleIcon = self.scheduleIcon.scaled(50, 50)
        self.scheduleLabel.setPixmap(self.scheduleIcon)

        # Button, Label and Icon for Patient Record
        self.patientRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.patientRecordButton.setGeometry(QtCore.QRect(700, 200, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.patientRecordButton.setFont(font)
        self.patientRecordButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.patientRecordButton.setObjectName("PatientRecord")
        self.patientRecordButton.setText("Patient Record")
        self.patientRecordButton.clicked.connect(self.gotoPatientRecord)


        self.patientRecordLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientRecordLabel.setGeometry(QtCore.QRect(720, 225, 50, 50))
        self.patientRecordLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.patientRecordIcon = QPixmap(filepath)
        self.patientRecordIcon = self.patientRecordIcon.scaled(50, 50)
        self.patientRecordLabel.setPixmap(self.patientRecordIcon)

        # Button, Label, Icon for Doctors My Appointment
        self.docMyAppointmentsButton = QtWidgets.QPushButton(self.centralwidget)
        self.docMyAppointmentsButton.setGeometry(QtCore.QRect(150, 400, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.docMyAppointmentsButton.setFont(font)
        self.docMyAppointmentsButton.setObjectName("DocMyAppointments")
        self.docMyAppointmentsButton.setLayoutDirection(Qt.LeftToRight)
        self.docMyAppointmentsButton.setText("My Appointments")

        self.docMyAppointmentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.docMyAppointmentsLabel.setGeometry(QtCore.QRect(175, 425, 50, 50))
        self.docMyAppointmentsLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.docMyAppointmentsIcon = QPixmap(filepath)
        self.docMyAppointmentsIcon = self.docMyAppointmentsIcon.scaled(50, 50)
        self.docMyAppointmentsLabel.setPixmap(self.docMyAppointmentsIcon)

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
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QRect(1150, 40, 70, 70))
        self.logoutButton.setIconSize(QSize(70, 70))
        self.logoutButton.setText("Log Out")
        self.logoutButton.clicked.connect(self.logout)

        MainWindow.setCentralWidget(self.centralwidget)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):

        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation", "Are you sure you want to logout",
                                               QMessageBox.Yes | QMessageBox.No)
        if logoutDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()
