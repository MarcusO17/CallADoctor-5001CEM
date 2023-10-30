import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .ClinicRequestDetails import ClinicRequestDetails
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .PageManager import PageManager


class ClinicRequestReview(QMainWindow):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.pageManager = PageManager()
        self.setWindowTitle("Prescription (Patient)")
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
        self.headerTitle.setText("Request Review")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setFixedSize(70, 70)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.MyAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.MyAccountIcon)
        self.myAccountButton.clicked.connect(self.goToAccountPage)

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
        self.buttonContainer.setContentsMargins(20, 20, 20, 20)
        button_layout = QVBoxLayout(self.buttonContainer)
        boxScrollArea = QScrollArea()
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setWidgetResizable(True)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        self.generateRequestButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000, 500)
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

    def requestButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicRequestDetails = ClinicRequestDetails(request, clinic)
        self.pageManager.add(self.clinicRequestDetails)

    def backButtonFunction(self):
        self.pageManager.goBack()

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

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Clinic", self.clinic)
        self.pageManager.add(self.accountPage)


