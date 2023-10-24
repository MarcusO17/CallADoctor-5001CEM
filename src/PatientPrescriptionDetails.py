import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import PrescriptionDetails
from .model import Prescription
from .PageManager import PageManager


class PatientPrescriptionDetailsWindow(QMainWindow):

    def __init__(self, patient, prescription):
        super().__init__()

        #set the information here
        self.prescription = prescription
        self.patient = patient
        self.pageManager = PageManager()
        self.setWindowTitle("Patient Prescription Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("patient_prescription_details")
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
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Prescription Details")
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

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.prescriptionDetailsList = self.prescription.getPrescriptionDetails()

        xStart = 180
        yStart = 220
        for i in range(len(self.prescriptionDetailsList)):
            self.prescriptionMedicationName = QLabel(self.centralwidget)
            self.prescriptionMedicationName.setGeometry(QRect(180, yStart, 300, 50))
            self.prescriptionMedicationName.setFrameShape(QtWidgets.QFrame.Box)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.prescriptionMedicationName.setFont(font)
            self.prescriptionMedicationName.setText(self.prescriptionDetailsList[i].getMedicationName())

            self.prescriptionDosage = QLabel(self.centralwidget)
            self.prescriptionDosage.setGeometry(QRect(550, yStart, 150, 50))
            self.prescriptionDosage.setFrameShape(QtWidgets.QFrame.Box)
            self.prescriptionDosage.setFont(font)
            self.prescriptionDosage.setText(self.prescriptionDetailsList[i].getDosage())

            self.prescriptionPillsPerDay = QLabel(self.centralwidget)
            self.prescriptionPillsPerDay.setGeometry(QRect(750, yStart, 150, 50))
            self.prescriptionPillsPerDay.setFrameShape(QtWidgets.QFrame.Box)
            self.prescriptionPillsPerDay.setFont(font)
            self.prescriptionPillsPerDay.setText(self.prescriptionDetailsList[i].getPillsPerDay())

            self.prescriptionPillsPerDay = QLabel(self.centralwidget)
            self.prescriptionPillsPerDay.setGeometry(QRect(950, yStart, 150, 50))
            self.prescriptionPillsPerDay.setFrameShape(QtWidgets.QFrame.Box)
            self.prescriptionPillsPerDay.setFont(font)
            self.prescriptionPillsPerDay.setText(self.prescriptionDetailsList[i].getFood())

            yStart = yStart + 100

        self.patientPrescriptionDetailsContainer = QLabel(self.centralwidget)
        self.patientPrescriptionDetailsContainer.setFixedSize(1000,500)
        self.patientPrescriptionDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.patientPrescriptionDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def backButtonFunction(self):
        self.pageManager.goBack()
