import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PatientAppointmentDetails import PatientAppointmentDetailsWindow 
from .PageManager import PageManager


class PatientMyAppointmentWindow(QMainWindow):
    def __init__(self, patient):
        super().__init__()
        self.setWindowTitle("My Appointment")
        self.patient = patient
        self.pageManager = PageManager()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PatientMyAppointment")
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
        self.headerTitle.setText("My Appointment")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.patientMyAccountButton = QPushButton(self.centralwidget)
        self.patientMyAccountButton.setFixedSize(70,70)
        self.patientMyAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.patientMyAccountIcon = QIcon(filepath)
        self.patientMyAccountButton.setIconSize(QSize(70, 70))
        self.patientMyAccountButton.setIcon(self.patientMyAccountIcon)

        # Push Button 5 (Log Out)
        self.patientBackButton = QPushButton(self.centralwidget)
        self.patientBackButton.setFixedSize(70, 70)
        self.patientBackButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.patientBackIcon = QIcon(filepath)
        self.patientBackButton.setIconSize(QSize(70, 70))
        self.patientBackButton.setIcon(self.patientBackIcon)
        self.patientBackButton.clicked.connect(self.backButtonFunction)

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
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(20)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def appointmentButtonFunction(self, appointment, patient):
        # Need to update the  page where it goes here according to button click
        self.patientAppointmentDetailsWindow = PatientAppointmentDetailsWindow(appointment, patient)
        self.patientAppointmentDetailsWindow.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.patientAppointmentDetailsWindow)
        print(self.pageManager.size())

    def backButtonFunction(self):
        self.pageManager.goBack()

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
