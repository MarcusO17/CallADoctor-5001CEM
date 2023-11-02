import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Clinic
from .PageManager import PageManager



class AdminViewClinicDetailsWindow(QMainWindow):

    def __init__(self, clinicTemp):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        print(self.clinic.getClinicID(), self.clinic.getClinicName(), self.clinic.getClinicAddress(), self.clinic.getClinicContact())
        self.setWindowTitle("Clinic Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("clinic_details")
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
        self.headerTitle.setText(self.clinic.getClinicName())
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")


        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.adminClinicDetailsPictureLabel = QLabel(self.centralwidget)
        self.adminClinicDetailsPictureLabel.setGeometry(QRect(180, 220, 400, 200))
        self.adminClinicDetailsPictureLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.adminClinicDetailsPicture = QPixmap(filepath)
        self.adminClinicDetailsPictureLabel.setPixmap(self.adminClinicDetailsPicture)

        self.adminClinicDetailsDescriptionLabel = QLabel(self.centralwidget)
        self.adminClinicDetailsDescriptionLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicDetailsDescriptionLabel.setFont(font)
        self.adminClinicDetailsDescriptionLabel.setText(self.clinic.getClinicName()+ "\n" + self.clinic.getClinicContact()+ "\n" + self.clinic.getClinicID())
        self.adminClinicDetailsDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.adminClinicDetailsAddressLabel = QLabel(self.centralwidget)
        self.adminClinicDetailsAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicDetailsAddressLabel.setFont(font)
        self.adminClinicDetailsAddressLabel.setText(self.clinic.getClinicAddress())
        self.adminClinicDetailsAddressLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.adminRemoveClinicButton = QPushButton(self.centralwidget)
        self.adminRemoveClinicButton.setGeometry(QRect(710, 545, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.adminRemoveClinicButton.setFont(font)
        self.adminRemoveClinicButton.setLayoutDirection(Qt.LeftToRight)
        self.adminRemoveClinicButton.setText("Remove Clinic")
        self.adminRemoveClinicButton.clicked.connect(self.adminRemoveClinicFunction)
        self.adminRemoveClinicButton.raise_()

        self.adminRemoveClinicLabel = QLabel(self.centralwidget)
        self.adminRemoveClinicLabel.setGeometry(QRect(730, 570, 50, 50))
        self.adminRemoveClinicLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.adminRemoveClinicIcon = QPixmap(filepath)
        self.adminRemoveClinicIcon = self.adminRemoveClinicIcon.scaled(50, 50)
        self.adminRemoveClinicLabel.setPixmap(self.adminRemoveClinicIcon)

        self.adminClinicDetailsContainer = QLabel(self.centralwidget)
        self.adminClinicDetailsContainer.setFixedSize(1000,500)
        self.adminClinicDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.adminClinicDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def adminRemoveClinicFunction(self):
        adminClinicRemoveDialogBox = QMessageBox.question(self.centralwidget, "Removal Confirmation", 
                                                          "Are you sure you want to remove this Clinic?",
                                               QMessageBox.Yes | QMessageBox.No)
        if adminClinicRemoveDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()