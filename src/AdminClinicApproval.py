import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Clinic
from .PageManager import PageManager



class AdminClinicApprovalWindow(QMainWindow):

    def __init__(self, clinicTemp):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        print(self.clinic.getClinicID(), self.clinic.getClinicName(), self.clinic.getClinicAddress(), self.clinic.getClinicContact(), self.clinic.getApprovalStatus())
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

        self.adminClinicApprovalPictureLabel = QLabel(self.centralwidget)
        self.adminClinicApprovalPictureLabel.setGeometry(QRect(180, 220, 400, 200))
        self.adminClinicApprovalPictureLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.adminClinicApprovalPicture = QPixmap(filepath)
        self.adminClinicApprovalPictureLabel.setPixmap(self.adminClinicApprovalPicture)

        self.adminClinicApprovalDescriptionLabel = QLabel(self.centralwidget)
        self.adminClinicApprovalDescriptionLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicApprovalDescriptionLabel.setFont(font)
        self.adminClinicApprovalDescriptionLabel.setText(self.clinic.getClinicName()+ "\n" + self.clinic.getClinicContact()+ "\n" + self.clinic.getClinicID())
        self.adminClinicApprovalDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.adminClinicApprovalAddressLabel = QLabel(self.centralwidget)
        self.adminClinicApprovalAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicApprovalAddressLabel.setFont(font)
        self.adminClinicApprovalAddressLabel.setText(self.clinic.getClinicAddress())
        self.adminClinicApprovalAddressLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.adminApproveClinicButton = QPushButton(self.centralwidget)
        self.adminApproveClinicButton.setGeometry(QRect(710, 545, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.adminApproveClinicButton.setFont(font)
        self.adminApproveClinicButton.setLayoutDirection(Qt.LeftToRight)
        self.adminApproveClinicButton.setText("Approve Clinic")
        self.adminApproveClinicButton.clicked.connect(self.adminApproveClinicFunction)
        self.adminApproveClinicButton.raise_()

        self.adminApproveClinicLabel = QLabel(self.centralwidget)
        self.adminApproveClinicLabel.setGeometry(QRect(730, 570, 50, 50))
        self.adminApproveClinicLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.adminApproveClinicIcon = QPixmap(filepath)
        self.adminApproveClinicIcon = self.adminApproveClinicIcon.scaled(50, 50)
        self.adminApproveClinicLabel.setPixmap(self.adminApproveClinicIcon)

        self.adminClinicApprovalContainer = QLabel(self.centralwidget)
        self.adminClinicApprovalContainer.setFixedSize(1000,500)
        self.adminClinicApprovalContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.adminClinicApprovalContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def adminApproveClinicFunction(self):
        adminClinicApproveDialogBox = QMessageBox.question(self.centralwidget, "Removal Confirmation", 
                                                          "Are you sure you want to remove this Clinic?",
                                               QMessageBox.Yes | QMessageBox.No)
        if adminClinicApproveDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()