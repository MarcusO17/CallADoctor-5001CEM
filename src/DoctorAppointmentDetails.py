import os
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QTime
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QLineEdit, QDialog
from PyQt5 import QtCore, QtWidgets

from .AccountPage import AccountPage
from .DoctorGeneratePrescription import DoctorGeneratePrescription
from .DoctorViewPrescription import DoctorViewPrescription
from .PageManager import PageManager, FrameLayoutManager
from .model import Patient, Request


class DoctorAppointmentDetails(QWidget):

    def __init__(self, appointment, doctor):
        super().__init__()
        self.appointment = appointment
        self.doctor = doctor

        # query the patient with patient ID from appointment

        self.patient = Patient.getPatientfromID(self.appointment.getPatientID())

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
        self.headerTitle.setText(f"{self.patient.getPatientName()} - {self.appointment.getAppointmentID()}")
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

        self.appointmentPurposeLabel = QLabel(self.centralwidget)
        self.appointmentPurposeLabel.setGeometry(QRect(80, 170, 400, 200))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.appointmentPurposeLabel.setFont(font)
        self.appointmentPurposeLabel.setText(f"{self.appointment.getVisitReason()} \n"
                                             f"Date: {self.appointment.getAppointmentDate()} \n"
                                             f"Start Time: {self.appointment.getStartTime()}")
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.patientDetailsLabel = QLabel(self.centralwidget)
        self.patientDetailsLabel.setGeometry(QRect(600, 170, 375, 200))
        self.patientDetailsLabel.setFont(font)
        self.patientDetailsLabel.setText("Patient Details")
        self.patientDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.patientAddressLabel = QLabel(self.centralwidget)
        self.patientAddressLabel.setGeometry(QRect(80, 420, 400, 200))
        self.patientAddressLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.patientAddressLabel.setText(self.patient.getPatientAddress())

        self.generatePrescriptionButton = QPushButton(self.centralwidget)
        self.generatePrescriptionButton.setGeometry(QRect(690, 400, 280, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.generatePrescriptionButton.setFont(font)
        self.generatePrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.generatePrescriptionButton.setText("Generate Prescription")
        self.generatePrescriptionButton.setStyleSheet("padding-right: 30px")
        self.generatePrescriptionButton.clicked.connect(self.generatePrescription)

        self.generatePrescriptionLabel = QLabel(self.centralwidget)
        self.generatePrescriptionLabel.setGeometry(QRect(710, 425, 50, 50))
        self.generatePrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.generatePrescriptionIcon = QPixmap(filepath)
        self.generatePrescriptionIcon = self.generatePrescriptionIcon.scaled(50, 50)
        self.generatePrescriptionLabel.setPixmap(self.generatePrescriptionIcon)

        self.requestCancelAppointmentButton = QPushButton(self.centralwidget)
        self.requestCancelAppointmentButton.setGeometry(QRect(690, 515, 280, 100))
        self.requestCancelAppointmentButton.setFont(font)
        self.requestCancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.requestCancelAppointmentButton.setText("Request Cancel")
        self.requestCancelAppointmentButton.clicked.connect(self.requestCancelAppointmentFunction)

        self.requestCancelAppointmentLabel = QLabel(self.centralwidget)
        self.requestCancelAppointmentLabel.setGeometry(QRect(710, 540, 50, 50))
        self.requestCancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.requestCancelAppointmentIcon = QPixmap(filepath)
        self.requestCancelAppointmentIcon = self.requestCancelAppointmentIcon.scaled(50, 50)
        self.requestCancelAppointmentLabel.setPixmap(self.requestCancelAppointmentIcon)

        self.viewPrescriptionButton = QPushButton(self.centralwidget)
        self.viewPrescriptionButton.setGeometry(QRect(690, 515, 280, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.viewPrescriptionButton.setFont(font)
        self.viewPrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.viewPrescriptionButton.setText("View Prescription")
        self.viewPrescriptionButton.setStyleSheet("padding-right: 30px")
        self.viewPrescriptionButton.clicked.connect(self.viewPrescription)

        self.viewPrescriptionLabel = QLabel(self.centralwidget)
        self.viewPrescriptionLabel.setGeometry(QRect(710, 540, 50, 50))
        self.viewPrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.viewPrescriptionIcon = QPixmap(filepath)
        self.viewPrescriptionIcon = self.viewPrescriptionIcon.scaled(50, 50)
        self.viewPrescriptionLabel.setPixmap(self.viewPrescriptionIcon)

        self.requestCancelAppointmentLabel.hide()
        self.requestCancelAppointmentButton.hide()
        self.generatePrescriptionButton.hide()
        self.generatePrescriptionLabel.hide()
        self.viewPrescriptionLabel.hide()
        self.viewPrescriptionButton.hide()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)


        self.requestCancelAppointmentButton.raise_()
        self.requestCancelAppointmentLabel.raise_()
        self.generatePrescriptionButton.raise_()
        self.generatePrescriptionLabel.raise_()
        self.viewPrescriptionLabel.raise_()
        self.viewPrescriptionButton.raise_()

        self.setLayout(mainLayout)


        # Cancel Appointment With Doctor

    def requestCancelAppointmentFunction(self):
        self.requestCancellationDialog = QDialog(self)

        self.requestCancellationDialog.move(350, 200)
        self.requestCancellationDialog.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.requestCancellationDialog.setFixedSize(400, 400)

        self.requestCancellationDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.requestCancellationDialog.setWindowFlag(Qt.FramelessWindowHint)
        self.requestCancellationDialog.setWindowTitle("Request Cancellation")

        self.layout = QVBoxLayout()

        self.cancellationReasonLabel = QLineEdit()
        self.cancellationReasonLabel.setFixedSize(300, 300)
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
        confirmationButton.clicked.connect(
            lambda checked: self.completeButtonConfirmationFunction(self.cancellationReasonLabel.text()))
        confirmationButton.setStyleSheet("background-color: white; border-radius: 10px;")
        confirmationButtonLayout.addWidget(confirmationButton)

        self.layout.addLayout(confirmationButtonLayout)
        self.requestCancellationDialog.setLayout(self.layout)
        self.requestCancellationDialog.exec_()

    def completeButtonConfirmationFunction(self, reason):

        request = Request(None, "Cancellation", self.doctor.getDoctorID(), "Pending", QTime.currentTime().toString("hh:mm:ss"), reason, self.appointment.getAppointmentID())
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.requestCancellationDialog.close()
        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generatePrescription(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        print("GENERATE PRESCRIPTION WINDOW MADE" )
        self.doctorGeneratePrescription = DoctorGeneratePrescription(self.patient, self.appointment, self.doctor)
        self.frameLayout.addWidget(self.doctorGeneratePrescription)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
    def viewPrescription(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.doctorViewPrescription = DoctorViewPrescription(self.patient, self.appointment, self.doctor)
        self.frameLayout.addWidget(self.doctorGeneratePrescription)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def setMode(self, mode):
        if mode == "Completed":
            self.viewPrescriptionLabel.show()
            self.viewPrescriptionButton.show()
        elif mode == "Approved":
            self.generatePrescriptionButton.show()
            self.generatePrescriptionLabel.show()
            self.requestCancelAppointmentLabel.show()
            self.requestCancelAppointmentButton.show()

        self.cancelAppointmentShow()

    def cancelAppointmentShow(self):
        appointmentStartTime = self.appointment.getStartTime().split(":")

        currentTime = QTime.currentTime()
        startTime = QTime(int(appointmentStartTime[0]), int(appointmentStartTime[1]), int(appointmentStartTime[2]))

        timeDiff = currentTime.secsTo(startTime)

        if timeDiff < 7200 and timeDiff > 0:
            self.requestCancelAppointmentLabel.hide()
            self.requestCancelAppointmentButton.hide()