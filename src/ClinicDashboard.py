import os

from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout,QSizePolicy

from .AccountPage import AccountPage
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .ClinicRequestDetails import ClinicRequestDetails
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .model import Appointment, AppointmentRepo, Patient
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager
from .model.DoctorRepo import DoctorRepository


class ClinicDashboard(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()

        self.generateDoctorWidgets()

        self.generateRequestReview()

        self.generateMapWidget()

        self.leftLayout.addWidget(self.doctorWidgets, 3)
        spacer = QWidget()
        spacer.setFixedHeight(25)
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
        self.requestReviewWidget.setFixedWidth(500)
        self.rightLayout.addWidget(self.requestReviewWidget)

        self.mainLayout.addLayout(self.leftLayout, 7)
        self.mainLayout.addLayout(self.rightLayout, 5)

        self.setLayout(self.mainLayout)

    def generateDoctorWidgets(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.doctorWidgets = QWidget()
        self.doctorWidgets.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        doctorWidgetsLayout = QVBoxLayout(self.doctorWidgets)

        doctorWidgetsRow = QHBoxLayout()

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.doctorTitle = QLabel()
        self.doctorTitle.setFixedWidth(150)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.doctorTitle.setFont(font)
        self.doctorTitle.setText("Doctors")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.doctorTitle)

        doctorWidgetsLayout.addLayout(headerRow)


        self.doctorList = DoctorRepository.getDoctorListClinic(self.clinic.getClinicID())

        threeDoctorList = self.doctorList[:3]

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\doctor.png")
        doctorIcon = QIcon(filepath)

        for count, doctor in enumerate(threeDoctorList):
            doctorButton = QPushButton()
            doctorButton.setFixedSize(QSize(100, 100))
            doctorButton.setIconSize(QSize(70, 70))
            doctorButton.setIcon(doctorIcon)
            doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))

            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)

            doctorLabel = QLabel()
            doctorLabel.setFixedSize(125, 25)
            doctorLabel.setFont(font)
            doctorLabel.setText(f"{doctor.getDoctorName()}")

            doctorWidget = QWidget()
            doctorWidget.setFixedSize(125, 125)
            doctorWidget.setStyleSheet("background-color: white; border-radius: 10px;")
            doctorLayout = QVBoxLayout(doctorWidget)
            doctorLayout.addWidget(doctorButton)
            doctorLayout.addWidget(doctorLabel)

            doctorWidgetsRow.addWidget(doctorWidget)

        doctorWidgetsLayout.addLayout(doctorWidgetsRow)

    def doctorButtonFunction(self, doctor, clinic):
        self.doctorSchedule = ClinicDetailedSchedule(doctor, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorSchedule)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def generateRequestReview(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.requestReviewWidget = QWidget()
        self.requestReviewWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px; margin-left: 20px;")
        self.requestReviewLayout = QVBoxLayout(self.requestReviewWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.requestReviewTitle = QLabel()
        self.requestReviewTitle.setFixedWidth(300)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.requestReviewTitle.setFont(font)
        self.requestReviewTitle.setText("Request Review")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.requestReviewTitle)

        self.requestReviewLayout.addLayout(headerRow)
        self.requestReviewLayout.setContentsMargins(20, 20, 20, 20)

        #get 3 reviews here
        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        threeAppointments = self.unassignedAppointmentList[:3]

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\request.png")

        requestIcon = QIcon(filepath)

        if len(threeAppointments) == 0:
            emptyReviews = QLabel()
            emptyReviews.setFont(buttonFont)
            emptyReviews.setText("Empty Reviews")
            emptyReviews.setStyleSheet("margin-left: 50px")
            self.requestReviewLayout.addWidget(emptyReviews)
        else:
            for count, request in enumerate(threeAppointments):
                self.requestButton = QPushButton()
                self.requestButton.setText(request.getAppointmentID() + " - " + request.getAppointmentStatus())
                self.requestButton.setStyleSheet("background-color: white; border-radius: 10px; margin-left: 30px;")
                self.requestButton.setFont(buttonFont)
                self.requestButton.setFixedSize(QSize(400, 100))
                self.requestButton.setIcon(requestIcon)
                self.requestButton.setIconSize(QSize(70, 70))
                self.requestButton.clicked.connect(
                    lambda checked, request=request: self.requestButtonFunction(request, self.clinic))
                self.requestReviewLayout.addWidget(self.requestButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.requestReviewLayout.addWidget(spacer)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\appointment.png")
        self.appointmentButtonIcon = QIcon(filepath)

    def requestButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicRequestDetails = ClinicRequestDetails(request, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicRequestDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
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