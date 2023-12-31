import os
import sys
import typing
import requests
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QTime, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QDialog, QLineEdit, QGraphicsDropShadowEffect
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
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(self.appointment.getAppointmentID())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
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
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(800, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-back-64.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setObjectName("backButton")
        self.backButton.setIcon(self.backIcon)
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

        self.visitPurposeTitle = QLabel(self.centralwidget)
        self.visitPurposeTitle.setGeometry(QRect(50, 160, 150, 40))
        self.visitPurposeTitle.setText("Appointment Purpose: ")


        self.visitPurposeLabel = QLabel(self.centralwidget)
        self.visitPurposeLabel.setGeometry(QRect(50, 190, 400, 200))
        self.visitPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.visitPurposeLabel.setFont(font)
        self.visitPurposeLabel.setText((f"Appointment Purpose:{self.appointment.getVisitReason()} \n"
                                        f"Date: {self.appointment.getAppointmentDate()} \n"
                                        f"Start Time: {self.appointment.getStartTime()}"))
        self.visitPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.visitPurposeLabel.setWordWrap(True)
        self.visitPurposeLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.visitPurposeLabel.setStyleSheet("""QLabel {
                                                            border-radius: 10px;
                                                            border: 1px solid black;
                                                            background: white;
                                                            }""")
        
        self.doctorDetailsTitle = QLabel(self.centralwidget)
        self.doctorDetailsTitle.setGeometry(QRect(520, 160, 150, 40))
        self.doctorDetailsTitle.setText("Doctor Details: ")

        self.doctorDetailsLabel = QLabel(self.centralwidget)
        self.doctorDetailsLabel.setGeometry(QRect(520, 190, 375, 200))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.doctorDetailsLabel.setFont(font)
        self.doctorDetailsLabel.setText(f"Doctor Name: {self.doctor.getDoctorName()} \n"
                                        f"Doctor ID: {self.doctor.getDoctorID()} \n"
                                        f"Doctor Type: {self.doctor.getDoctorType()} \n"
                                        f"Years Of Experience: {str(self.doctor.getYearsOfExperience())} \n"
                                        f"Doctor Contact: {self.doctor.getDoctorContact()} \n")
        self.doctorDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorDetailsLabel.setStyleSheet("""QLabel {
                                                        border-radius: 10px;
                                                        border: 1px solid black;
                                                        background: white;
                                                        }""")
        self.doctorDetailsLabel.setWordWrap(True)
        self.doctorDetailsLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.clinicDetailsTitle = QLabel(self.centralwidget)
        self.clinicDetailsTitle.setGeometry(QRect(50, 400, 150, 40))
        self.clinicDetailsTitle.setText("Clinic Address: ")

        self.clinicDetailsLabel = QLabel(self.centralwidget)
        self.clinicDetailsLabel.setGeometry(QRect(50, 430, 400, 200))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.clinicDetailsLabel.setFont(font)
        self.clinicDetailsLabel.setText(f"Clinic Name: {self.clinic.getClinicName()} \n"
                                        f"Clinic ID: {self.clinic.getClinicID()} \n"
                                        f"Clinic Contact: {self.clinic.getClinicContact()} \n"
                                        f"Clinic Address: {self.clinic.getClinicAddress()}")
        self.clinicDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.clinicDetailsLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")
        self.clinicDetailsLabel.setWordWrap(True)
        self.clinicDetailsLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.cancelAppointmentButton = QPushButton(self.centralwidget)
        self.cancelAppointmentButton.setGeometry(QRect(520, 530, 325, 100))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.cancelAppointmentButton.setFont(font)
        self.cancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.cancelAppointmentButton.setText("Request Cancellation")
        self.cancelAppointmentButton.clicked.connect(self.cancelAppointmentFunction)
        self.cancelAppointmentButton.setStyleSheet("""QPushButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;
                                                        text-align: center; 
                                                        color:white;
                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                          text-align: center; 
                                                          color:white;
                                                        }""")
                                                        

        self.cancelAppointmentLabel = QLabel(self.centralwidget)
        self.cancelAppointmentLabel.setGeometry(QRect(540, 555, 50, 50))
        self.cancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-appointment-50.png")
        self.cancelAppointmentIcon = QPixmap(filepath)
        self.cancelAppointmentIcon = self.cancelAppointmentIcon.scaled(50, 50)
        self.cancelAppointmentLabel.setPixmap(self.cancelAppointmentIcon)

        self.viewPrescriptionButton = QPushButton(self.centralwidget)
        self.viewPrescriptionButton.setGeometry(QRect(520, 420, 325, 100))
        self.viewPrescriptionButton.setFont(font)
        self.viewPrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        self.viewPrescriptionButton.setText("View Prescription")
        self.viewPrescriptionButton.clicked.connect(self.viewPrescription)
        self.viewPrescriptionButton.setStyleSheet("""QPushButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;
                                                        text-align: center; 
                                                        color:white;
                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                          text-align: center; 
                                                          color:white;
                                                        }""")

        self.viewPrescriptionLabel = QLabel(self.centralwidget)
        self.viewPrescriptionLabel.setGeometry(QRect(540, 445, 50, 50))
        self.viewPrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-prescription-50.png")
        self.viewPrescriptionIcon = QPixmap(filepath)
        self.viewPrescriptionIcon = self.viewPrescriptionIcon.scaled(50, 50)
        self.viewPrescriptionLabel.setPixmap(self.viewPrescriptionIcon)

        self.completeAppointmentButton = QPushButton(self.centralwidget)
        self.completeAppointmentButton.setGeometry(QRect(520, 420, 325, 100))
        self.completeAppointmentButton.setFont(font)
        self.completeAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.completeAppointmentButton.setText("Complete Appointment")
        self.completeAppointmentButton.clicked.connect(self.completeAppointment)
        self.completeAppointmentButton.setStyleSheet("""QPushButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;
                                                        text-align: center; 
                                                        color:white;
                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                          text-align: center; 
                                                          color:white;
                                                        }""")

        self.completeAppointmentLabel = QLabel(self.centralwidget)
        self.completeAppointmentLabel.setGeometry(QRect(540, 445, 50, 50))
        self.completeAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-paid-bill-50.png")
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
        self.viewPrescriptionButton.raise_()
        self.viewPrescriptionLabel.raise_()
        self.completeAppointmentButton.raise_()
        self.completeAppointmentLabel.raise_()
        
        self.setLayout(mainLayout)

    # this method is triggered when request cancellation button is clicked
    def cancelAppointmentFunction(self):
        self.requestCancellationDialog = QDialog(self)

        self.requestCancellationDialog.move(350, 200)
        self.requestCancellationDialog.setStyleSheet("""QDialog {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                stop: 0 rgba(25, 4, 130, 255), 
                                                stop: 1 rgba(119, 82, 254, 255)
                                            );
                                            border-radius: 10px;
                                            }""")
        self.requestCancellationDialog.setFixedSize(400, 400)

        self.requestCancellationDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.requestCancellationDialog.setWindowFlag(Qt.FramelessWindowHint)
        self.requestCancellationDialog.setWindowTitle("Request Cancellation")

        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)

        titleFont = QFont()
        titleFont.setFamily("Montserrat")
        titleFont.setPointSize(10)

        self.cancelAppointmentTitle = QLabel()
        self.cancelAppointmentTitle.setText("State reason of cancellation:")
        self.cancelAppointmentTitle.setFont(titleFont)
        self.cancelAppointmentTitle.setStyleSheet("QLabel {color: white}")
        self.cancelAppointmentTitle.setFixedSize(200, 30)
        self.layout.addWidget(self.cancelAppointmentTitle)

        self.cancellationReasonLabel = QLineEdit()
        self.cancellationReasonLabel.setFixedSize(382,280)
        self.cancellationReasonLabel.setStyleSheet("background: white; border-radius: 10px;")
        self.cancellationReasonLabel.setPlaceholderText("Enter your cancellation reason here")
        self.cancellationReasonLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.layout.addWidget(self.cancellationReasonLabel)

        confirmationButtonLayout = QHBoxLayout()

        cancelButton = QPushButton()
        cancelButton.setText("Cancel")
        cancelButton.setFont(font)
        cancelButton.setFixedSize(150,50)
        cancelButton.clicked.connect(lambda checked: self.requestCancellationDialog.close())
        cancelButton.setStyleSheet("""QPushButton {
                                                        background: white;
                                                        border-radius: 10px;
                                                        text-align: center; 

                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #E8E8E8;
                                                          text-align: center; 
                                                        }""")
        confirmationButtonLayout.addWidget(cancelButton)

        confirmationButton = QPushButton()
        confirmationButton.setText("Confirm")
        confirmationButton.setFont(font)
        confirmationButton.setFixedSize(150,50)
        confirmationButton.clicked.connect(lambda checked: self.completeButtonConfirmationFunction(self.cancellationReasonLabel.text()))
        confirmationButton.setStyleSheet("""QPushButton {
                                            background: white;
                                            border-radius: 10px;
                                            text-align: center; 

                                            }
                                            QPushButton:hover
                                            {
                                              background-color: #E8E8E8;
                                              text-align: center; 
                                            }""")
        confirmationButtonLayout.addWidget(confirmationButton)

        self.layout.addLayout(confirmationButtonLayout)
        self.requestCancellationDialog.setLayout(self.layout)
        self.requestCancellationDialog.exec_()

    # this methodi s triggered when the confirmation button in the QDialog is clicked
    def completeButtonConfirmationFunction(self, reason):
        requestJSON = {
            'requestsType' : 'Cancellation',
            'clientID' : self.patient.getPatientID(),
            'requestReason' : reason,
            'appointmentID' : self.appointment.getAppointmentID()

        }

        request = requests.post('http://127.0.0.1:5000/requests',json=requestJSON)
        print(request.text)
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.cancelAppoitmentButtonUpdate()

        self.requestCancellationDialog.close()
        self.frameLayoutManager.back()
        self.frameLayout.widget(self.frameLayoutManager.top()).generateAppointmentButtons()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this method is triggered when the back button is clicked
    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this methodis triggered when the view prescription button is clicked
    def viewPrescription(self):
        
        self.patientPrescriptionDetails = PatientPrescriptionDetailsWindow(self.prescription,self.patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientPrescriptionDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this method is triggered when the complete appointment button is clicked
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
            self.frameLayout.widget(self.frameLayoutManager.top()).generateAppointmentButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this method is triggered to set the mode this page is going to be in
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
        self.prescription = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByAppointment(self.appointment.getAppointmentID())   
        print("Prescription here", self.prescription)
        if len(self.prescription) == 0:
            self.viewPrescriptionButton.hide()
            self.viewPrescriptionLabel.hide()

        self.cancelAppoitmentButtonUpdate()

    # this method checks for existing request in this appointment and hides the request cancellation appointment accordingly
    def cancelAppoitmentButtonUpdate(self):
        if Request.existingAppointments(self.appointment.getAppointmentID()):
            self.cancelAppointmentButton.hide()
            self.cancelAppointmentLabel.hide()

    # this method will hide request cancellation button if the appointment is near 2 hours
    def cancelAppointmentShow(self):
        appointmentStartTime = self.appointment.getStartTime().split(":")

        print(appointmentStartTime)
        currentTime = QTime.currentTime()
        startTime = QTime(int(appointmentStartTime[0]), int(appointmentStartTime[1]))

        timeDiff = currentTime.secsTo(startTime)

        if timeDiff < 7200 and timeDiff > 0:
            self.cancelAppointmentButton.hide()
            self.cancelAppointmentLabel.hide()