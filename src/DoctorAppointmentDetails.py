import os
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea
from PyQt5 import QtCore, QtWidgets

from .DoctorGeneratePrescription import DoctorGeneratePrescription
from .DoctorViewPrescription import DoctorViewPrescription
from .PageManager import PageManager
from .model import Patient


class DoctorAppointmentDetails(QMainWindow):

    def __init__(self, appointment, doctor):
        super().__init__()
        self.pageManager = PageManager()
        self.appointment = appointment
        self.doctor = doctor

        # query the patient with patient ID from appointment

        self.patient = Patient("p0001", "Patient 1", "Patient 1 address", "2001-01-30", "ABC", "Indian")

        self.setWindowTitle("Patient Appointment Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):

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
        self.headerTitle.setText(f"{self.patient.getPatientName()} - {self.appointment.getAppointmentID()}")
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

        self.appointmentPurposeLabel = QLabel(self.centralwidget)
        self.appointmentPurposeLabel.setGeometry(QRect(180, 220, 400, 200))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.appointmentPurposeLabel.setFont(font)
        self.appointmentPurposeLabel.setText(self.appointment.getVisitReason())
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.patientDetailsLabel = QLabel(self.centralwidget)
        self.patientDetailsLabel.setGeometry(QRect(700, 220, 375, 200))
        self.patientDetailsLabel.setFont(font)
        self.patientDetailsLabel.setText("Patient Details")
        self.patientDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.patientAddressLabel = QLabel(self.centralwidget)
        self.patientAddressLabel.setGeometry(QRect(180, 470, 400, 200))
        self.patientAddressLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.patientAddressLabel.setText(self.patient.getPatientAddress())

        self.generatePrescriptionButton = QPushButton(self.centralwidget)
        self.generatePrescriptionButton.setGeometry(QRect(790, 450, 280, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.generatePrescriptionButton.setFont(font)
        self.generatePrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.generatePrescriptionButton.setText("Generate Prescription")
        self.generatePrescriptionButton.setStyleSheet("padding-right: 30px")
        self.generatePrescriptionButton.clicked.connect(self.generatePrescription)

        self.generatePrescriptionLabel = QLabel(self.centralwidget)
        self.generatePrescriptionLabel.setGeometry(QRect(810, 475, 50, 50))
        self.generatePrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.generatePrescriptionIcon = QPixmap(filepath)
        self.generatePrescriptionIcon = self.generatePrescriptionIcon.scaled(50, 50)
        self.generatePrescriptionLabel.setPixmap(self.generatePrescriptionIcon)

        self.requestCancelAppointmentButton = QPushButton(self.centralwidget)
        self.requestCancelAppointmentButton.setGeometry(QRect(790, 565, 280, 100))
        self.requestCancelAppointmentButton.setFont(font)
        self.requestCancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.requestCancelAppointmentButton.setText("Request Cancel")
        self.requestCancelAppointmentButton.clicked.connect(self.requestCancelAppointmentFunction)

        self.requestCancelAppointmentLabel = QLabel(self.centralwidget)
        self.requestCancelAppointmentLabel.setGeometry(QRect(810, 590, 50, 50))
        self.requestCancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.requestCancelAppointmentIcon = QPixmap(filepath)
        self.requestCancelAppointmentIcon = self.requestCancelAppointmentIcon.scaled(50, 50)
        self.requestCancelAppointmentLabel.setPixmap(self.requestCancelAppointmentIcon)

        self.viewPrescriptionButton = QPushButton(self.centralwidget)
        self.viewPrescriptionButton.setGeometry(QRect(790, 565, 280, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.viewPrescriptionButton.setFont(font)
        self.viewPrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.viewPrescriptionButton.setText("View Prescription")
        self.viewPrescriptionButton.setStyleSheet("padding-right: 30px")
        self.viewPrescriptionButton.clicked.connect(self.viewPrescription)

        self.viewPrescriptionLabel = QLabel(self.centralwidget)
        self.viewPrescriptionLabel.setGeometry(QRect(810, 590, 50, 50))
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

        self.appointmentDetailsContainer = QLabel(self.centralwidget)
        self.appointmentDetailsContainer.setFixedSize(1000, 500)
        self.appointmentDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(20)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.appointmentDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.requestCancelAppointmentButton.raise_()
        self.requestCancelAppointmentLabel.raise_()
        self.generatePrescriptionButton.raise_()
        self.generatePrescriptionLabel.raise_()
        self.viewPrescriptionLabel.raise_()
        self.viewPrescriptionButton.raise_()

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

        # Cancel Appointment With Doctor

    def requestCancelAppointmentFunction(self):
        requestCancelAppointmentDialogBox = QMessageBox.question(self, "Request Cancel Confirmation",
                                                          "Are you sure you want to request cancel Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if requestCancelAppointmentDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()

    def generatePrescription(self):
        self.doctorGeneratePrescription = DoctorGeneratePrescription(self.patient, self.appointment)
        self.pageManager.add(self.doctorGeneratePrescription)

    def viewPrescription(self):
        self.doctorViewPrescription = DoctorViewPrescription(self.patient, self.appointment)
        self.pageManager.add(self.doctorViewPrescription)

    def backButtonFunction(self):
        self.pageManager.goBack()

    def setMode(self, mode):
        if mode == "Completed":
            self.viewPrescriptionLabel.show()
            self.viewPrescriptionButton.show()
        elif mode == "Approved":
            self.generatePrescriptionButton.show()
            self.generatePrescriptionLabel.show()
            self.requestCancelAppointmentLabel.show()
            self.requestCancelAppointmentButton.show()