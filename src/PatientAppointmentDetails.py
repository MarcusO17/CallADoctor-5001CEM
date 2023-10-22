import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtCore, QtWidgets
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager


class PatientAppointmentDetailsWindow(QMainWindow):

    def __init__(self, appointmentTemp, doctorTemp, clinicTemp):
        super().__init__()
        self.pageManager = PageManager()
         #set the information here
        self.appointment = appointmentTemp
        self.doctor = doctorTemp
        self.clinic = clinicTemp
        print(self.clinic.getClinicID(), self.clinic.getClinicName(), self.clinic.getClinicContact(), self.clinic.getClinicAddress())
        print(self.doctor.getDoctorName(), self.doctor.getStatus())
        print(self.appointment.getAppointmentID(),self.appointment.getPatientID(), self.appointment.getDoctorID(), self.appointment.getAppointmentStatus(), self.appointment.getStartTime, self.appointment.getEndTime, self.appointment.getAppointmentDate(), self.appointment.getVisitReason())
        self.setWindowTitle("Patient Appointment Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("patientAppointment_details")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # header (probably reused in most files)
        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(self.appointment.getAppointmentID())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setFixedSize(70, 70)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.patientAppointmentPurposeLabel = QLabel(self.centralwidget)
        self.patientAppointmentPurposeLabel.setGeometry(QRect(180, 220, 400, 200))
        self.patientAppointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patientAppointmentPurposeLabel.setFont(font)
        self.patientAppointmentPurposeLabel.setText(str(self.appointment.getVisitReason()) + " " + str(self.appointment.getStartTime()) + " " + str(self.appointment.getEndTime() + " " + str(self.appointment.getAppointmentDate())))
        self.patientAppointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        

        self.doctorDetailsLabel = QLabel(self.centralwidget)
        self.doctorDetailsLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.doctorDetailsLabel.setFont(font)
        self.doctorDetailsLabel.setText(str(self.doctor.getDoctorName()) + " " + str(self.doctor.getStatus()) )
        self.doctorDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.clinicDetailsLabel = QLabel(self.centralwidget)
        self.clinicDetailsLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clinicDetailsLabel.setFont(font)
        self.clinicDetailsLabel.setText(str(self.clinic.getClinicName()) + " " + str(self.clinic.getClinicContact()) + " " + str(self.clinic.getClinicAddress()))
        self.clinicDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)


        self.cancelAppointmentButton = QPushButton(self.centralwidget)
        self.cancelAppointmentButton.setGeometry(QRect(890, 545, 180, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cancelAppointmentButton.setFont(font)
        self.cancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.cancelAppointmentButton.setText("Cancel Request")
        self.cancelAppointmentButton.clicked.connect(self.cancelAppointmentFunction)

        self.cancelAppointmentLabel = QLabel(self.centralwidget)
        self.cancelAppointmentLabel.setGeometry(QRect(910, 570, 50, 50))
        self.cancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.cancelAppointmentIcon = QPixmap(filepath)
        self.cancelAppointmentIcon = self.cancelAppointmentIcon.scaled(50, 50)
        self.cancelAppointmentLabel.setPixmap(self.cancelAppointmentIcon)


        self.patientDetailsContainer = QLabel(self.centralwidget)
        self.patientDetailsContainer.setFixedSize(1000,500)
        self.patientDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.patientDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

        # Cancel Appointment With Doctor
    
    def cancelAppointmentFunction(self):
        cancelAppointmentDialogBox = QMessageBox.question(self.centralWidget, "Cancel Confirmation",
                                                          "Are you sure you want to cancel Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if cancelAppointmentDialogBox == QMessageBox.Yes:
            self.appointment.setAppointmentStatus("Cancelled")
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()