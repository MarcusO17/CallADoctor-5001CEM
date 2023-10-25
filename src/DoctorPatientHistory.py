import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets

from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model import Patient
from .PageManager import PageManager


class DoctorPatientHistoryWindow(QMainWindow):
    def __init__(self, patient, doctor):
        super().__init__()
        self.patient = patient
        self.doctor = doctor
        self.setWindowTitle("My Appointment (Patient)")
        self.pageManager = PageManager()
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
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Appointment History")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setFixedSize(70,70)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
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

        appointmentList = list()

        appointment1 = Appointment("ap0001", "Doc101","clinicID", "P1001", "Completed", "10:00", "11:00", "2023-10-29", "Fever")
        appointment2 = Appointment("ap0002", "Doc102", "clinicID","P1002", "Approved", "12:00", "13:00", "2023-10-29", "Cold")
        appointment3 = Appointment("ap0003", "Doc103", "clinicID","P1003", "Completed", "9:00", "10:00", "2023-10-29", "Pain")

        appointmentList.append(appointment1)
        appointmentList.append(appointment2)
        appointmentList.append(appointment3)
        print("appointment list size" , len(appointmentList))

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
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def appointmentButtonFunction(self, appointment, doctor):

        self.appointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.appointmentDetails.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.appointmentDetails)

    def backButtonFunction(self):
        self.pageManager.goBack()
