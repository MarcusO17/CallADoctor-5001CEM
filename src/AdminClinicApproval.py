import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Clinic
from .PageManager import PageManager



class AdminClinicApprovalWindow(QMainWindow):

    def __init__(self, clinicTemp, adminID):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        self.adminID = adminID
        self.setWindowTitle("Clinic Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("clinic_details")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # header (probably reused in most files)
        self.topLeftLogo = QLabel(self.centralWidget)
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.headerTitle = QLabel(self.centralWidget)
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
        self.backButton = QPushButton(self.centralWidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.adminClinicApprovalPictureLabel = QLabel(self.centralWidget)
        self.adminClinicApprovalPictureLabel.setGeometry(QRect(180, 220, 400, 200))
        self.adminClinicApprovalPictureLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicApprovalPicture = QPixmap.fromImage(QImage.fromData(self.clinic.getCertification()))
        self.adminClinicApprovalPictureLabel.setPixmap(self.adminClinicApprovalPicture)

        self.adminClinicApprovalDescriptionLabel = QLabel(self.centralWidget)
        self.adminClinicApprovalDescriptionLabel.setGeometry(QRect(700, 220, 375, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicApprovalDescriptionLabel.setFont(font)
        self.adminClinicApprovalDescriptionLabel.setText(f"Clinic ID: {self.clinic.getClinicID()} \n Clinic Name: {self.clinic.getClinicName()} \n Clinic Status: {self.clinic.getClinicStatus()}")
        self.adminClinicApprovalDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.adminClinicApprovalAddressLabel = QLabel(self.centralWidget)
        self.adminClinicApprovalAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicApprovalAddressLabel.setFont(font)
        self.adminClinicApprovalAddressLabel.setText(self.clinic.getClinicAddress())
        self.adminClinicApprovalAddressLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.adminApproveClinicButton = QPushButton(self.centralWidget)
        self.adminApproveClinicButton.setGeometry(QRect(790, 450, 280, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.adminApproveClinicButton.setFont(font)
        self.adminApproveClinicButton.setLayoutDirection(Qt.LeftToRight)
        self.adminApproveClinicButton.setText("Approve Clinic")
        self.adminApproveClinicButton.clicked.connect(self.adminApproveClinicFunction)
        self.adminApproveClinicButton.raise_()

        self.adminApproveClinicLabel = QLabel(self.centralWidget)
        self.adminApproveClinicLabel.setGeometry(QRect(810, 475, 50, 50))
        self.adminApproveClinicLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.adminApproveClinicIcon = QPixmap(filepath)
        self.adminApproveClinicIcon = self.adminApproveClinicIcon.scaled(50, 50)
        self.adminApproveClinicLabel.setPixmap(self.adminApproveClinicIcon)

        self.adminDisapproveClinicButton = QPushButton(self.centralWidget)
        self.adminDisapproveClinicButton.setGeometry(QRect(790, 565, 280, 100))
        self.adminDisapproveClinicButton.setFont(font)
        self.adminDisapproveClinicButton.setLayoutDirection(Qt.RightToLeft)
        self.adminDisapproveClinicButton.setText("Request Cancel")
        self.adminDisapproveClinicButton.clicked.connect(self.adminDisapproveClinicFunction)

        self.adminDisapproveClinicLabel = QLabel(self.centralWidget)
        self.adminDisapproveClinicLabel.setGeometry(QRect(810, 590, 50, 50))
        self.adminDisapproveClinicLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminDisapproveClinicIcon = QPixmap.fromImage(QImage.fromData(self.clinic.getCertification()))
        self.adminDisapproveClinicIcon = self.adminDisapproveClinicIcon.scaled(50, 50)
        self.adminDisapproveClinicLabel.setPixmap(self.adminDisapproveClinicIcon)


        self.adminClinicApprovalContainer = QLabel(self.centralWidget)
        self.adminClinicApprovalContainer.setFixedSize(1000,500)
        self.adminClinicApprovalContainer.setFrameShape(QtWidgets.QFrame.Box)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.adminClinicApprovalContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.adminDisapproveClinicButton.raise_()
        self.adminApproveClinicButton.raise_()

        self.centralWidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def adminApproveClinicFunction(self):
        adminApproveClinicDialogBox = QMessageBox.question(self.centralWidget, "Approval Confirmation", 
                                                          "Are you sure you want to Approve this Clinic?",
                                               QMessageBox.Yes | QMessageBox.No)
        if adminApproveClinicDialogBox == QMessageBox.Yes:
            self.clinic.approve()
            print(self.clinic.getClinicStatus())
            self.pageManager.getPreviousPage().generateViewApprovalButtons()
            self.pageManager.goBack()

    def adminDisapproveClinicFunction(self):
        adminDisapproveClinicDialogBox = QMessageBox.question(self.centralWidget, "Disapproval Confirmation",
                                                          "Are you sure you want to disapprove this Clinic?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if adminDisapproveClinicDialogBox == QMessageBox.Yes:
            self.clinic.cancel()
            self.pageManager.getPreviousPage().generateViewApprovalButtons()
            print(self.clinic.getClinicStatus())
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()