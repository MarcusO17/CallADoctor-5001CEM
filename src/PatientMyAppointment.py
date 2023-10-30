import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PatientAppointmentDetails import PatientAppointmentDetailsWindow 
from .PageManager import PageManager, FrameLayoutManager


class PatientMyAppointmentWindow(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.setWindowTitle("My Appointment")
        self.patient = patient
        self.pageManager = PageManager()
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")

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
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.appointmentList = list()

        self.generateAppointmentButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def appointmentButtonFunction(self, appointment, patient):
        # Need to update the  page where it goes here according to button click
        self.patientAppointmentDetailsWindow = PatientAppointmentDetailsWindow(appointment, patient)
        self.patientAppointmentDetailsWindow.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientAppointmentDetailsWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateAppointmentButtons(self):

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.appointmentList.clear()

        #query appointment here
        self.appointmentList = AppointmentRepository.getAppointmentsByPatients(self.patient.getPatientID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, appointment in enumerate(self.appointmentList):
            self.patientAppointmentButton = QPushButton()
            self.patientAppointmentButton.setText(
                appointment.getAppointmentID() + " - " + appointment.getAppointmentStatus())
            self.patientAppointmentButton.setFont(buttonFont)
            self.patientAppointmentButton.setFixedSize(QSize(900, 150))
            self.patientAppointmentButton.clicked.connect(
                lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.patient))
            self.buttonContainer.layout().addWidget(self.patientAppointmentButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)
