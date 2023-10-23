import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model import Patient
from .DocPatientDetails import DocPatientDetailsWindow 
from .PageManager import PageManager


class DocPatientHistoryWindow(QMainWindow):
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
        self.headerTitle.setText("Welcome! [name]")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.patientHistoryMyAccountButton = QPushButton(self.centralwidget)
        self.patientHistoryMyAccountButton.setFixedSize(70,70)
        self.patientHistoryMyAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.patientHistoryMyAccountIcon = QIcon(filepath)
        self.patientHistoryMyAccountButton.setIconSize(QSize(70, 70))
        self.patientHistoryMyAccountButton.setIcon(self.patientHistoryMyAccountIcon)

        # Push Button 5 (Log Out)
        self.patientHistoryBackButton = QPushButton(self.centralwidget)
        self.patientHistoryBackButton.setFixedSize(70, 70)
        self.patientHistoryBackButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.patientHistoryBackIcon = QIcon(filepath)
        self.patientHistoryBackButton.setIconSize(QSize(70, 70))
        self.patientHistoryBackButton.setIcon(self.patientHistoryBackIcon)
        self.patientHistoryBackButton.clicked.connect(self.backButtonFunction)

        buttonContainer = QVBoxLayout()
        buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        appointmentList = list()


        appointment1 = Appointment("ap0001", "Doc101", "P1001", "Completed", "Starts 10am", "Ends 5pm", "4th Novemeber", "Fever")
        appointment2 = Appointment("ap0002", "Doc102", "P1002", "In-Progress", "Starts 12am", "Starts 4pm", "30th Novemeber", "Cold")
        appointment3 = Appointment("ap0003", "Doc103", "P1003", "Completed", "Starts 9am", "Starts 6pm", "21st Novemeber", "Pain")

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
            self.patientAppointmentButton.setText(appointment.getPatientID() + " - " + appointment.getDoctorID())
            self.patientAppointmentButton.setFont(buttonFont)
            self.patientAppointmentButton.setFixedSize(QSize(950,150))
            self.patientAppointmentButton.clicked.connect(lambda checked, appointment=appointment: self.appointmentButtonFunction(self.patient,appointment,self.doctor))
            buttonContainer.addWidget(self.patientAppointmentButton)

        boxScrollArea.setLayout(buttonContainer)
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

    def appointmentButtonFunction(self, patient, appointment, doctor):
        # Need to update the  page where it goes here according to button click
        self.patientHistoryAppointmentDetailsWindow = DocPatientDetailsWindow(patient,appointment,doctor)
        self.pageManager.add(self.patientHistoryAppointmentDetailsWindow)
        print(self.pageManager.size())

    def backButtonFunction(self):
        self.pageManager.goBack()

# def runthiswindow():
#     app = QApplication(sys.argv)
#     patientMyAppointmentWindow = PatientMyAppointmentWindow()
#     patientMyAppointmentWindow.show()
#     sys.exit(app.exec_())

# runthiswindow()
