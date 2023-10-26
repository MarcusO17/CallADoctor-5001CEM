import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QLineEdit
from PyQt5 import QtCore, QtWidgets
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager


class AccountPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pageManager = PageManager()
        # set the information here
        self.user = None
        self.setWindowTitle("Account Page")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.mode = None

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("My Account")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.nameTitle = QLabel(self.centralwidget)
        self.nameTitle.setGeometry(QRect(180, 200, 400, 30))
        self.nameTitle.setText("Name: ")

        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QRect(180, 230, 400, 50))
        self.nameLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.iDTitle = QLabel(self.centralwidget)
        self.iDTitle.setGeometry(QRect(180, 280, 400, 30))
        self.iDTitle.setText("ID: ")

        self.iDLabel = QLabel(self.centralwidget)
        self.iDLabel.setGeometry(QRect(180, 310, 400, 50))
        self.iDLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.flexTitle1 = QLabel(self.centralwidget)
        self.flexTitle1.setGeometry(QRect(180, 360, 400, 30))
        self.flexTitle1.hide()

        self.flexLabel1 = QLabel(self.centralwidget)
        self.flexLabel1.setGeometry(QRect(180, 390, 400, 50))
        self.flexLabel1.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel1.hide()

        self.flexTitle2 = QLabel(self.centralwidget)
        self.flexTitle2.setGeometry(QRect(180, 440, 400, 30))
        self.flexTitle2.hide()

        self.flexLabel2 = QLabel(self.centralwidget)
        self.flexLabel2.setGeometry(QRect(180, 470, 400, 50))
        self.flexLabel2.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel2.hide()

        self.flexTitle3 = QLabel(self.centralwidget)
        self.flexTitle3.setGeometry(QRect(180, 520, 400, 30))
        self.flexTitle3.hide()

        self.flexLabel3 = QLabel(self.centralwidget)
        self.flexLabel3.setGeometry(QRect(180, 550, 400, 50))
        self.flexLabel3.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel3.hide()

        self.flexTitle4 = QLabel(self.centralwidget)
        self.flexTitle4.setGeometry(QRect(180, 600, 400, 30))
        self.flexTitle4.hide()

        self.flexLabel4 = QLabel(self.centralwidget)
        self.flexLabel4.setGeometry(QRect(180, 630, 400, 50))
        self.flexLabel4.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel4.hide()

        self.flexTitle5 = QLabel(self.centralwidget)
        self.flexTitle5.setGeometry(QRect(700, 190, 400, 30))
        self.flexTitle5.hide()

        self.flexLabel5 = QLabel(self.centralwidget)
        self.flexLabel5.setGeometry(QRect(700, 220, 400, 50))
        self.flexLabel5.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel5.hide()

        self.addressTitle = QLabel(self.centralwidget)
        self.addressTitle.setGeometry(QRect(700, 190, 400, 30))
        self.addressTitle.setText("Address: ")
        self.addressTitle.hide()

        self.addressLabel = QLineEdit(self.centralwidget)
        self.addressLabel.setGeometry(QRect(700, 220, 375, 200))
        self.addressLabel.setDisabled(True)
        self.addressLabel.hide()

        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.statusLabel.setGeometry(QRect(700, 420, 400, 50))
        self.statusLabel.hide()

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setGeometry(QRect(790, 545, 280, 100))
        self.editButton.setLayoutDirection(Qt.RightToLeft)
        self.editButton.setText("Edit")
        self.editButton.clicked.connect(self.editButtonFunction)
        self.editButtonState = True

        self.container = QLabel(self.centralwidget)
        self.container.setFixedSize(1000, 500)
        self.container.setFrameShape(QtWidgets.QFrame.Box)

        self.editButton.raise_()
        self.addressLabel.raise_()

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.container)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def editButtonFunction(self):
        if self.editButtonState == True:

            self.editButtonState = False
            self.editButton.setText("Save")
            if self.mode == "Patient":
                self.addressLabel.setEnabled(True)
        else:
            self.editButtonState = True
            self.editButton.setText("Edit")
            if self.mode == "Patient":
                self.addressLabel.setEnabled(False)
                self.user.setPatientAddress(self.addressLabel.text())


    def backButtonFunction(self):
        self.pageManager.goBack()

    def setUser(self, mode, user):
        self.user = user
        if mode == "Patient":
            self.mode = "Patient"
            self.nameLabel.setText(self.user.getPatientName())
            self.iDLabel.setText(self.user.getPatientID())
            self.flexTitle1.setText("Date of Birth")
            self.flexTitle1.show()
            self.flexLabel1.setText(self.user.getPatientDOB())
            self.flexLabel1.show()
            self.flexTitle2.setText("Blood Type")
            self.flexTitle2.show()
            self.flexLabel2.setText(self.user.getPatientBlood())
            self.flexLabel2.show()
            self.flexTitle3.setText("Race")
            self.flexTitle3.show()
            self.flexLabel3.setText(self.user.getPatientRace())
            self.flexLabel3.show()
            self.addressLabel.setText(self.user.getPatientAddress())
            self.addressLabel.show()
            self.addressTitle.show()
        elif mode == "Clinic":
            self.mode = "Clinic"
            self.nameLabel.setText(self.user.getClinicName())
            self.iDLabel.setText(self.user.getClinicID())
            self.flexTitle1.setText("Clinic Contact")
            self.flexTitle1.show()
            self.flexLabel1.setText(str(self.user.getClinicContact()))
            self.flexLabel1.show()
            self.addressTitle.show()
            self.addressLabel.setText(self.user.getClinicAddress())
            self.addressLabel.show()
            self.statusLabel.setText(str(self.user.getClinicStatus()))
            self.statusLabel.show()
        elif mode == "Doctor":
            self.mode = "Doctor"
            self.nameLabel.setText(self.user.getDoctorName())
            self.iDLabel.setText(self.user.getDoctorID())
            self.flexTitle1.setText("IC Number")
            self.flexTitle1.show()
            self.flexLabel1.setText(self.user.getDoctorICNumber())
            self.flexLabel1.show()
            self.flexTitle2.setText("Doctor Type")
            self.flexTitle2.show()
            self.flexLabel2.setText(self.user.getDoctorType())
            self.flexLabel2.show()
            self.flexTitle3.setText("Doctor Contact")
            self.flexTitle3.show()
            self.flexLabel3.setText(self.user.getDoctorContact())
            self.flexLabel3.show()
            self.flexTitle4.setText("Years of Experience")
            self.flexTitle4.show()
            self.flexLabel4.setText(str(self.user.getYearsOfExperience()))
            self.flexLabel4.show()
            self.flexTitle5.setText("Assigned Clinic")
            self.flexTitle5.show()
            self.flexLabel5.setText(self.user.getClinicID())
            self.flexLabel5.show()
            self.statusLabel.setText(self.user.getStatus())
            self.statusLabel.show()