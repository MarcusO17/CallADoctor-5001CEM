import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea
from PyQt5 import QtCore, QtWidgets

from .AccountPage import AccountPage
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager


class ClinicAppointmentDetails(QMainWindow):

    def __init__(self, appointment, doctor, clinic):
        super().__init__()
        self.pageManager = PageManager()
        # set the information here
        self.appointment = appointment
        self.doctor = doctor
        self.clinic = clinic
        self.setWindowTitle("Appointment Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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
        self.headerTitle.setText(self.appointment.getAppointmentID())
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
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.appointmentPurposeLabel = QLabel(self.centralwidget)
        self.appointmentPurposeLabel.setGeometry(QRect(180, 220, 400, 200))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.appointmentPurposeLabel.setFont(font)
        self.appointmentPurposeLabel.setText(str(self.appointment.getVisitReason()))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.doctorDetailsLabel = QLabel(self.centralwidget)
        self.doctorDetailsLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.doctorDetailsLabel.setFont(font)
        self.doctorDetailsLabel.setText(str(self.doctor.getDoctorName()))
        self.doctorDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.dateTitle = QLabel(self.centralwidget)
        self.dateTitle.setGeometry(QRect(180, 420, 150, 40))
        self.dateTitle.setText("Date: ")
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QRect(180, 450, 150, 40))
        self.dateLabel.setText(str(self.appointment.getAppointmentDate()))
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.startTimeTitle = QLabel(self.centralwidget)
        self.startTimeTitle.setGeometry(QRect(180, 490, 150, 40))
        self.startTimeTitle.setText("Start Time: ")
        self.startTimeLabel = QLabel(self.centralwidget)
        self.startTimeLabel.setGeometry(QRect(180, 530, 150, 40))
        self.startTimeLabel.setText(self.appointment.getStartTime())
        self.startTimeLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.endTimeTitle = QLabel(self.centralwidget)
        self.endTimeTitle.setGeometry(QRect(390, 490, 150, 40))
        self.endTimeTitle.setText("End Time: ")
        self.endTimeLabel = QLabel(self.centralwidget)
        self.endTimeLabel.setGeometry(QRect(390, 530, 150, 40))
        self.endTimeLabel.setText(self.appointment.getEndTime())
        self.endTimeLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.cancelAppointmentButton = QPushButton(self.centralwidget)
        self.cancelAppointmentButton.setGeometry(QRect(710, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cancelAppointmentButton.setFont(font)
        self.cancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.cancelAppointmentButton.setText("Cancel Request")
        self.cancelAppointmentButton.clicked.connect(self.cancelAppointmentFunction)

        self.cancelAppointmentLabel = QLabel(self.centralwidget)
        self.cancelAppointmentLabel.setGeometry(QRect(730, 570, 50, 50))
        self.cancelAppointmentLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.cancelAppointmentIcon = QPixmap(filepath)
        self.cancelAppointmentIcon = self.cancelAppointmentIcon.scaled(50, 50)
        self.cancelAppointmentLabel.setPixmap(self.cancelAppointmentIcon)

        self.container = QLabel(self.centralwidget)
        self.container.setFixedSize(1000, 500)
        self.container.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(20)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.container)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

        # Cancel Appointment With Doctor

    def cancelAppointmentFunction(self):
        cancelAppointmentDialogBox = QMessageBox.question(self.centralWidget, "Cancel Confirmation",
                                                          "Are you sure you want to cancel Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if cancelAppointmentDialogBox == QMessageBox.Yes:
            self.appointment.setAppointmentStatus("Cancelled")
            self.pageManager.goBack()
            print(self.appointment.getAppointmentStatus())

    def backButtonFunction(self):
        self.pageManager.goBack()

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Clinic", self.clinic)
        self.pageManager.add(self.accountPage)