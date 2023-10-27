import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtCore, QtWidgets

from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .model import Appointment, Prescription, PrescriptionDetails, PrescriptionRepo
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager

class PatientAppointmentDetailsWindow(QMainWindow):

    def __init__(self, appointment, patient):
        super().__init__()
        self.pageManager = PageManager()
        self.appointment = appointment
        self.patient = patient
        # query the information here
        self.doctor = Doctor("D0001", "Doctor1", "C0001", "Status", "DoctorType", "Doctor Contact", "IC number", 3)
        self.clinic = Clinic("C0001", "clinicName","clinicContact" ,"clinicAddress","Approved")
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

        self.visitPurposeLabel = QLabel(self.centralwidget)
        self.visitPurposeLabel.setGeometry(QRect(180, 220, 400, 200))
        self.visitPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.visitPurposeLabel.setFont(font)
        self.visitPurposeLabel.setText(str(self.appointment.getVisitReason()) + " " + str(self.appointment.getStartTime()) + " " + str(self.appointment.getEndTime() + " " + str(self.appointment.getAppointmentDate())))
        self.visitPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        

        self.doctorDetailsLabel = QLabel(self.centralwidget)
        self.doctorDetailsLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.doctorDetailsLabel.setFont(font)
        self.doctorDetailsLabel.setText(f"Doctor Name: {self.doctor.getDoctorName()} \n"
                                        f"Doctor ID: {self.doctor.getDoctorID()} \n"
                                        f"Doctor Type: {self.doctor.getDoctorType()} \n"
                                        f"Years Of Experience: {str(self.doctor.getYearsOfExperience())} \n"
                                        f"Doctor Contact: {self.doctor.getDoctorContact()} \n")
        self.doctorDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.clinicDetailsLabel = QLabel(self.centralwidget)
        self.clinicDetailsLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clinicDetailsLabel.setFont(font)
        self.clinicDetailsLabel.setText(f"Clinic Name: {self.clinic.getClinicName()} \n"
                                        f"Clinic ID: {self.clinic.getClinicID()} \n"
                                        f"Clinic Contact: {self.clinic.getClinicContact()} \n"
                                        f"Clinic Address: {self.clinic.getClinicAddress()}")
        self.clinicDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.cancelAppointmentButton = QPushButton(self.centralwidget)
        self.cancelAppointmentButton.setGeometry(QRect(790, 545, 280, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cancelAppointmentButton.setFont(font)
        self.cancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.cancelAppointmentButton.setText("Cancel Request")
        self.cancelAppointmentButton.clicked.connect(self.cancelAppointmentFunction)

        self.cancelAppointmentLabel = QLabel(self.centralwidget)
        self.cancelAppointmentLabel.setGeometry(QRect(810, 570, 50, 50))
        self.cancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.cancelAppointmentIcon = QPixmap(filepath)
        self.cancelAppointmentIcon = self.cancelAppointmentIcon.scaled(50, 50)
        self.cancelAppointmentLabel.setPixmap(self.cancelAppointmentIcon)

        self.viewPrescriptionButton = QPushButton(self.centralwidget)
        self.viewPrescriptionButton.setGeometry(QRect(790, 545, 280, 100))
        self.viewPrescriptionButton.setFont(font)
        self.viewPrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.viewPrescriptionButton.setText("View Prescription")
        self.viewPrescriptionButton.clicked.connect(self.viewPrescription)

        self.viewPrescriptionLabel = QLabel(self.centralwidget)
        self.viewPrescriptionLabel.setGeometry(QRect(810, 570, 50, 50))
        self.viewPrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.viewPrescriptionIcon = QPixmap(filepath)
        self.viewPrescriptionIcon = self.viewPrescriptionIcon.scaled(50, 50)
        self.viewPrescriptionLabel.setPixmap(self.viewPrescriptionIcon)

        self.completeAppointmentButton = QPushButton(self.centralwidget)
        self.completeAppointmentButton.setGeometry(QRect(790, 445, 280, 100))
        self.completeAppointmentButton.setFont(font)
        self.completeAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.completeAppointmentButton.setText("Complete Appointment")
        self.completeAppointmentButton.clicked.connect(self.completeAppointment)

        self.completeAppointmentLabel = QLabel(self.centralwidget)
        self.completeAppointmentLabel.setGeometry(QRect(810, 470, 50, 50))
        self.completeAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.completeAppointmentIcon = QPixmap(filepath)
        self.completeAppointmentIcon = self.completeAppointmentIcon.scaled(50, 50)
        self.completeAppointmentLabel.setPixmap(self.completeAppointmentIcon)

        self.cancelAppointmentLabel.hide()
        self.cancelAppointmentButton.hide()
        self.viewPrescriptionLabel.hide()
        self.viewPrescriptionButton.hide()
        self.completeAppointmentButton.hide()
        self.completeAppointmentLabel.hide()

        self.appointmentContainer = QLabel(self.centralwidget)
        self.appointmentContainer.setFixedSize(1000,500)
        self.appointmentContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.appointmentContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.cancelAppointmentButton.raise_()
        self.cancelAppointmentLabel.raise_()
        self.viewPrescriptionLabel.raise_()
        self.viewPrescriptionButton.raise_()
        self.completeAppointmentButton.raise_()
        self.completeAppointmentLabel.raise_()

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

        # Cancel Appointment With Doctor
    
    def cancelAppointmentFunction(self):
        cancelAppointmentDialogBox = QMessageBox.question(self, "Cancel Confirmation",
                                                          "Are you sure you want to cancel Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if cancelAppointmentDialogBox == QMessageBox.Yes:
            #SET CANCELLATIONS
            self.appointment.setAppointmentStatus("Cancelled")
            self.pageManager.getPreviousPage().generateAppointmentButtons()
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()

    def viewPrescription(self):
        prescription = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByAppointment(self.appointment.getAppointmentID())   
        self.patientPrescriptionDetails = PatientPrescriptionDetailsWindow(self.patient, prescription)
        self.pageManager.add(self.patientPrescriptionDetails)

    def completeAppointment(self):
        cancelAppointmentDialogBox = QMessageBox.question(self, "Complete Confirmation",
                                                          "Are you sure you want to complete Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if cancelAppointmentDialogBox == QMessageBox.Yes:
            self.appointment.setAppointmentStatus("Complete")
            self.appointment.completeAppointment()
            self.pageManager.getPreviousPage().generateAppointmentButtons()
            self.pageManager.goBack()

    def setMode(self, mode):
        if mode == "Completed":
            self.viewPrescriptionButton.show()
            self.viewPrescriptionLabel.show()
        elif mode == "Approved":
            self.cancelAppointmentButton.show()
            self.cancelAppointmentLabel.show()
            self.completeAppointmentLabel.show()
            self.completeAppointmentButton.show()