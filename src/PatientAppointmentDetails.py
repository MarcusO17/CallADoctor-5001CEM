import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QTime
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QDialog, QLineEdit
from PyQt5 import QtCore, QtWidgets

from .AccountPage import AccountPage
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .model import Appointment, Prescription, PrescriptionDetails, PrescriptionRepo, Request
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager, FrameLayoutManager


class PatientAppointmentDetailsWindow(QWidget):

    def __init__(self, appointment, patient):
        super().__init__()
        self.appointment = appointment
        self.patient = patient
        # query the information here
        self.doctor = Doctor.getDoctorfromID(self.appointment.getDoctorID())
        self.clinic = Clinic.getClinicfromID(self.appointment.getClinicID())
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(self.appointment.getAppointmentID())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
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
        self.visitPurposeLabel.setText((f"{self.appointment.getVisitReason()} \n"
                                        f"Date: {self.appointment.getAppointmentDate()} \n"
                                        f"Start Time: {self.appointment.getStartTime()}"))
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
        self.cancelAppointmentButton.setText("Request Cancellation")
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

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.cancelAppointmentButton.raise_()
        self.cancelAppointmentLabel.raise_()
        self.viewPrescriptionLabel.raise_()
        self.viewPrescriptionButton.raise_()
        self.completeAppointmentButton.raise_()
        self.completeAppointmentLabel.raise_()

        self.setLayout(mainLayout)

    
    def cancelAppointmentFunction(self):
        self.requestCancellationDialog = QDialog(self)

        self.requestCancellationDialog.move(350, 200)
        self.requestCancellationDialog.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.requestCancellationDialog.setFixedSize(400, 400)

        self.requestCancellationDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.requestCancellationDialog.setWindowFlag(Qt.FramelessWindowHint)
        self.requestCancellationDialog.setWindowTitle("Request Cancellation")

        self.layout = QVBoxLayout()

        self.cancellationReasonLabel = QLineEdit()
        self.cancellationReasonLabel.setFixedSize(300,300)
        self.cancellationReasonLabel.setStyleSheet("background-color: white; border-radius: 10px;")
        self.cancellationReasonLabel.setPlaceholderText("Enter your cancellation reason here")
        self.layout.addWidget(self.cancellationReasonLabel)

        confirmationButtonLayout = QHBoxLayout()

        cancelButton = QPushButton()
        cancelButton.setText("Cancel")
        cancelButton.clicked.connect(lambda checked: self.requestCancellationDialog.close())
        cancelButton.setStyleSheet("background-color: white; border-radius: 10px;")
        confirmationButtonLayout.addWidget(cancelButton)

        confirmationButton = QPushButton()
        confirmationButton.setText("Confirm")
        confirmationButton.clicked.connect(lambda checked: self.completeButtonConfirmationFunction(self.cancellationReasonLabel.text()))
        confirmationButton.setStyleSheet("background-color: white; border-radius: 10px;")
        confirmationButtonLayout.addWidget(confirmationButton)

        self.layout.addLayout(confirmationButtonLayout)
        self.requestCancellationDialog.setLayout(self.layout)
        self.requestCancellationDialog.exec_()

    def completeButtonConfirmationFunction(self, reason):

        request = Request(None, "Cancellation", self.patient.getPatientID(), "Pending", QTime.currentTime().toString("hh:mm:ss"), reason, self.appointment.getAppointmentID())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.requestCancellationDialog.close()
        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def viewPrescription(self):
        prescription = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByAppointment(self.appointment.getAppointmentID())   
        self.patientPrescriptionDetails = PatientPrescriptionDetailsWindow(prescription,self.patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientPrescriptionDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def completeAppointment(self):
        cancelAppointmentDialogBox = QMessageBox.question(self, "Complete Confirmation",
                                                          "Are you sure you want to complete Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if cancelAppointmentDialogBox == QMessageBox.Yes:
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.appointment.setAppointmentStatus("Complete")
            self.appointment.completeAppointment()

            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def setMode(self, mode):
        if mode == "Completed":
            self.viewPrescriptionButton.show()
            self.viewPrescriptionLabel.show()
        elif mode == "Approved":
            self.cancelAppointmentButton.show()
            self.cancelAppointmentLabel.show()
            self.completeAppointmentLabel.show()
            self.completeAppointmentButton.show()

        self.cancelAppointmentShow()

    def cancelAppointmentShow(self):
        appointmentStartTime = self.appointment.getStartTime().split(":")

        print(appointmentStartTime)
        currentTime = QTime.currentTime()
        startTime = QTime(int(appointmentStartTime[0]), int(appointmentStartTime[1]))

        timeDiff = currentTime.secsTo(startTime)

        if timeDiff < 7200 and timeDiff > 0:
            self.cancelAppointmentButton.hide()
            self.cancelAppointmentLabel.hide()