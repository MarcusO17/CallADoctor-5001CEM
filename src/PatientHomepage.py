import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QMessageBox, QSizePolicy, \
    QHBoxLayout, QVBoxLayout, QStackedWidget
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .PatientDashboard import PatientDashboard
from .model import Patient
from .PatientClinicsNearbyWindow import PatientClinicsNearbyWindow
from .PageManager import PageManager, FrameLayoutManager
from .PatientPrescription import PatientPrescriptionWindow
from .PatientMyAppointment import PatientMyAppointmentWindow




class PatientHomepage(QMainWindow):
    def __init__(self, patientID):
        super().__init__()
        self.patient = Patient.getPatientfromID(patientID)
        self.pageManager = PageManager()
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayoutManager.add(0)
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.setupUi(self)

    def goToDashboard(self):
        self.setButtonHighlight(self.dashboardButton)
        self.frameLayoutManager.backToBasePage(0)
        self.frameLayout.setCurrentIndex(0)
    def goToClinicsNearby(self):
        self.setButtonHighlight(self.clinicNearbyButton)
        self.frameLayoutManager.backToBasePage(1)
        self.frameLayout.setCurrentIndex(1)

    def gotoMyPrescription(self):
        self.setButtonHighlight(self.myPrescriptionButton)
        self.frameLayoutManager.backToBasePage(3)
        self.frameLayout.setCurrentIndex(3)

    def gotoPatientMyAppointment(self):
        self.setButtonHighlight(self.myAppointmentButton)
        self.frameLayoutManager.backToBasePage(2)
        self.frameLayout.setCurrentIndex(2)

    def goToAccountPage(self):
        self.setButtonHighlight(self.myAccountButton)
        self.frameLayoutManager.backToBasePage(4)
        self.frameLayout.setCurrentIndex(4)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Homepage")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)

        self.dashboardButton = QPushButton()
        self.dashboardButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\dashboard.png")
        self.dashboardIcon = QIcon(filepath)
        self.dashboardButton.setIconSize(QSize(35, 35))
        self.dashboardButton.setIcon(self.dashboardIcon)
        self.dashboardButton.setStyleSheet("background-color: #3872E8; border-radius: 10px;")
        self.dashboardButton.clicked.connect(self.goToDashboard)

        self.clinicNearbyButton = QPushButton()
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\clinic.png")
        self.clinicNearbyIcon = QIcon(filepath)
        self.clinicNearbyButton.setFixedSize(70, 70)
        self.clinicNearbyButton.setIcon(self.clinicNearbyIcon)
        self.clinicNearbyButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.clinicNearbyButton.setIconSize(QSize(35, 35))
        self.clinicNearbyButton.clicked.connect(self.goToClinicsNearby)

        self.myPrescriptionButton = QPushButton()
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\medical-prescription.png")
        self.myPrescriptionIcon = QIcon(filepath)
        self.myPrescriptionButton.setFixedSize(70, 70)
        self.myPrescriptionButton.setIcon(self.myPrescriptionIcon)
        self.myPrescriptionButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.myPrescriptionButton.setIconSize(QSize(35, 35))
        self.myPrescriptionButton.clicked.connect(self.gotoMyPrescription)

        self.myAppointmentButton = QPushButton()
        self.myAppointmentButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\appointment.png")
        self.myAppointmentIcon = QIcon(filepath)
        self.myAppointmentButton.setIconSize(QSize(35, 35))
        self.myAppointmentButton.setIcon(self.myAppointmentIcon)
        self.myAppointmentButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.myAppointmentButton.clicked.connect(self.gotoPatientMyAppointment)

        self.topLeftLogo = QLabel()
        self.topLeftLogo.setGeometry(QRect(20, 10, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(70, 70)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.myAccountButton = QPushButton()
        self.myAccountButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\account.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(35, 35))
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setFixedSize(70, 70)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logout.png")
        self.logoutIcon = QIcon(filepath)
        self.logoutButton.setIconSize(QSize(35, 35))
        self.logoutButton.setIcon(self.logoutIcon)
        self.logoutButton.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")
        self.logoutButton.clicked.connect(self.logout)

        self.highlightButtonList = list()
        self.highlightButtonList.append(self.myAccountButton)
        self.highlightButtonList.append(self.myAppointmentButton)
        self.highlightButtonList.append(self.myPrescriptionButton)
        self.highlightButtonList.append(self.dashboardButton)
        self.highlightButtonList.append(self.clinicNearbyButton)

        self.mainLayout = QHBoxLayout()
        self.sideLayoutWidget = QWidget()
        self.sideLayoutWidget.setStyleSheet("background-color: #E6EBF5; border-radius: 10px;")
        self.sideLayout = QVBoxLayout(self.sideLayoutWidget)
        self.sideLayout.setContentsMargins(10, 10, 10, 10)

        self.sideLayout.addWidget(self.topLeftLogo)
        spacer1 = QWidget()
        spacer1.setFixedHeight(100)
        self.sideLayout.addWidget(spacer1)
        self.sideLayout.addWidget(self.dashboardButton)
        self.sideLayout.addWidget(self.clinicNearbyButton)
        self.sideLayout.addWidget(self.myAppointmentButton)
        self.sideLayout.addWidget(self.myPrescriptionButton)
        spacer2 = QWidget()
        spacer2.setFixedHeight(100)
        self.sideLayout.addWidget(spacer2)
        self.sideLayout.addWidget(self.myAccountButton)
        self.sideLayout.addWidget(self.logoutButton)
        bottomSpacer = QWidget()
        bottomSpacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sideLayout.addWidget(bottomSpacer)

        self.mainLayout.addWidget(self.sideLayoutWidget, 1)

        # THIS QSTACKEDWIDGET IS ONLY FOR QWIDGET SWITCHING
        self.frameLayout = QStackedWidget()
        # start and set all pages to the framelayout
        self.patientDashboard = PatientDashboard(self.patient)  # index 0
        self.patientClinicsNearby = PatientClinicsNearbyWindow(self.patient)  # index 1
        self.patientMyAppointment = PatientMyAppointmentWindow(self.patient)  # index 2
        self.patientPrescription = PatientPrescriptionWindow(self.patient)  # index 3
        self.accountPage = AccountPage()  # index 4
        self.accountPage.setUser("Patient", self.patient)

        self.frameLayout.addWidget(self.patientDashboard)
        self.frameLayout.addWidget(self.patientClinicsNearby)
        self.frameLayout.addWidget(self.patientMyAppointment)
        self.frameLayout.addWidget(self.patientPrescription)
        self.frameLayout.addWidget(self.accountPage)

        self.frameLayoutManager.setFrameLayout(self.frameLayout)

        self.mainLayout.addWidget(self.frameLayout, 11)

        self.centralwidget.setLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):
        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation",
                                               "Are you sure you want to logout",
                                               QMessageBox.Yes | QMessageBox.No)
        if logoutDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()
            self.frameLayoutManager.back()

    def setButtonHighlight(self, button):
        for buttonTemp in self.highlightButtonList:
            if buttonTemp == button:
                button.setStyleSheet("background-color: #3872E8; border-radius: 10px;")
            else:
                buttonTemp.setStyleSheet("background-color: #9DB9F2; border-radius: 10px;")