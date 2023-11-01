import os

from PyQt5.QtCore import QSize, QDate, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
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
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()

        self.generateDoctorWidgets()

        self.generateRequestReview()

        self.generateGraphWidget()

        self.leftLayout.addWidget(self.doctorWidgets, 3)
        spacer = QWidget()
        spacer.setFixedHeight(25)
        self.leftLayout.addWidget(spacer)
        self.leftLayout.addWidget(self.graphWidget, 7)

        self.dateLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(230)
        self.dateLayout.addWidget(spacer)
        self.dateWidget = QLabel(f"Date: {QDate.currentDate().toString('dd-MM-yyyy')}")
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.dateWidget.setFont(font)
        self.dateWidget.setFixedSize(220,75)
        self.dateWidget.setStyleSheet("background-color: transparent;")
        self.dateWidget.setContentsMargins(10, 10, 10, 10)

        self.dateLayout.addWidget(self.dateWidget)

        self.rightLayout.addLayout(self.dateLayout)

        spacer = QWidget()
        self.requestReviewWidget.setFixedWidth(500)
        self.rightLayout.addWidget(self.requestReviewWidget)

        self.mainLayout.addLayout(self.leftLayout, 7)
        self.mainLayout.addLayout(self.rightLayout, 5)

        self.setLayout(self.mainLayout)

    def generateDoctorWidgets(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.doctorWidgets = QWidget()
        doctorWidgetsLayout = QVBoxLayout(self.doctorWidgets)

        doctorWidgetsRow = QHBoxLayout()

        self.doctorTitle = QLabel()
        self.doctorTitle.setFixedWidth(200)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setWeight(75)
        self.doctorTitle.setFont(font)
        self.doctorTitle.setText("Doctors")
        self.doctorTitle.setStyleSheet("QLabel {margin-left: 50px; color: #022b3a;}")
        headerRow = QHBoxLayout()
        headerRow.setAlignment(Qt.AlignLeft)
        headerRow.addWidget(self.doctorTitle)

        doctorWidgetsLayout.addLayout(headerRow)


        self.doctorList = DoctorRepository.getDoctorListClinic(self.clinic.getClinicID())

        threeDoctorList = self.doctorList[:3]

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(28)
        buttonFont.setWeight(75)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\doctor.png")
        doctorIcon = QIcon(filepath)

        for count, doctor in enumerate(threeDoctorList):
            doctorButton = QPushButton()
            doctorButton.setFixedSize(QSize(100, 100))
            doctorButton.setIconSize(QSize(35, 35))
            doctorButton.setIcon(doctorIcon)
            doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))

            font = QFont()
            font.setFamily("Montserrat")
            font.setPointSize(12)
            font.setWeight(75)

            doctorLabel = QLabel()
            doctorLabel.setFont(font)
            doctorNameSliced = doctor.getDoctorName()[:8]
            doctorLabel.setText(f"{doctorNameSliced}..")

            doctorLabel.adjustSize()

            doctorWidget = QWidget()
            doctorWidget.setFixedSize(125, 125)
            doctorWidget.setStyleSheet("background-color: #ffffff; border-radius: 5px; box-shadow: 5px 10px;")
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
        self.requestReviewWidget.setStyleSheet("background-color: transparent;")
        self.requestReviewLayout = QVBoxLayout(self.requestReviewWidget)
        self.requestReviewLayout.setSpacing(20)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.requestReviewTitle = QLabel()
        self.requestReviewTitle.setFixedWidth(300)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setWeight(75)
        self.requestReviewTitle.setFont(font)
        self.requestReviewTitle.setText("Request Review")
        self.requestReviewTitle.setStyleSheet("QLabel {color: #022b3a}")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.requestReviewTitle)

        self.requestReviewLayout.addLayout(headerRow)
        self.requestReviewLayout.setContentsMargins(20, 20, 20, 20)

        #get 3 reviews here
        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)
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
                self.requestButton.setStyleSheet("background-color: white; margin-left: 30px; border-radius: 5px;")
                self.requestButton.setFont(buttonFont)
                self.requestButton.setFixedSize(QSize(430, 100))
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

    def generateGraphWidget(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        self.graphWidget = QWidget()
        self.graphWidget.setStyleSheet("background-color: transparent;")
        self.graphWidgetLayout = QVBoxLayout(self.graphWidget)

        self.widgetTitle = QLabel()
        self.widgetTitle.setFixedWidth(380)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setWeight(75)
        self.widgetTitle.setFont(font)
        self.widgetTitle.setText("ANALYTIC STUFF")
        self.widgetTitle.setStyleSheet("QLabel {color: #022b3a}")

        headerRow = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(200)
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.widgetTitle)

        self.graphWidgetLayout.addLayout(headerRow)
        self.graphWidgetLayout.setContentsMargins(20, 20, 20, 20)

        #generate your graph here

        self.graphLabel = QLabel()
        self.graphLabel.setFixedSize(600,400)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        graphPixmap = QPixmap(filepath)
        self.graphLabel.setPixmap(graphPixmap)

        self.graphWidgetLayout.addWidget(self.graphLabel)