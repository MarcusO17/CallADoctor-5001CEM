import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Patient
from .model import Appointment
from .model import Doctor
from .model import Prescription
from .model import PrescriptionDetails
from .PageManager import PageManager
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow


class DocPatientDetailsWindow(QMainWindow):

    def __init__(self, patientTemp, appointmentTemp, doctorTemp):
        super().__init__()
        self.pageManager = PageManager()
        #set the information here
        self.patient = patientTemp
        self.appointment = appointmentTemp
        self.doctor = doctorTemp
        print(self.doctor.getDoctorName(), self.doctor.getDoctorType(), self.doctor.getDoctorContact(), self.doctor.getYearsOfExperience())
        print(self.appointment.getPatientID(), self.appointment.getDoctorID(), self.appointment.getStartTime(), self.appointment.getEndTime(), self.appointment.getAppointmentDate(), self.appointment.getVisitReason())
        print(self.patient.getPatientName(), self.patient.getPatientDOB(), self.patient.getPatientAddress, self.patient.getPatientBlood, self.patient.getPatientBlood())
        self.setWindowTitle("Patient Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("patient_details")
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
        self.headerTitle.setText(self.patient.getPatientName())
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

        self.patientAppointmentDetailLabel = QLabel(self.centralwidget)
        self.patientAppointmentDetailLabel.setGeometry(QRect(180, 220, 400, 200))
        self.patientAppointmentDetailLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patientAppointmentDetailLabel.setFont(font)
        self.patientAppointmentDetailLabel.setText(str(self.appointment.getVisitReason()) + " " + str(self.appointment.getStartTime()) + " " + str(self.appointment.getEndTime()) + " " + str(self.appointment.getAppointmentDate()) )
        self.patientAppointmentDetailLabel.setFrameShape(QtWidgets.QFrame.Box)
        

        self.patientDescriptionsLabel = QLabel(self.centralwidget)
        self.patientDescriptionsLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patientDescriptionsLabel.setFont(font)
        self.patientDescriptionsLabel.setText(str(self.patient.getPatientName()) + " " + str(self.patient.getPatientDOB()) + " " + str(self.patient.getPatientBlood()) + " " + str(self.patient.getPatientRace()))
        self.patientDescriptionsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.doctorDetailsLabel = QLabel(self.centralwidget)
        self.doctorDetailsLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.doctorDetailsLabel.setFont(font)
        self.doctorDetailsLabel.setText(str(self.doctor.getDoctorName()) + " " + str(self.doctor.getDoctorType()) + " " + str(self.doctor.getDoctorContact()) + " " + str(self.doctor.getYearsOfExperience()))
        self.doctorDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.viewPrescriptionButton = QPushButton(self.centralwidget)
        self.viewPrescriptionButton.setGeometry(QRect(710, 545, 180, 100))
        self.viewPrescriptionButton.setLayoutDirection(Qt.RightToLeft)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.viewPrescriptionButton.setFont(font)
        self.viewPrescriptionButton.setText("View Prescription")
        self.viewPrescriptionButton.setObjectName("ViewPrescription")
        self.viewPrescriptionButton.clicked.connect(self.viewPrescriptionFunction)

        self.viewPrescriptionLabel = QLabel(self.centralwidget)
        self.viewPrescriptionLabel.setGeometry(QRect(730, 570, 50, 50))
        self.viewPrescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.viewPrescriptionIcon = QPixmap(filepath)
        self.viewPrescriptionIcon = self.viewPrescriptionIcon.scaled(50, 50)
        self.viewPrescriptionLabel.setPixmap(self.viewPrescriptionIcon)


        self.patientDetailsContainer = QLabel(self.centralwidget)
        self.patientDetailsContainer.setFixedSize(1000,500)
        self.patientDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)

        #get precription data here by appointmentID



        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.patientDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.viewPrescriptionButton.raise_()

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def viewPrescriptionFunction(self):
        prescriptionDetails1 = PrescriptionDetails ("ABC med", 4, "After", "150ML")
        prescriptionDetails2 = PrescriptionDetails ("BCA med", 3, "Before", "50ML")
        prescriptionDetails3 = PrescriptionDetails ("CDS med", 2, "After", "10ML")


        prescription1 = Prescription ("p101", "ap101", "13-04-2023")
        prescription1.setPrescriptionDetails(prescriptionDetails1)
        prescription1.setPrescriptionDetails(prescriptionDetails2)
        prescription1.setPrescriptionDetails(prescriptionDetails3)

        self.patientPrescription = PatientPrescriptionDetailsWindow(self.patient, prescription1)
        self.pageManager.add(self.patientPrescription)
        print(self.pageManager.size())



    def backButtonFunction(self):
        self.pageManager.goBack()