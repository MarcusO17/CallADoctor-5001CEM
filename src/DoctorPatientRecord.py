import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy
from PyQt5 import QtWidgets
from .AccountPage import AccountPage
from .model import Patient,Doctor
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .PageManager import PageManager, FrameLayoutManager


class DoctorPatientRecordWindow(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.setWindowTitle("Patient Record (Doctor)")
        self.pageManager = PageManager()
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
        self.headerTitle.setText("Patient Record")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        buttonContainer = QVBoxLayout()
        buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        patientList = Doctor.getDoctorPastPatients(self.doctor.getDoctorID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, patient in enumerate(patientList):
            self.patientButton = QPushButton()
            self.patientButton.setText(patient.getPatientID() + " - " + patient.getPatientName())
            self.patientButton.setFont(buttonFont)
            self.patientButton.setFixedSize(QSize(950,150))
            self.patientButton.clicked.connect(lambda checked, patient=patient: self.patientButtonFunction(patient, self.doctor))
            buttonContainer.addWidget(self.patientButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        buttonContainer.layout().addWidget(spacer)

        boxScrollArea.setLayout(buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        boxScrollArea.setStyleSheet("margin-left: 100px; margin top: 20px")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def patientButtonFunction(self, patient, doctor):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()
        # update the clinic details page here according to button click
        self.patientHistoryWindow = DoctorPatientHistoryWindow(patient, doctor)
        self.frameLayout.addWidget(self.patientHistoryWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

