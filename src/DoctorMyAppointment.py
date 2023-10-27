import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model import Patient
from .PageManager import PageManager


class DoctorMyAppointmentWindow(QMainWindow):
    def __init__(self, doctor):

        super().__init__()
        self.doctor = doctor
        self.setWindowTitle("My Appointment")
        self.pageManager = PageManager()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DocMyAppointment")
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
        self.headerTitle.setText("Welcome! [name]")
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
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backButtonIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backButtonIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        buttonContainer = QWidget()
        buttonLayout = QVBoxLayout(buttonContainer)
        buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setWidgetResizable(True)

        appointmentList = list()

        appointment1 = Appointment("ap0001", "Doc101", "clinic1", "P1001", "Completed", "Starts 10am", "Ends 5pm",
                                   "4th Novemeber", "Fever")
        appointment2 = Appointment("ap0002", "Doc102", "clinic1", "P1002", "Approved", "Starts 12am", "Starts 4pm",
                                   "30th Novemeber", "Cold")
        appointment3 = Appointment("ap0003", "Doc103", "clinic1", "P1003", "Completed", "Starts 9am", "Starts 6pm",
                                   "21st Novemeber", "Pain")

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
            self.appointmentButton = QPushButton()
            self.appointmentButton.setText(f"{appointment.getAppointmentID()} - {appointment.getAppointmentStatus()}")
            self.appointmentButton.setFont(buttonFont)
            self.appointmentButton.setFixedSize(QSize(900,150))
            self.appointmentButton.clicked.connect(lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.doctor))
            buttonContainer.layout().addWidget(self.appointmentButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        buttonContainer.layout().addWidget(spacer)

        boxScrollArea.setWidget(buttonContainer)
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

    def appointmentButtonFunction(self, appointment, doctor):
        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.doctorAppointmentDetails)
        print(self.pageManager.size())
    def backButtonFunction(self):
        self.pageManager.goBack()

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Doctor", self.doctor)
        self.pageManager.add(self.accountPage)

