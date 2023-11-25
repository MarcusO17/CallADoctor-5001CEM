import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Clinic
from .PatientSendRequest import PatientSendRequest
from .PageManager import PageManager, FrameLayoutManager


class PatientClinicDetailsWindow(QWidget):

    def __init__(self, clinicTemp, patient):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        self.patient = patient
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(self.clinic.getClinicName())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
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
        self.backButton.setFixedSize(70, 70)
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

        self.clinicDescriptionTitle = QLabel(self.centralwidget)
        self.clinicDescriptionTitle.setGeometry(QRect(50, 160, 150, 40))
        self.clinicDescriptionTitle.setText("Clinic Description: ")

        self.clinicDescriptionLabel = QLabel(self.centralwidget)
        self.clinicDescriptionLabel.setGeometry(QRect(50, 190, 400, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clinicDescriptionLabel.setFont(font)
        self.clinicDescriptionLabel.setText(f"Clinic Name: {self.clinic.getClinicName()} \nClinic Contact: {str(self.clinic.getClinicContact())}")
        self.clinicDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.clinicDescriptionLabel.setStyleSheet("""QLabel {
                                                        border-radius: 10px;
                                                        border: 1px solid black;
                                                        background: white;
                                                        }""")
        self.clinicDescriptionLabel.setWordWrap(True)
        self.clinicDescriptionLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.clinicAddressTitle = QLabel(self.centralwidget)
        self.clinicAddressTitle.setGeometry(QRect(50, 400, 150, 40))
        self.clinicAddressTitle.setText("Clinic Address: ")

        self.clinicAddressLabel = QLabel(self.centralwidget)
        self.clinicAddressLabel.setGeometry(QRect(50, 430, 400, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clinicAddressLabel.setFont(font)
        self.clinicAddressLabel.setText(self.clinic.getClinicAddress())
        self.clinicAddressLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.clinicAddressLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")
        self.clinicAddressLabel.setWordWrap(True)
        self.clinicAddressLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.sendRequestButton = QPushButton(self.centralwidget)
        self.sendRequestButton.setGeometry(QRect(520, 500, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.sendRequestButton.setFont(font)
        self.sendRequestButton.setLayoutDirection(Qt.LeftToRight)
        self.sendRequestButton.setText("  Send Request")
        self.sendRequestButton.clicked.connect(self.sendRequestFunction)
        self.sendRequestButton.setStyleSheet("""QPushButton {
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
        
        self.sendRequestButtonLabel = QLabel(self.centralwidget)
        self.sendRequestButtonLabel.setGeometry(QRect(540, 525, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-send-file-30.png")
        self.sendRequestButtonIcon = QPixmap(filepath)
        self.sendRequestButtonIcon = self.sendRequestButtonIcon.scaled(50, 50)
        self.sendRequestButtonLabel.setPixmap(self.sendRequestButtonIcon)
        self.sendRequestButtonLabel.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        self.sendRequestButton.raise_()
        self.sendRequestButtonLabel.raise_()

        self.setLayout(mainLayout)


    def sendRequestFunction(self):
        self.patientSendRequest = PatientSendRequest(self.clinic, self.patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientSendRequest)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
