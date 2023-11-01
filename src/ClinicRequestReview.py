import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QStackedWidget
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .ClinicCancellationDetails import ClinicCancellationDetails
from .ClinicRequestDetails import ClinicRequestDetails
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .PageManager import PageManager, FrameLayoutManager


class ClinicRequestReview(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()
        self.state = "Request Review"

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setGeometry(QRect(200, 200, 1000, 500))

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Request Review")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.appointmentCancellationButton = QPushButton(self.centralwidget)
        self.appointmentCancellationButton.setGeometry(QRect(200, 120, 200, 40))
        self.appointmentCancellationButton.setText("Cancellation Request")
        self.appointmentCancellationButton.clicked.connect(self.appointmentCancellationFunction)

        self.requestReviewButton = QPushButton(self.centralwidget)
        self.requestReviewButton.setGeometry(QRect(600, 120, 200, 40))
        self.requestReviewButton.setText("Request Review")
        self.requestReviewButton.clicked.connect(self.requestReviewFunction)

        self.buttonContainer = QWidget()
        self.buttonContainer.setContentsMargins(20, 20, 20, 20)
        buttonLayout = QVBoxLayout(self.buttonContainer)
        self.boxScrollArea = QScrollArea()
        self.boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.boxScrollArea.setWidgetResizable(True)

        self.appointmentCancellationButtonContainer = QWidget()
        self.appointmentCancellationButtonContainer.setContentsMargins(20, 20, 20, 20)
        appointmentCancellationButtonLayout = QVBoxLayout(self.appointmentCancellationButtonContainer)
        self.appointmentCancellationboxScrollArea = QScrollArea()
        self.appointmentCancellationboxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.appointmentCancellationboxScrollArea.setWidgetResizable(True)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())
        self.appointmentCancellationList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        self.generateRequestButtons()
        self.generateCancellationButtons()

        self.boxScrollArea.setWidget(self.buttonContainer)
        self.boxScrollArea.setFixedSize(1000, 500)
        self.appointmentCancellationboxScrollArea.setWidget(self.appointmentCancellationButtonContainer)
        self.appointmentCancellationboxScrollArea.setFixedSize(1000, 500)

        self.stackedWidget.addWidget(self.boxScrollArea) # index 0
        self.stackedWidget.addWidget(self.appointmentCancellationboxScrollArea)  # index 1

        stackedWidgetLayout = QVBoxLayout()
        stackedWidgetLayout.addWidget(self.stackedWidget, alignment=Qt.AlignCenter)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addLayout(stackedWidgetLayout)

        self.setLayout(mainLayout)

        self.stackedWidget.setCurrentIndex(0)

    def appointmentCancellationFunction(self):
        if self.state == "Request Cancellation":
            pass
        else:
            self.state = "Request Cancellation"
            print(self.state)
            self.stackedWidget.setCurrentIndex(1)

    def requestReviewFunction(self):
        if self.state == "Request Review":
            pass
        else:
            self.state = "Request Review"
            print(self.state)
            self.stackedWidget.setCurrentIndex(0)

    def requestButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicRequestDetails = ClinicRequestDetails(request, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicRequestDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateRequestButtons(self):

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.unassignedAppointmentList.clear()

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        for count, request in enumerate(self.unassignedAppointmentList):
            print("generate request", count)
            self.requestButton = QPushButton()
            self.requestButton.setText(request.getAppointmentID() + " - " + request.getAppointmentStatus())
            self.requestButton.setFont(buttonFont)
            self.requestButton.setFixedSize(QSize(900, 150))
            self.requestButton.clicked.connect(
                lambda checked, request=request: self.requestButtonFunction(request, self.clinic))
            self.buttonContainer.layout().addWidget(self.requestButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

    def cancellationButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicCancellationDetails = ClinicCancellationDetails(request, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicCancellationDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateCancellationButtons(self):

        for i in range(self.appointmentCancellationButtonContainer.layout().count()):
            widget = self.appointmentCancellationButtonContainer.layout().itemAt(0).widget()
            self.appointmentCancellationButtonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.appointmentCancellationList.clear()

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        # update this
        self.appointmentCancellationList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        for count, request in enumerate(self.appointmentCancellationList):
            self.cancellationButton = QPushButton()
            self.cancellationButton.setText(request.getPatientID() + " - " + request.getStartTime())
            self.cancellationButton.setFont(buttonFont)
            self.cancellationButton.setFixedSize(QSize(900, 150))
            self.cancellationButton.clicked.connect(
                lambda checked, request=request: self.cancellationButtonFunction(request, self.clinic))
            self.appointmentCancellationButtonContainer.layout().addWidget(self.cancellationButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.appointmentCancellationButtonContainer.layout().addWidget(spacer)



