import os

from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout,QSizePolicy

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .PatientAppointmentDetails import PatientAppointmentDetailsWindow
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .model import Appointment, AppointmentRepo, Patient, PrescriptionRepo
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager


class PatientDashboard(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient
        self.setupUi()

    def setupUi(self):

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()

        self.generateWelcomeText()

        self.generateUpcomingAppointments()

        self.generateMapWidget()

        self.generatePrescription()

        self.leftLayout.addWidget(self.welcomeTextWidget, 3)
        spacer = QWidget()
        spacer.setFixedHeight(30)
        self.leftLayout.addWidget(spacer)
        self.leftLayout.addWidget(self.mapWidget, 7)

        self.dateLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(230)
        self.dateLayout.addWidget(spacer)
        self.dateWidget = QLabel(f"Date: {QDate.currentDate().toString('dd-MM-yyyy')}")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.dateWidget.setFont(font)
        self.dateWidget.setFixedSize(220,75)
        self.dateWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.dateWidget.setContentsMargins(10, 10, 10, 10)

        self.dateLayout.addWidget(self.dateWidget)

        self.rightLayout.addLayout(self.dateLayout)

        spacer = QWidget()
        spacer.setFixedHeight(50)
        self.rightLayout.addWidget(spacer)
        self.upcomingAppointmentWidget.setFixedWidth(500)
        self.rightLayout.addWidget(self.upcomingAppointmentWidget, 5)
        self.rightLayout.addWidget(self.prescriptionWidget, 5)

        self.mainLayout.addLayout(self.leftLayout, 7)
        self.mainLayout.addLayout(self.rightLayout, 5)


        self.setLayout(self.mainLayout)

    def generatePrescription(self):
        self.prescriptionWidget = QWidget()
        self.prescriptionWidget.setStyleSheet(
            "background-color: #BCCAE0; border-radius: 10px; margin-left: 20px;")
        self.prescriptionLayout = QVBoxLayout(self.prescriptionWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.prescriptionTitle = QLabel()
        self.prescriptionTitle.setFixedWidth(200)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.prescriptionTitle.setFont(font)
        self.prescriptionTitle.setText("Prescription")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.prescriptionTitle)

        self.prescriptionLayout.addLayout(headerRow)
        self.prescriptionLayout.setContentsMargins(20, 20, 20, 20)

        # get 3 upcoming appointment here

        prescriptionList = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByPatient(self.patient.getPatientID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\medical-prescription.png")
        self.prescriptionButtonIcon = QIcon(filepath)

        for count, prescription in enumerate(prescriptionList):
            self.prescriptionButton = QPushButton()
            self.prescriptionButton.setText(f"{prescription.getPrescriptionID()}")
            self.prescriptionButton.setStyleSheet("background-color: white; border-radius: 10px;")
            self.prescriptionButton.setFont(buttonFont)
            self.prescriptionButton.setFixedSize(QSize(400,100))
            self.prescriptionButton.setIconSize(QSize(70, 70))
            self.prescriptionButton.setIcon(self.prescriptionButtonIcon)
            self.prescriptionButton.clicked.connect(
                lambda checked, prescription=prescription: self.prescriptionButtonFunction(prescription, self.patient))
            self.prescriptionLayout.addWidget(self.prescriptionButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.prescriptionLayout.addWidget(spacer)

    def prescriptionButtonFunction(self, prescription, patient):
        self.prescriptionDetails = PatientPrescriptionDetailsWindow(prescription, patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.prescriptionDetails)
        self.frameLayoutManager.add(self.frameLayout.count()-1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def generateWelcomeText(self):

        self.welcomeTextWidget = QWidget()
        self.welcomeTextWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.welcomeTextLayout = QVBoxLayout(self.welcomeTextWidget)

        welcomeTextLabel = QLabel()
        welcomeTextLabel.setText(f"Welcome {self.patient.getPatientName()}!")
        welcomeTextLabel.setStyleSheet("padding-left: 30px")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        welcomeTextLabel.setFont(font)

        self.welcomeTextLayout.addWidget(welcomeTextLabel)


    def generateUpcomingAppointments(self):

        self.upcomingAppointmentWidget = QWidget()
        self.upcomingAppointmentWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px; margin-left: 20px;")
        self.upcomingAppointmentLayout = QVBoxLayout(self.upcomingAppointmentWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.upcomingAppointmentTitle = QLabel()
        self.upcomingAppointmentTitle.setFixedWidth(420)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.upcomingAppointmentTitle.setFont(font)
        self.upcomingAppointmentTitle.setText("Upcoming Appointment")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.upcomingAppointmentTitle)

        self.upcomingAppointmentLayout.addLayout(headerRow)
        self.upcomingAppointmentLayout.setContentsMargins(20, 20, 20, 20)

        #get 3 upcoming appointment here

        appointmentList = list()

        appointment1 = Appointment("A0001", "D00001", "C0001", "P0001", "Approved", "8:00", "9:00", "appointmentDate",
                                   "visitReason")

        appointmentList.append(appointment1)

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\appointment.png")
        self.appointmentButtonIcon = QIcon(filepath)

        for count, appointment in enumerate(appointmentList):
            self.appointmentButton = QPushButton()
            self.appointmentButton.setText(f"{appointment.getAppointmentID()} - {appointment.getStartTime()}")
            self.appointmentButton.setStyleSheet("background-color: white; border-radius: 10px; margin-left: 30px;")
            self.appointmentButton.setFont(buttonFont)
            self.appointmentButton.setFixedSize(QSize(400,100))
            self.appointmentButton.setIconSize(QSize(70, 70))
            self.appointmentButton.setIcon(self.appointmentButtonIcon)
            self.appointmentButton.clicked.connect(
                lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.patient))
            self.upcomingAppointmentLayout.addWidget(self.appointmentButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.upcomingAppointmentLayout.addWidget(spacer)

    def appointmentButtonFunction(self, appointment, patient):
        self.patientAppointmentDetails = PatientAppointmentDetailsWindow(appointment, patient)
        self.patientAppointmentDetails.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientAppointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count()-1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateMapWidget(self):

        self.mapWidget = QWidget()
        self.mapWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        self.widgetTitle = QLabel()
        self.widgetTitle.setFixedWidth(380)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.widgetTitle.setFont(font)
        self.widgetTitle.setText("Map")

        headerRow = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(200)
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.widgetTitle)

        self.mapWidgetLayout.addLayout(headerRow)
        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)

    def patientButtonFunction(self, patient, doctor):
        # update the clinic details page here according to button click

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.patientHistoryWindow = DoctorPatientHistoryWindow(patient, doctor)
        self.frameLayout.addWidget(self.patientHistoryWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())