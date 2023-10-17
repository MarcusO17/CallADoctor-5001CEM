import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from model import Patient

class DocPatientDetailsWindow(QMainWindow):

    def __init__(self, patientTemp):
        super().__init__()

        #set the information here
        self.patient = patientTemp
        print(self.patient.getPatientID(), self.patient.getPatientName(), self.patient.getPatientDOB(), self.patient.getPatientAddress, self.patient.getPatientBlood, self.patient.getPatientBlood())
        self.setWindowTitle("Patient Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("patient_details")
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
        self.headerTitle.setText(self.patient.getPatientName())
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
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)

        self.patientAppointmentDetailLabel = QLabel(self.centralwidget)
        self.patientAppointmentDetailLabel.setGeometry(QRect(180, 220, 400, 200))
        self.patientAppointmentDetailLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patientAppointmentDetailLabel.setFont(font)
        self.patientAppointmentDetailLabel.setText("Data of Patient Appointment")
        self.patientAppointmentDetailLabel.setFrameShape(QtWidgets.QFrame.Box)
        

        self.patientDescriptionsLabel = QLabel(self.centralwidget)
        self.patientDescriptionsLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patientDescriptionsLabel.setFont(font)
        self.patientDescriptionsLabel.setText(str(self.patient.getPatientName()) + " " + str(self.patient.getPatientDOB()) + " " + str(self.patient.getPatientBlood()) + " " + str(self.patient.getPatientRace()))
        self.patientDescriptionsLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.patientAddressLabel = QLabel(self.centralwidget)
        self.patientAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patientAddressLabel.setFont(font)
        self.patientAddressLabel.setText(self.patient.getPatientAddress())
        self.patientAddressLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.sendRequestButton = QPushButton(self.centralwidget)
        self.sendRequestButton.setGeometry(QRect(710, 545, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.sendRequestButton.setFont(font)
        self.sendRequestButton.setLayoutDirection(Qt.LeftToRight)
        self.sendRequestButton.setText("Send Request")
        self.sendRequestButton.clicked.connect(self.sendRequestFunction)

        self.sendRequestLabel = QLabel(self.centralwidget)
        self.sendRequestLabel.setGeometry(QRect(730, 570, 50, 50))
        self.sendRequestLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.sendRequestIcon = QPixmap(filepath)
        self.sendRequestIcon = self.sendRequestIcon.scaled(50, 50)
        self.sendRequestLabel.setPixmap(self.sendRequestIcon)

        self.patientDetailsContainer = QLabel(self.centralwidget)
        self.patientDetailsContainer.setFixedSize(1000,500)
        self.patientDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.patientDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def sendRequestFunction(self):
        pass
        # go to send request window
        # pass the clinic object to the window