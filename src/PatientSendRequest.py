import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QDate, QTime, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QLineEdit, QComboBox, QDateEdit, QMessageBox, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Clinic
from .model import Appointment
from .PageManager import PageManager, FrameLayoutManager


class PatientSendRequest(QWidget):

    def __init__(self, clinic, patient):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinic
        self.patient = patient
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        self.timeList = list()

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(self.clinic.getClinicName() + " - Send Request")
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

        self.requestPurposeTitle = QLabel(self.centralwidget)
        self.requestPurposeTitle.setGeometry(QRect(50, 160, 150, 40))
        self.requestPurposeTitle.setText("Request Purpose: ")

        self.requestPurpose = QLineEdit(self.centralwidget)
        self.requestPurpose.setGeometry(QRect(50, 190, 400, 200))
        self.requestPurpose.setAlignment(Qt.AlignTop)
        self.requestPurpose.setPlaceholderText("Enter the Purpose of Request")

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setText("Date: ")
        self.dateLabel.setGeometry(QRect(50, 450, 150, 40))
        self.preferredDate = QDateEdit(self.centralwidget)
        self.preferredDate.setDate(QDate.currentDate())
        self.preferredDate.setDisplayFormat("yyyy-MM-dd")
        self.preferredDate.setMinimumDate(QDate.currentDate())
        self.preferredDate.setGeometry(QRect(50, 490, 150, 40))
        self.preferredDate.dateChanged.connect(self.updateTimeslot)
        self.maxDate = QDate.currentDate().addMonths(1)
        self.preferredDate.setMaximumDate(self.maxDate)

        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setText("Time: ")
        self.timeLabel.setGeometry(QRect(300, 450, 150, 40))
        self.preferredTimeComboBox = QComboBox(self.centralwidget)

        self.preferredTimeComboBox.addItems(self.timeList)
        self.preferredTimeComboBox.setGeometry(QRect(300, 490, 150, 40))
        self.updateTimeslot()

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-send-file-30.png")
        self.submitButtonIcon = QIcon(filepath)

        self.submitButton = QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QRect(520, 545, 275, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.submitButton.setFont(font)
        self.submitButton.setLayoutDirection(Qt.LeftToRight)
        self.submitButton.setText("    Submit")
        self.submitButton.setIconSize(QSize(50, 50))
        self.submitButton.setIcon(self.submitButtonIcon)
        self.submitButton.clicked.connect(self.sendRequestFunction)
        self.submitButton.setStyleSheet("""QPushButton {
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

        # self.submitButtonLabel.setGeometry(QRect(540, 570, 50, 50))
        self.requestPurpose.raise_()
        self.preferredTimeComboBox.raise_()
        self.preferredDate.raise_()
        self.submitButton.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)


    def sendRequestFunction(self):
        # generate an appointmentID
        backDialogBox = QMessageBox.question(self.centralwidget, "Submit Confirmation",
                                             "Do you want to submit this request",
                                             QMessageBox.Yes | QMessageBox.No)
        if backDialogBox == QMessageBox.Yes:
            timeTemp = self.preferredTimeComboBox.currentText().split(":")
            endTime = QTime(int(timeTemp[0]), int(timeTemp[1])).addSecs(3600)

            # back end magic here
            appointment = Appointment("0", 
                                      "",
                                      self.clinic.getClinicID(), 
                                      self.patient.getPatientID(),
                                      "Pending",
                                       self.preferredTimeComboBox.currentText(),
                                       endTime.toString("hh:mm:ss"),
                                       self.preferredDate.date().toString("yyyy-MM-dd"), 
                                       self.requestPurpose.text())
            
            result, isSuccess = Appointment.postAppointment(appointment)
            if isSuccess:
                print(result)
            else:
                print('failed!')

            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def updateTimeslot(self):
        # rounding current time + adding 3 hours to current time
        nextDay = False
        print("running updatetimeslot")
        self.timeList.clear()
        currentTime = QTime.currentTime()
        roundedTime = QTime(currentTime.hour(), 0)
        print(roundedTime.toString())
        roundedTime = roundedTime.addSecs(10800)

        # check if the added 3 hours made it go to the next day
        if roundedTime.hour() < currentTime.hour():
            nextDay = True

        print(roundedTime.toString())
        timeDiff = roundedTime.secsTo(QTime(15, 0))

        print(timeDiff)
        hoursLeft = timeDiff // 3600
        print(hoursLeft)
        startTime = QTime(8, 0)
       

        if nextDay == True:
            self.preferredDate.setDate(QDate.currentDate().addDays(1))
            self.preferredDate.setMinimumDate(QDate.currentDate().addDays(1))
            self.timeList.clear()
            for hour in range(8):
                self.timeList.append(startTime.addSecs(3600 * hour).toString("hh:mm"))
                print(self.timeList)

        elif self.preferredDate.date() == QDate.currentDate():
            if roundedTime > QTime(15, 0):
                self.preferredDate.setDate(QDate.currentDate().addDays(1))
                self.preferredDate.setMinimumDate(QDate.currentDate().addDays(1))
                self.timeList.clear()
                for hour in range(8):
                    self.timeList.append(startTime.addSecs(3600 * hour).toString("hh:mm"))
                    print(self.timeList)
            elif roundedTime < QTime(8, 0):
                for hour in range(8):
                    self.timeList.append(startTime.addSecs(3600 * hour).toString("hh:mm"))
                    print(self.timeList)
            else:
                self.timeList.clear()
                for hour in range(hoursLeft):
                    self.timeList.append(roundedTime.addSecs(3600 * hour).toString("hh:mm"))
                    print(self.timeList)
        else:
            self.timeList.clear()
            for hour in range(8):
                self.timeList.append(startTime.addSecs(3600 * hour).toString("hh:mm"))


        print("FINISHED", self.timeList)

        self.preferredTimeComboBox.clear()
        self.preferredTimeComboBox.addItems(self.timeList)

    def backButtonFunction(self):

        backDialogBox = QMessageBox.question(self.centralwidget, "Discard Confirmation",
                                               "Do you want to discard this request",
                                               QMessageBox.Yes | QMessageBox.No)
        if backDialogBox == QMessageBox.Yes:
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
