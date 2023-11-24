import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QMessageBox, QGraphicsDropShadowEffect
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
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(f"{self.request.getAppointmentID()} Details")
        self.headerTitle.setGeometry(QRect(80, 40, 700, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                        background: #D0BFFF;
                                                        border-radius: 10px;
                                                        }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(800, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-back-64.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonFunction)
        self.backButton.setStyleSheet("""QPushButton#backButton {
                                            background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                    stop: 0 rgba(10, 2, 85, 255), 
                                                                    stop: 1 rgba(59, 41, 168, 255));
                                            border-radius: 10px; color: white;

                                            }
                                            QPushButton#backButton:hover
                                            {
                                              background-color: #7752FE;
                                            }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.backButton.setGraphicsEffect(effect)

        detailsContainer = QLabel(self.centralwidget)
        detailsContainer.setGeometry(QRect(20, 150, 900, 500))
        detailsContainer.setStyleSheet("""QLabel {
                                        background: #D0BFFF;
                                        border-radius: 10px;
                                        }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        detailsContainer.setGraphicsEffect(effect)

        self.requestReasonTitle = QLabel(self.centralwidget)
        self.requestReasonTitle.setGeometry(QRect(50, 190, 150, 40))
        self.requestReasonTitle.setText("Request Reason: ")

        self.requestReasonLabel = QLabel(self.centralwidget)
        self.requestReasonLabel.setGeometry(QRect(50, 220, 400, 200))
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.requestReasonLabel.setFont(font)
        self.requestReasonLabel.setText(f"{self.request.getRequestReason()}")
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.requestReasonLabel.setWordWrap(True)
        self.requestReasonLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.requestReasonLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QRect(730, 170, 150, 40))
        self.dateLabel.setFont(font)
        self.dateLabel.setText(f"Date Submitted: {self.request.getDateSubmitted()}")
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.dateLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

        self.appointmentTitle = QLabel(self.centralwidget)
        self.appointmentTitle.setGeometry(QRect(470, 190, 150, 40))
        self.appointmentTitle.setText("Appointment Details")

        self.appointmentLabel = QLabel(self.centralwidget)
        self.appointmentLabel.setGeometry(QRect(470, 220, 400, 200))
        self.appointmentLabel.setFont(font)
        self.appointmentLabel.setWordWrap(True)
        self.appointmentLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.appointmentLabel.setText(f"AppointmentID: {self.appointment.getAppointmentID()} \n"
                                      f"Doctor Assigned: {self.appointment.getDoctorID()} \n"
                                      f"Start Time: {self.appointment.getStartTime()} \n"
                                      f"Status: {self.appointment.getAppointmentStatus()}")
        self.appointmentLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QRect(50, 530, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.cancelButton.setFont(font)
        self.cancelButton.setLayoutDirection(Qt.LeftToRight)
        self.cancelButton.setText("   Cancel Request")
        self.cancelButton.clicked.connect(self.cancelRequestFunction)
        self.cancelButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: center; 
                                                    color:white;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: center; 
                                                      color:white;
                                                    }""")

        self.cancelButtonLabel = QLabel(self.centralwidget)
        self.cancelButtonLabel.setGeometry(QRect(70, 555, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-remove-64.png")
        self.cancelButtonIcon = QPixmap(filepath)
        self.cancelButtonIcon = self.cancelButtonIcon.scaled(50, 50)
        self.cancelButtonLabel.setPixmap(self.cancelButtonIcon)

        self.acceptButton = QPushButton(self.centralwidget)
        self.acceptButton.setGeometry(QRect(550, 530, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.acceptButton.setFont(font)
        self.acceptButton.setLayoutDirection(Qt.LeftToRight)
        self.acceptButton.setText("    Accept Request")
        self.acceptButton.clicked.connect(self.acceptRequestFunction)
        self.acceptButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: center; 
                                                    color:white;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: center; 
                                                      color:white;
                                                    }""")

        self.acceptButtonLabel = QLabel(self.centralwidget)
        self.acceptButtonLabel.setGeometry(QRect(570, 555, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-add-64.png")
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
            self.request.approveRequest()
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
            self.request.cancelRequest(self.request.getRequestID())
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.widget(self.frameLayoutManager.top()).generateCancellationButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


