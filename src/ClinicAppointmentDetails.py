import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QGraphicsDropShadowEffect
from PyQt5 import QtCore, QtWidgets

from .AccountPage import AccountPage
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager, FrameLayoutManager


class ClinicAppointmentDetails(QWidget):

    def __init__(self, appointment, doctor, clinic):
        super().__init__()
        # set the information here
        self.appointment = appointment
        self.doctor = doctor
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(f"{self.appointment.getAppointmentID()} Appointment")
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

        self.appointmentPurposeTitle = QLabel(self.centralwidget)
        self.appointmentPurposeTitle.setGeometry(QRect(50, 190, 150, 40))
        self.appointmentPurposeTitle.setText("Appointment Purpose: ")

        self.appointmentPurposeLabel = QLabel(self.centralwidget)
        self.appointmentPurposeLabel.setGeometry(QRect(50, 220, 400, 200))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.appointmentPurposeLabel.setFont(font)
        self.appointmentPurposeLabel.setText(str(self.appointment.getVisitReason()))
        self.appointmentPurposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.appointmentPurposeLabel.setWordWrap(True)
        self.appointmentPurposeLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.appointmentPurposeLabel.setStyleSheet("""QLabel {
                                                        border-radius: 10px;
                                                        border: 1px solid black;
                                                        background: white;
                                                        }""")

        self.doctorDetailsTitle = QLabel(self.centralwidget)
        self.doctorDetailsTitle.setGeometry(QRect(520, 190, 150, 40))
        self.doctorDetailsTitle.setText("Doctor Details: ")

        self.doctorDetailsLabel = QLabel(self.centralwidget)
        self.doctorDetailsLabel.setGeometry(QRect(520, 220, 375, 200))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.doctorDetailsLabel.setFont(font)
        self.doctorDetailsLabel.setText(f"Doctor ID: {self.doctor.getDoctorID()}\n"
                                        f"Doctor Name: {self.doctor.getDoctorName()}\n"
                                        f"Doctor Contact: {self.doctor.getDoctorContact()}\n"
                                        f"Doctor Type: {self.doctor.getDoctorType()}\n")

        self.doctorDetailsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorDetailsLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")
        self.doctorDetailsLabel.setWordWrap(True)
        self.doctorDetailsLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)


        self.dateTitle = QLabel(self.centralwidget)
        self.dateTitle.setGeometry(QRect(50, 460, 150, 40))
        self.dateTitle.setText("Date: ")
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QRect(50, 490, 150, 40))
        self.dateLabel.setText(str(self.appointment.getAppointmentDate()))
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.dateLabel.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")

        self.startTimeTitle = QLabel(self.centralwidget)
        self.startTimeTitle.setGeometry(QRect(50, 530, 150, 40))
        self.startTimeTitle.setText("Start Time: ")
        self.startTimeLabel = QLabel(self.centralwidget)
        self.startTimeLabel.setGeometry(QRect(50, 570, 150, 40))
        self.startTimeLabel.setText(self.appointment.getStartTime())
        self.startTimeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.startTimeLabel.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        self.endTimeTitle = QLabel(self.centralwidget)
        self.endTimeTitle.setGeometry(QRect(260, 530, 150, 40))
        self.endTimeTitle.setText("End Time: ")
        self.endTimeLabel = QLabel(self.centralwidget)
        self.endTimeLabel.setGeometry(QRect(260, 570, 150, 40))
        self.endTimeLabel.setText(self.appointment.getEndTime())
        self.endTimeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.endTimeLabel.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        self.cancelAppointmentButton = QPushButton(self.centralwidget)
        self.cancelAppointmentButton.setGeometry(QRect(520, 510, 325, 100))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.cancelAppointmentButton.setFont(font)
        self.cancelAppointmentButton.setLayoutDirection(Qt.RightToLeft)
        self.cancelAppointmentButton.setText("Cancel Request")
        self.cancelAppointmentButton.clicked.connect(self.cancelAppointmentFunction)

        self.cancelAppointmentLabel = QLabel(self.centralwidget)
        self.cancelAppointmentLabel.setGeometry(QRect(540, 535, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-remove-64.png")
        self.cancelAppointmentIcon = QPixmap(filepath)
        self.cancelAppointmentIcon = self.cancelAppointmentIcon.scaled(50, 50)
        self.cancelAppointmentLabel.setPixmap(self.cancelAppointmentIcon)
        self.cancelAppointmentButton.setStyleSheet("""QPushButton {
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

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)

        # Cancel Appointment With Doctor

    # this method is triggered when the cancel appointment button is clicked
    def cancelAppointmentFunction(self):
        cancelAppointmentDialogBox = QMessageBox.question(self, "Cancel Confirmation",
                                                          "Are you sure you want to cancel Appointment?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if cancelAppointmentDialogBox == QMessageBox.Yes:
            self.appointment.cancelAppointment()
            # implement back end stuff here
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()
            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
            try:
                self.frameLayout.widget(self.frameLayoutManager.top()).setSchedule()
            except Exception as e:
                print(e)

    # this method is triggered when the back button is clicked
    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
