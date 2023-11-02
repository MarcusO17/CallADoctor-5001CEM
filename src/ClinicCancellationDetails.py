import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QMessageBox
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .AssignDoctorDialog import AssignDoctorDialog
from .model import Appointment, Clinic
from .PageManager import PageManager, FrameLayoutManager


class ClinicCancellationDetails(QWidget):

    def __init__(self, request, clinic):
        super().__init__()

        # set the information here
        self.request = request  # appointmentObject
        self.clinic = clinic
        self.appointment = Appointment.getAppointmentfromID(self.request.getAppointmentID())
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(self.request.getRequestID())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1000, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.requestReasonLabel = QLabel(self.centralwidget)
        self.requestReasonLabel.setGeometry(QRect(180, 220, 400, 300))
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.requestReasonLabel.setFont(font)
        self.requestReasonLabel.setText(self.request.getRequestReason())
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QRect(700, 220, 150, 40))
        self.dateLabel.setFont(font)
        self.dateLabel.setText(str(self.request.getDateSubmitted()))
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.appointmentLabel = QLabel(self.centralwidget)
        self.appointmentLabel.setGeometry(QRect(700, 350, 250, 200))
        self.appointmentLabel.setText(f"AppointmentID: {self.appointment.getAppointmentID()} \n"
                                      f"Doctor Assigned: {self.appointment.getDoctorID()} \n"
                                      f"Start Time: {self.appointment.getStartTime()} \n"
                                      f"Status: {self.appointment.getAppointmentStatus()}")

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QRect(180, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.cancelButton.setFont(font)
        self.cancelButton.setLayoutDirection(Qt.LeftToRight)
        self.cancelButton.setText("Reject Cancellation")
        self.cancelButton.setStyleSheet("padding-left: 50px;")
        self.cancelButton.clicked.connect(self.cancelRequestFunction)

        self.cancelButtonLabel = QLabel(self.centralwidget)
        self.cancelButtonLabel.setGeometry(QRect(200, 570, 50, 50))
        self.cancelButtonLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.cancelButtonIcon = QPixmap(filepath)
        self.cancelButtonIcon = self.cancelButtonIcon.scaled(50, 50)
        self.cancelButtonLabel.setPixmap(self.cancelButtonIcon)

        self.acceptButton = QPushButton(self.centralwidget)
        self.acceptButton.setGeometry(QRect(710, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.acceptButton.setFont(font)
        self.acceptButton.setLayoutDirection(Qt.LeftToRight)
        self.acceptButton.setText("Accept Cancellation")
        self.acceptButton.setStyleSheet("padding-left: 50px;")
        self.acceptButton.clicked.connect(self.acceptRequestFunction)

        self.acceptButtonLabel = QLabel(self.centralwidget)
        self.acceptButtonLabel.setGeometry(QRect(730, 570, 50, 50))
        self.acceptButtonLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.acceptButtonIcon = QPixmap(filepath)
        self.acceptButtonIcon = self.acceptButtonIcon.scaled(50, 50)
        self.acceptButtonLabel.setPixmap(self.acceptButtonIcon)

        self.acceptButton.raise_()
        self.acceptButtonLabel.raise_()
        self.cancelButton.raise_()
        self.cancelButtonLabel.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)

    def backButtonFunction(self):
        backConfirmationDialogBox = QMessageBox.question(self.centralwidget, "Back Confirmation",
                                                         "Are you sure you want to back from this request, you may continue later.",
                                                         QMessageBox.Yes | QMessageBox.No)
        if backConfirmationDialogBox == QMessageBox.Yes:
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def acceptRequestFunction(self):
        acceptRequestDialogBox = QMessageBox.question(self.centralwidget, "Request Confirmation",
                                                      "Are you sure you want to approve this request",
                                                      QMessageBox.Yes | QMessageBox.No)
        if acceptRequestDialogBox == QMessageBox.Yes:
            self.request.setApprovalStatus("Approved")
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.widget(self.frameLayoutManager.top()).generateCancellationButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def cancelRequestFunction(self):
        cancelRequestDialogBox = QMessageBox.question(self.centralwidget, "Request Cancel Confirmation",
                                                      "Are you sure you want to deny this request",
                                                      QMessageBox.Yes | QMessageBox.No)
        if cancelRequestDialogBox == QMessageBox.Yes:
            self.request.setApprovalStatus("Deny")
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.widget(self.frameLayoutManager.top()).generateCancellationButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


