import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import PrescriptionDetails
from .model import Prescription
from .model import PrescriptionRepo
from .PageManager import PageManager, FrameLayoutManager


class DoctorViewPrescription(QWidget):

    def __init__(self, patient, appointment, doctor):
        super().__init__()

        #set the information here
        self.patient = patient
        self.appointment = appointment
        self.doctor = doctor

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        # use appointmentID to get prescriptionID
        self.prescription = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByAppointment(
                            self.appointment.getAppointmentID())[0]

        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Prescription Details")
        self.headerTitle.setObjectName("headerTitle")
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

        rowContainer = QWidget()
        rowContainer.setObjectName("rowContainer")
        rowContainer.setStyleSheet("""QWidget#rowContainer {
                                        background: #D0BFFF;
                                        border-radius: 10px;
                                        margin-left: 50px;
                                        }""")
        rowLayout = QVBoxLayout(rowContainer)
        rowContainer.setContentsMargins(20, 20, 20, 20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        medicationNameLabel = QLabel(self.centralwidget)
        medicationNameLabel.setGeometry(QRect(40, 120, 300, 50))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        medicationNameLabel.setFont(font)
        medicationNameLabel.setText("Medication Name: ")

        dosageLabel = QLabel(self.centralwidget)
        dosageLabel.setGeometry(QRect(380, 120, 150, 50))
        dosageLabel.setFont(font)
        dosageLabel.setText("Dosage: ")

        pillsPerDayLabel = QLabel(self.centralwidget)
        pillsPerDayLabel.setGeometry(QRect(570, 120, 100, 50))
        pillsPerDayLabel.setFont(font)
        pillsPerDayLabel.setText("Pills Per Day: ")

        foodLabel = QLabel(self.centralwidget)
        foodLabel.setGeometry(QRect(710, 120, 200, 50))
        foodLabel.setFont(font)
        foodLabel.setText("Before/After Eating: ")


        self.prescriptionDetailsList = self.prescription.getPrescriptionDetails()

        for count, prescriptionDetails in enumerate(self.prescriptionDetailsList):
            prescriptionMedicationName = QLabel()
            prescriptionMedicationName.setFixedSize(300,50)
            prescriptionMedicationName.setFrameShape(QtWidgets.QFrame.Box)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(16)
            prescriptionMedicationName.setFont(font)
            prescriptionMedicationName.setText(prescriptionDetails.getMedicationName())
            prescriptionMedicationName.setStyleSheet("""QLabel {
                                                    border-radius: 10px;
                                                    border: 1px solid black;
                                                    background: white;
                                                    }""")

            prescriptionDosage = QLabel()
            prescriptionDosage.setFixedSize(130,50)
            prescriptionDosage.setFrameShape(QtWidgets.QFrame.Box)
            prescriptionDosage.setFont(font)
            prescriptionDosage.setText(str(prescriptionDetails.getDosage()))
            prescriptionDosage.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

            prescriptionPillsPerDay = QLabel()
            prescriptionPillsPerDay.setFixedSize(100,50)
            prescriptionPillsPerDay.setFrameShape(QtWidgets.QFrame.Box)
            prescriptionPillsPerDay.setFont(font)
            prescriptionPillsPerDay.setText(str(prescriptionDetails.getPillsPerDay()))
            prescriptionPillsPerDay.setStyleSheet("""QLabel {
                                                    border-radius: 10px;
                                                    border: 1px solid black;
                                                    background: white;
                                                    }""")

            prescriptionFood = QLabel()
            prescriptionFood.setFixedSize(150,50)
            prescriptionFood.setFrameShape(QtWidgets.QFrame.Box)
            prescriptionFood.setFont(font)
            prescriptionFood.setText(prescriptionDetails.getFood())
            prescriptionFood.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

            row = QHBoxLayout()
            row.addWidget(prescriptionMedicationName)
            row.addWidget(prescriptionDosage)
            row.addWidget(prescriptionPillsPerDay)
            row.addWidget(prescriptionFood)

            rowContainer.layout().addLayout(row)

        boxScrollArea.setWidget(rowContainer)
        boxScrollArea.setFixedSize(900, 500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 30px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def backButtonFunction(self):
        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

