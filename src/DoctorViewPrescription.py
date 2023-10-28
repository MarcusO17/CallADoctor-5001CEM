import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
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
                            self.appointment.getAppointmentID())

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
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Prescription Details")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        rowContainer = QWidget()
        rowLayout = QVBoxLayout(rowContainer)
        rowContainer.setContentsMargins(20, 20, 20, 20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        medicationNameLabel = QLabel(self.centralwidget)
        medicationNameLabel.setGeometry(QRect(80, 120, 300, 50))
        medicationNameLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        medicationNameLabel.setFont(font)
        medicationNameLabel.setText("Medication Name: ")

        dosageLabel = QLabel(self.centralwidget)
        dosageLabel.setGeometry(QRect(420, 120, 150, 50))
        dosageLabel.setFrameShape(QtWidgets.QFrame.Box)
        dosageLabel.setFont(font)
        dosageLabel.setText("Dosage: ")

        pillsPerDayLabel = QLabel(self.centralwidget)
        pillsPerDayLabel.setGeometry(QRect(610, 120, 150, 50))
        pillsPerDayLabel.setFrameShape(QtWidgets.QFrame.Box)
        pillsPerDayLabel.setFont(font)
        pillsPerDayLabel.setText("Pills Per Day: ")

        foodLabel = QLabel(self.centralwidget)
        foodLabel.setGeometry(QRect(790, 120, 200, 50))
        foodLabel.setFrameShape(QtWidgets.QFrame.Box)
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
            font.setBold(True)
            font.setWeight(75)
            prescriptionMedicationName.setFont(font)
            prescriptionMedicationName.setText(prescriptionDetails.getMedicationName())

            prescriptionDosage = QLabel()
            prescriptionDosage.setFixedSize(150,50)
            prescriptionDosage.setFrameShape(QtWidgets.QFrame.Box)
            prescriptionDosage.setFont(font)
            prescriptionDosage.setText(prescriptionDetails.getDosage())

            prescriptionPillsPerDay = QLabel()
            prescriptionPillsPerDay.setFixedSize(150,50)
            prescriptionPillsPerDay.setFrameShape(QtWidgets.QFrame.Box)
            prescriptionPillsPerDay.setFont(font)
            prescriptionPillsPerDay.setText(str(prescriptionDetails.getPillsPerDay()))

            prescriptionFood = QLabel()
            prescriptionFood.setFixedSize(150,50)
            prescriptionFood.setFrameShape(QtWidgets.QFrame.Box)
            prescriptionFood.setFont(font)
            prescriptionFood.setText(prescriptionDetails.getFood())

            row = QHBoxLayout()
            row.addWidget(prescriptionMedicationName)
            row.addWidget(prescriptionDosage)
            row.addWidget(prescriptionPillsPerDay)
            row.addWidget(prescriptionFood)

            rowContainer.layout().addLayout(row)

        boxScrollArea.setWidget(rowContainer)
        boxScrollArea.setFixedSize(1000, 500)
        boxScrollArea.setStyleSheet("margin-left: 100px; margin top: 20px")
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def backButtonFunction(self):
        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

