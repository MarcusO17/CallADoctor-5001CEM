import os
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QTime, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QLineEdit, QDialog, QGraphicsDropShadowEffect
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
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(f"{self.patient.getPatientName()} - {self.appointment.getAppointmentID()}")
        self.headerTitle.setGeometry(QRect(80, 40, 700, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(800, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-back-64.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonFunction)
        self.backButton.setStyleSheet("""QPushButton#backButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;

                                                        }
                                                        QPushButton#backButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                        }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.backButton.setGraphicsEffect(effect)

        detailsContainer = QLabel(self.centralwidget)
        detailsContainer.setGeometry(QRect(20, 150, 900, 500))
        detailsContainer.setStyleSheet("""QLabel {
                                                background: #D0BFFF;
                                                border-radius: 10px;
                                                }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        detailsContainer.setGraphicsEffect(effect)

        self.appointmentPurposeTitle = QLabel(self.centralwidget)
        self.appointmentPurposeTitle.setGeometry(QRect(50, 190, 150, 40))
        self.appointmentPurposeTitle.setText("Appointment Purpose: ")

        self.appointmentPurposeLabel = QLabel(self.centralwidget)
        self.appointmentPurposeLabel.setGeometry(QRect(50, 220, 400, 200))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.appointmentPurposeLabel.setFont(font)
        self.appointmentPurposeLabel.setText(f"{self.appointment.getVisitReason()}")
        self.appointmentPurposeLabel.setWordWrap(True)
        self.appointmentPurposeLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.appointmentPurposeLabel.setStyleSheet("""QLabel {
                                                                border-radius: 10px;
                                                                border: 1px solid black;
                                                                background: white;
                                                                }""")

        self.patientDetailsTitle = QLabel(self.centralwidget)
        self.patientDetailsTitle.setGeometry(QRect(520, 190, 150, 40))
        self.patientDetailsTitle.setText("Patient Details: ")

        self.patientDetailsLabel = QLabel(self.centralwidget)
        self.patientDetailsLabel.setGeometry(QRect(520, 220, 375, 200))
        self.patientDetailsLabel.setFont(font)
        self.patientDetailsLabel.setText(f"Patient ID: {self.patient.getPatientID()}\n"
                                        f"Patient Name: {self.patient.getPatientName()}\n"
                                        f"Patient Blood: {self.patient.getPatientBlood()}\n"
                                        f"Patient Race: {self.patient.getPatientRace()}\n"
                                        f"Date of Birth: {self.patient.getPatientDOB()}\n")
        self.patientDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.patientDetailsLabel.setStyleSheet("""QLabel {
                                                        border-radius: 10px;
                                                        border: 1px solid black;
                                                        background: white;
                                                        }""")
        self.patientDetailsLabel.setWordWrap(True)
        self.patientDetailsLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.patientAddressTitle = QLabel(self.centralwidget)
        self.patientAddressTitle.setGeometry(QRect(50, 470, 150, 40))
        self.patientAddressTitle.setText("Patient Address: ")

        self.patientAddressLabel = QLabel(self.centralwidget)
        self.patientAddressLabel.setGeometry(QRect(50, 500, 400, 200))
        self.patientAddressLabel.setFont(font)
        self.patientAddressLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.patientAddressLabel.setText(self.patient.getPatientAddress())
        self.patientAddressLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")
        self.patientAddressLabel.setWordWrap(True)
        self.patientAddressLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)

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
        self.requestCancelAppointmentButton.setGeometry(QRect(520, 510, 325, 100))
        self.requestCancelAppointmentButton.setFont(font)
        self.requestCancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.requestCancelAppointmentButton.setText("Request Cancel")
        self.requestCancelAppointmentButton.clicked.connect(self.requestCancelAppointmentFunction)

        self.requestCancelAppointmentLabel = QLabel(self.centralwidget)
        self.requestCancelAppointmentLabel.setGeometry(QRect(540, 535, 50, 50))
        self.requestCancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.requestCancelAppointmentIcon = QPixmap(filepath)
        self.requestCancelAppointmentIcon = self.requestCancelAppointmentIcon.scaled(50, 50)
        self.requestCancelAppointmentLabel.setPixmap(self.requestCancelAppointmentIcon)

        self.viewPrescriptionButton = QPushButton(self.centralwidget)
        self.viewPrescriptionButton.setGeometry(QRect(520, 510, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.viewPrescriptionButton.setFont(font)
        self.viewPrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.viewPrescriptionButton.setText("View Prescription")
        self.viewPrescriptionButton.setStyleSheet("padding-right: 30px")
        self.viewPrescriptionButton.clicked.connect(self.viewPrescription)

        self.viewPrescriptionLabel = QLabel(self.centralwidget)
        self.viewPrescriptionLabel.setGeometry(QRect(540, 535, 50, 50))
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