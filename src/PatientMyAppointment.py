import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PatientAppointmentDetails import PatientAppointmentDetailsWindow 
from .PageManager import PageManager, FrameLayoutManager


class PatientMyAppointmentWindow(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.setWindowTitle("My Appointment")
        self.patient = patient
        self.pageManager = PageManager()
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("My Appointment")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(80, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.buttonContainer = QWidget()
        buttonLayout = QVBoxLayout(self.buttonContainer)
        buttonLayout.setSpacing(20)
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            margin-left: 100px;
                                                            }""")
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.appointmentList = list()

        self.generateAppointmentButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(900,500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 80px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        spacer = QWidget()
        spacer.setFixedHeight(30)
        
        mainLayout.addWidget(spacer)

        self.setLayout(mainLayout)

    def appointmentButtonFunction(self, appointment, patient):
        # Need to update the  page where it goes here according to button click
        self.patientAppointmentDetailsWindow = PatientAppointmentDetailsWindow(appointment, patient)
        self.patientAppointmentDetailsWindow.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientAppointmentDetailsWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateAppointmentButtons(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.appointmentList.clear()

        #query appointment here
        self.appointmentList = AppointmentRepository.getAppointmentsByPatients(self.patient.getPatientID())
        self.appointmentList = [appointment for appointment in self.appointmentList if appointment.getAppointmentStatus() != 'Cancelled']

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-appointment-50.png")
        patientAppointmentIcon = QIcon(filepath)

        for count, appointment in enumerate(self.appointmentList):
            self.patientAppointmentButton = QPushButton()
            self.patientAppointmentButton.setText(
                appointment.getAppointmentID() + " - " + appointment.getAppointmentStatus())
            self.patientAppointmentButton.setFont(buttonFont)
            self.patientAppointmentButton.setIconSize(QSize(80, 80))
            self.patientAppointmentButton.setFixedSize(QSize(700, 100))
            self.patientAppointmentButton.setIcon(patientAppointmentIcon)
            self.patientAppointmentButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: left; 
                                                    padding-left: 20px;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: left; 
                                                      padding-left: 20px;
                                                    }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            self.patientAppointmentButton.setGraphicsEffect(effect)
            self.patientAppointmentButton.clicked.connect(
                lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.patient))
            self.buttonContainer.layout().addWidget(self.patientAppointmentButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)
