import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from model import Prescription
from PatientPrescriptionDetails import PatientPrescriptionDetailsWindow

class PatientPrescriptionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prescription (Patient)")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PatientPrescription")
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
        self.headerTitle.setText("Welcome! [name]")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.patientPrescriptionMyAccountButton = QPushButton(self.centralwidget)
        self.patientPrescriptionMyAccountButton.setFixedSize(70,70)
        self.patientPrescriptionMyAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.patientPrescriptionMyAccountIcon = QIcon(filepath)
        self.patientPrescriptionMyAccountButton.setIconSize(QSize(70, 70))
        self.patientPrescriptionMyAccountButton.setIcon(self.patientPrescriptionMyAccountIcon)

        # Push Button 5 (Log Out)
        self.patientPrescriptionBackButton = QPushButton(self.centralwidget)
        self.patientPrescriptionBackButton.setFixedSize(70, 70)
        self.patientPrescriptionBackButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.patientPrescriptionBackIcon = QIcon(filepath)
        self.patientPrescriptionBackButton.setIconSize(QSize(70, 70))
        self.patientPrescriptionBackButton.setIcon(self.patientPrescriptionBackIcon)

        buttonContainer = QVBoxLayout()
        buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        prescriptionList = list()


        prescription1 = Prescription("pr0001", "ap1001", "Prescription 1 Name", "3 piils", "food 1", "Dosage 1")
        prescription2 = Prescription("pr0002", "ap1002", "Prescription 2 Name", "2 piils", "food 2", "Dosage 2")
        prescription3 = Prescription("pr0003", "ap1003", "Prescription 3 Name", "4 piils", "food 3", "Dosage 3")

        prescriptionList.append(prescription1)
        prescriptionList.append(prescription2)
        prescriptionList.append(prescription3)
        print("prescription list size" , len(prescriptionList))

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, Prescription in enumerate(prescriptionList):
            self.prescriptionButton = QPushButton()
            self.prescriptionButton.setText(Prescription.getPrescriptionID() + " - " + Prescription.getMedicationName())
            self.prescriptionButton.setFont(buttonFont)
            self.prescriptionButton.setFixedSize(QSize(950,150))
            self.prescriptionButton.clicked.connect(lambda checked, prescription=Prescription: self.prescriptionButtonFunction(prescription))
            buttonContainer.addWidget(self.prescriptionButton)

        boxScrollArea.setLayout(buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def prescriptionButtonFunction(self, patient):
        # update the clinic details page here according to button click
        self.prescriptionDetailsWindow = PatientPrescriptionDetailsWindow(patient)
        self.prescriptionDetailsWindow.show()
        self.close()