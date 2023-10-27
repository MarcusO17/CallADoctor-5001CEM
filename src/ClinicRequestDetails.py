import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QMessageBox
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .AssignDoctorDialog import AssignDoctorDialog
from .model import Appointment, Clinic
from .PageManager import PageManager


class ClinicRequestDetails(QMainWindow):

    def __init__(self, request, clinic):
        super().__init__()

        # set the information here
        self.request = request #appointmentObject
        self.clinic = clinic
        self.pageManager = PageManager()
        self.setWindowTitle("Request Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
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
        self.headerTitle.setText(self.request.getAppointmentID())
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

        self.requestReasonLabel = QLabel(self.centralwidget)
        self.requestReasonLabel.setGeometry(QRect(180, 220, 400, 300))
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.requestReasonLabel.setFont(font)
        self.requestReasonLabel.setText(self.request.getVisitReason())
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QRect(700, 220, 150, 40))
        self.dateLabel.setFont(font)
        self.dateLabel.setText(str(self.request.getAppointmentDate()))
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QRect(700, 280, 150, 40))
        self.timeLabel.setFont(font)
        self.timeLabel.setText(self.request.getStartTime())
        self.timeLabel.setFrameShape(QtWidgets.QFrame.Box)

        self.assignedDoctorLabel = QLabel(self.centralwidget)
        self.assignedDoctorLabel.setGeometry(QRect(700, 350, 150, 40))
        self.assignedDoctorLabel.setText(self.request.getDoctorID())

        self.assignDoctorButton = QPushButton(self.centralwidget)
        self.assignDoctorButton.setGeometry(QRect(710, 400, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.assignDoctorButton.setFont(font)
        self.assignDoctorButton.setLayoutDirection(Qt.LeftToRight)
        self.assignDoctorButton.setText("Assign Doctor")
        self.assignDoctorButton.setStyleSheet("padding-left: 30px;")
        self.assignDoctorButton.clicked.connect(self.assignDoctorFunction)

        self.assignDoctorLabel = QLabel(self.centralwidget)
        self.assignDoctorLabel.setGeometry(QRect(730, 425, 50, 50))
        self.assignDoctorLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.assignDoctorIcon = QPixmap(filepath)
        self.assignDoctorIcon = self.assignDoctorIcon.scaled(50, 50)
        self.assignDoctorLabel.setPixmap(self.assignDoctorIcon)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QRect(180, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.cancelButton.setFont(font)
        self.cancelButton.setLayoutDirection(Qt.LeftToRight)
        self.cancelButton.setText("Cancel Request")
        self.cancelButton.setStyleSheet("padding-left: 50px;")
        self.cancelButton.clicked.connect(self.cancelRequestFunction)

        self.cancelButtonLabel = QLabel(self.centralwidget)
        self.cancelButtonLabel.setGeometry(QRect(200, 570, 50, 50))
        self.cancelButtonLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.cancelButtonIcon = QPixmap(filepath)
        self.cancelButtonIcon = self.cancelButtonIcon.scaled(50, 50)
        self.cancelButtonLabel.setPixmap(self.cancelButtonIcon)

        self.acceptButton = QPushButton(self.centralwidget)
        self.acceptButton.setGeometry(QRect(710, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.acceptButton.setFont(font)
        self.acceptButton.setLayoutDirection(Qt.LeftToRight)
        self.acceptButton.setText("Accept Request")
        self.acceptButton.setStyleSheet("padding-left: 50px;")
        self.acceptButton.clicked.connect(self.acceptRequestFunction)

        self.acceptButtonLabel = QLabel(self.centralwidget)
        self.acceptButtonLabel.setGeometry(QRect(730, 570, 50, 50))
        self.acceptButtonLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.acceptButtonIcon = QPixmap(filepath)
        self.acceptButtonIcon = self.acceptButtonIcon.scaled(50, 50)
        self.acceptButtonLabel.setPixmap(self.acceptButtonIcon)


        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(20)

        self.requestContainer = QLabel(self.centralwidget)
        self.requestContainer.setFixedSize(1000, 500)
        self.requestContainer.setFrameShape(QtWidgets.QFrame.Box)

        self.acceptButton.raise_()
        self.acceptButtonLabel.raise_()
        self.cancelButton.raise_()
        self.cancelButtonLabel.raise_()
        self.assignDoctorButton.raise_()
        self.assignDoctorLabel.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.requestContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def backButtonFunction(self):
        backConfirmationDialogBox = QMessageBox.question(self.centralwidget, "Back Confirmation",
                                                      "Are you sure you want to back from this request, you may continue later.",
                                                      QMessageBox.Yes | QMessageBox.No)
        if backConfirmationDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()


    def acceptRequestFunction(self):
        acceptRequestDialogBox = QMessageBox.question(self.centralwidget, "Request Confirmation",
                                                      "Are you sure you want to approve this request",
                                                      QMessageBox.Yes | QMessageBox.No)
        if acceptRequestDialogBox == QMessageBox.Yes:
            if self.request.getDoctorID() == "":
                print("NO DOCTOR ASSIGNED")
                noDoctorValidationDialogBox = QMessageBox(self.centralwidget)
                noDoctorValidationDialogBox.setIcon(QMessageBox.Critical)
                noDoctorValidationDialogBox.setText("No Doctor Assigned")
                noDoctorValidationDialogBox.setInformativeText("Please Assign a Doctor before Approving")
                noDoctorValidationDialogBox.setWindowTitle("Validation Error")
                noDoctorValidationDialogBox.exec_()
            else:
                response, isSuccess = self.request.assignDoctorAppointment(self.request.doctorID) 
                if isSuccess == True:
                    print(response)
                else:
                    print('Failed!')
                self.pageManager.getPreviousPage().generateRequestButtons()
                self.pageManager.goBack()

    def cancelRequestFunction(self):
        cancelRequestDialogBox = QMessageBox.question(self.centralwidget, "Request Cancel Confirmation",
                                               "Are you sure you want to cancel this request",
                                               QMessageBox.Yes | QMessageBox.No)
        if cancelRequestDialogBox == QMessageBox.Yes:
            self.request.cancelAppointment()
            self.pageManager.getPreviousPage().generateRequestButtons()
            self.pageManager.goBack()

    def assignDoctorFunction(self):
        self.assignDoctorDialog = AssignDoctorDialog(self)
        self.assignDoctorDialog.setData(self.request)
        print("FINISHED SETTING REQUEST")
        self.assignDoctorDialog.exec_()

        self.assignedDoctorLabel.setText(self.request.getDoctorID())

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Clinic", self.clinic)
        self.pageManager.add(self.accountPage)
       