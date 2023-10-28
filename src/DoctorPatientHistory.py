import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model import Patient
from .model import AppointmentRepo
from .PageManager import PageManager, FrameLayoutManager


class DoctorPatientHistoryWindow(QWidget):
    def __init__(self, patient, doctor):
        super().__init__()
        self.patient = patient
        self.doctor = doctor
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
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
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Appointment History")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backButtonIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backButtonIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.buttonContainer = QWidget()
        buttonLayout = QVBoxLayout(self.buttonContainer)
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        appointmentList = AppointmentRepo.AppointmentRepository.getAppointmentsByPatients(self.patient.getPatientID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, appointment in enumerate(appointmentList):
            self.patientAppointmentButton = QPushButton()
            self.patientAppointmentButton.setText(f"{appointment.getAppointmentID()} -  {appointment.getAppointmentDate()}")
            self.patientAppointmentButton.setFont(buttonFont)
            self.patientAppointmentButton.setFixedSize(QSize(900,150))
            self.patientAppointmentButton.clicked.connect(lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment,self.doctor))
            self.buttonContainer.layout().addWidget(self.patientAppointmentButton)

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        boxScrollArea.setStyleSheet("margin-left: 100px; margin top: 20px")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def appointmentButtonFunction(self, appointment, doctor):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.appointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.appointmentDetails.setMode(appointment.getAppointmentStatus())

        self.frameLayout.addWidget(self.appointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
