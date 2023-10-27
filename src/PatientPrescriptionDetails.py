import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import PrescriptionDetails
from .model import Prescription
from .PageManager import PageManager


class PatientPrescriptionDetailsWindow(QMainWindow):

    def __init__(self, patient, prescription):
        super().__init__()

        #set the information here
        self.prescription = prescription
        self.patient = patient
        self.prescription = prescription
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
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.prescriptionDetailsList = self.prescription[0].getPrescriptionDetails()

        rowContainer = QWidget()
        rowLayout = QVBoxLayout(rowContainer)
        rowContainer.setContentsMargins(20, 20, 20, 20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        medicationNameLabel = QLabel(self.centralwidget)
        medicationNameLabel.setGeometry(QRect(190, 130, 300, 50))
        medicationNameLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        medicationNameLabel.setFont(font)
        medicationNameLabel.setText("Medication Name: ")

        dosageLabel = QLabel(self.centralwidget)
        dosageLabel.setGeometry(QRect(530, 130, 150, 50))
        dosageLabel.setFrameShape(QtWidgets.QFrame.Box)
        dosageLabel.setFont(font)
        dosageLabel.setText("Dosage: ")

        pillsPerDayLabel = QLabel(self.centralwidget)
        pillsPerDayLabel.setGeometry(QRect(720, 130, 150, 50))
        pillsPerDayLabel.setFrameShape(QtWidgets.QFrame.Box)
        pillsPerDayLabel.setFont(font)
        pillsPerDayLabel.setText("Pills Per Day: ")

        foodLabel = QLabel(self.centralwidget)
        foodLabel.setGeometry(QRect(900, 130, 200, 50))
        foodLabel.setFrameShape(QtWidgets.QFrame.Box)
        foodLabel.setFont(font)
        foodLabel.setText("Before/After Eating: ")


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
            prescriptionDosage.setText(str(prescriptionDetails.getDosage()))

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

    def backButtonFunction(self):
        self.pageManager.goBack()

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Patient", self.patient)
        self.pageManager.add(self.accountPage)

