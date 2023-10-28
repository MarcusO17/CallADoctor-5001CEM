import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Clinic, Doctor, Appointment, Patient, AppointmentRepo
from .PageManager import PageManager


class DoctorMyAppointmentWindow(QWidget):
    def __init__(self, doctor):

        super().__init__()
        self.doctor = doctor
        self.pageManager = PageManager()
        self.setWindowTitle("My Appointment")
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        mainLayout = QVBoxLayout()

        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("My Appointment")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.buttonContainer = QWidget()
        buttonLayout = QVBoxLayout(self.buttonContainer)
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setWidgetResizable(True)

        self.appointmentList = list()

        self.generateMyAppointmentButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        boxScrollArea.setStyleSheet("margin-left: 100px; margin top: 20px")

        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def appointmentButtonFunction(self, appointment, doctor):
        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.doctorAppointmentDetails)
        print(self.pageManager.size())

    def generateMyAppointmentButtons(self):

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.appointmentList.clear()

        self.appointmentList = AppointmentRepo.AppointmentRepository.getAppointmentsByDoctor(self.doctor.getDoctorID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, appointment in enumerate(self.appointmentList):
            self.appointmentButton = QPushButton()
            self.appointmentButton.setText(f"{appointment.getAppointmentID()} - {appointment.getAppointmentStatus()}")
            self.appointmentButton.setFont(buttonFont)
            self.appointmentButton.setFixedSize(QSize(800, 150))
            self.appointmentButton.clicked.connect(
                lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.doctor))
            self.buttonContainer.layout().addWidget(self.appointmentButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)


