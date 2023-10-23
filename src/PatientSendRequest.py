import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QDate, QTime
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QLineEdit, QComboBox, QDateEdit, QMessageBox
from PyQt5 import QtWidgets
from .model import Clinic
from .model import Appointment
from .PageManager import PageManager



class PatientSendRequest(QMainWindow):

    def __init__(self, clinic, patient):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinic
        self.patient = patient
        print(self.clinic.getClinicID(), self.clinic.getClinicName(), self.clinic.getClinicAddress(), self.clinic.getClinicContact())
        self.setWindowTitle("Clinics Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("clinic_details")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        self.timeList = list()

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
        self.headerTitle.setText(self.clinic.getClinicName() + " - Send Request")
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
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.requestPurpose = QLineEdit(self.centralwidget)
        self.requestPurpose.setGeometry(QRect(180, 220, 400, 200))
        self.requestPurpose.setAlignment(Qt.AlignTop)
        self.requestPurpose.setPlaceholderText("Enter the Purpose of Request")

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setText("Date: ")
        self.dateLabel.setGeometry(QRect(180, 450, 150, 40))
        self.preferredDate = QDateEdit(self.centralwidget)
        self.preferredDate.setDate(QDate.currentDate())
        self.preferredDate.setDisplayFormat("yyyy-MM-dd")
        self.preferredDate.setMinimumDate(QDate.currentDate())
        self.preferredDate.setGeometry(QRect(180, 490, 150, 40))
        self.preferredDate.dateChanged.connect(self.updateTimeslot)
        self.maxDate = QDate.currentDate().addMonths(1)
        self.preferredDate.setMaximumDate(self.maxDate)

        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setText("Time: ")
        self.timeLabel.setGeometry(QRect(400, 450, 150, 40))
        self.preferredTimeComboBox = QComboBox(self.centralwidget)

        self.preferredTimeComboBox.addItems(self.timeList)
        self.preferredTimeComboBox.setGeometry(QRect(400, 490, 150, 40))
        self.updateTimeslot()

        self.submitButton = QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QRect(710, 545, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.submitButton.setFont(font)
        self.submitButton.setLayoutDirection(Qt.LeftToRight)
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.sendRequestFunction)

        self.submitButtonLabel = QLabel(self.centralwidget)
        self.submitButtonLabel.setGeometry(QRect(730, 570, 50, 50))
        self.submitButtonLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.submitButtonIcon = QPixmap(filepath)
        self.submitButtonIcon = self.submitButtonIcon.scaled(50, 50)
        self.submitButtonLabel.setPixmap(self.submitButtonIcon)

        self.clinicDetailsContainer = QLabel(self.centralwidget)
        self.clinicDetailsContainer.setFixedSize(1000,500)
        self.clinicDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)
        self.requestPurpose.raise_()
        self.preferredTimeComboBox.raise_()
        self.preferredDate.raise_()
        self.submitButton.raise_()
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.clinicDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def sendRequestFunction(self):
        # generate an appointmentID
        backDialogBox = QMessageBox.question(self.centralwidget, "Submit Confirmation",
                                             "Do you want to submit this request",
                                             QMessageBox.Yes | QMessageBox.No)
        if backDialogBox == QMessageBox.Yes:
            timeTemp = self.preferredTimeComboBox.currentText().split(":")
            endTime = QTime(int(timeTemp[0]), int(timeTemp[1])).addSecs(3600)

            # back end magic here
            appointment = Appointment("appointmentID HERE", "", self.patient.getPatientID(),"Pending",
                                        self.preferredTimeComboBox.currentText(),endTime.toString("hh:mm"),self.preferredDate.date().toString("yyyy-MM-dd"), self.requestPurpose.text())

            print(appointment.getAppointmentID(),appointment.getAppointmentDate(),appointment.getAppointmentStatus(),appointment.getStartTime(),
                  appointment.getEndTime(), appointment.getVisitReason())

            self.pageManager.goBack()



    def updateTimeslot(self):
        # rounding current time + adding 3 hours to current time
        print("running updatetimeslot")
        self.timeList.clear()
        currentTime = QTime.currentTime()
        roundedTime = QTime(currentTime.hour(), 0)
        roundedTime = roundedTime.addSecs(10800)
        timeDiff = roundedTime.secsTo(QTime(17, 0))
        hoursLeft = timeDiff // 3600
        startTime = QTime(8, 0)
        print(timeDiff)
        print(hoursLeft)
        print(roundedTime)

        if self.preferredDate.date() == QDate.currentDate():
            if currentTime > QTime(17, 0):
                self.preferredDate.setDate(QDate.currentDate().addDays(1))
                self.preferredDate.setMinimumDate(QDate.currentDate().addDays(1))
                self.timeList.clear()
                for hour in range(9):
                    self.timeList.append(startTime.addSecs(3600 * hour).toString("hh:mm"))
                    print(self.timeList)
            else:
                self.timeList.clear()
                self.timeList.append(roundedTime.toString("hh:mm"))
                for hour in range(hoursLeft):
                    self.timeList.append(roundedTime.addSecs(3600 * hour).toString("hh:mm"))
                    print(self.timeList)
        else:
            self.timeList.clear()
            for hour in range(9):
                self.timeList.append(startTime.addSecs(3600 * hour).toString("hh:mm"))


        print("FINISHED", self.timeList)

        self.preferredTimeComboBox.clear()
        self.preferredTimeComboBox.addItems(self.timeList)

    def backButtonFunction(self):

        backDialogBox = QMessageBox.question(self.centralwidget, "Discard Confirmation",
                                               "Do you want to discard this request",
                                               QMessageBox.Yes | QMessageBox.No)
        if backDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()