import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QMessageBox, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .AssignDoctorDialog import AssignDoctorDialog
from .model import Appointment, Clinic, Doctor
from .PageManager import PageManager, FrameLayoutManager


class ClinicRequestDetails(QWidget):

    def __init__(self, request, clinic):
        super().__init__()

        # set the information here
        self.request = request #appointmentObject
        self.clinic = clinic
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
        self.headerTitle.setText(f"{self.request.getAppointmentID()} Details")
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

        self.requestReasonTitle = QLabel(self.centralwidget)
        self.requestReasonTitle.setGeometry(QRect(50, 190, 150, 40))
        self.requestReasonTitle.setText("Request Reason: ")

        self.requestReasonLabel = QLabel(self.centralwidget)
        self.requestReasonLabel.setGeometry(QRect(50, 220, 400, 200))
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.requestReasonLabel.setFont(font)
        self.requestReasonLabel.setText(self.request.getVisitReason())
        self.requestReasonLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.requestReasonLabel.setWordWrap(True)
        self.requestReasonLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.requestReasonLabel.setStyleSheet("""QLabel {
                                                    border-radius: 10px;
                                                    border: 1px solid black;
                                                    background: white;
                                                    }""")
        self.dateTitle = QLabel(self.centralwidget)
        self.dateTitle.setGeometry(QRect(500, 190, 150, 40))
        self.dateTitle.setText("Date: ")

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QRect(500, 220, 150, 40))
        self.dateLabel.setFont(font)
        self.dateLabel.setText(str(self.request.getAppointmentDate()))
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.dateLabel.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")

        self.timeTitle = QLabel(self.centralwidget)
        self.timeTitle.setGeometry(QRect(700, 190, 150, 40))
        self.timeTitle.setText("Start Time: ")

        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QRect(700, 220, 150, 40))
        self.timeLabel.setFont(font)
        self.timeLabel.setText(self.request.getStartTime())
        self.timeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.timeLabel.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")

        self.assignedDoctorTitle = QLabel(self.centralwidget)
        self.assignedDoctorTitle.setGeometry(QRect(500, 270, 150, 40))
        self.assignedDoctorTitle.setText("Assigned Doctor: ")

        self.assignedDoctorLabel = QLabel(self.centralwidget)
        self.assignedDoctorLabel.setGeometry(QRect(500, 300, 350, 40))
        self.assignedDoctorLabel.setFont(font)
        if len(self.request.getDoctorID()) == 0:
            assignedDoctor = "None"
        else:
            doctor = Doctor.getDoctorfromID(self.request.getDoctorID())
            assignedDoctor = doctor.getDoctorName()
        self.assignedDoctorLabel.setText(assignedDoctor)
        self.assignedDoctorLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.assignedDoctorLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

        self.assignDoctorButton = QPushButton(self.centralwidget)
        self.assignDoctorButton.setGeometry(QRect(550, 400, 325, 100))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        self.assignDoctorButton.setFont(font)
        self.assignDoctorButton.setLayoutDirection(Qt.LeftToRight)
        self.assignDoctorButton.setText("   Assign Doctor")
        self.assignDoctorButton.clicked.connect(self.assignDoctorFunction)
        self.assignDoctorButton.setStyleSheet("""QPushButton {
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

        self.assignDoctorLabel = QLabel(self.centralwidget)
        self.assignDoctorLabel.setGeometry(QRect(570, 425, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-doctor-64.png")
        self.assignDoctorIcon = QPixmap(filepath)
        self.assignDoctorIcon = self.assignDoctorIcon.scaled(50, 50)
        self.assignDoctorLabel.setPixmap(self.assignDoctorIcon)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QRect(50, 530, 325, 100))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        self.cancelButton.setFont(font)
        self.cancelButton.setLayoutDirection(Qt.LeftToRight)
        self.cancelButton.setText("   Cancel Request")
        self.cancelButton.clicked.connect(self.cancelRequestFunction)
        self.cancelButton.setStyleSheet("""QPushButton {
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

        self.cancelButtonLabel = QLabel(self.centralwidget)
        self.cancelButtonLabel.setGeometry(QRect(70, 555, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-remove-64.png")
        self.cancelButtonIcon = QPixmap(filepath)
        self.cancelButtonIcon = self.cancelButtonIcon.scaled(50, 50)
        self.cancelButtonLabel.setPixmap(self.cancelButtonIcon)


        self.acceptButton = QPushButton(self.centralwidget)
        self.acceptButton.setGeometry(QRect(550, 530, 325, 100))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        self.acceptButton.setFont(font)
        self.acceptButton.setLayoutDirection(Qt.LeftToRight)
        self.acceptButton.setText("    Accept Request")
        self.acceptButton.clicked.connect(self.acceptRequestFunction)
        self.acceptButton.setStyleSheet("""QPushButton {
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

        self.acceptButtonLabel = QLabel(self.centralwidget)
        self.acceptButtonLabel.setGeometry(QRect(570, 555, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-add-64.png")
        self.acceptButtonIcon = QPixmap(filepath)
        self.acceptButtonIcon = self.acceptButtonIcon.scaled(50, 50)
        self.acceptButtonLabel.setPixmap(self.acceptButtonIcon)

        self.acceptButton.raise_()
        self.acceptButtonLabel.raise_()
        self.cancelButton.raise_()
        self.cancelButtonLabel.raise_()
        self.assignDoctorButton.raise_()
        self.assignDoctorLabel.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)
    def backButtonFunction(self):
        backConfirmationDialogBox = QMessageBox.question(self.centralwidget, "Back Confirmation",
                                                      "Are you sure you want to back from this request, you may continue later.",
                                                      QMessageBox.Yes | QMessageBox.No)
        if backConfirmationDialogBox == QMessageBox.Yes:
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

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
                self.frameLayoutManager = FrameLayoutManager()
                self.frameLayout = self.frameLayoutManager.getFrameLayout()

                self.frameLayoutManager.back()
                self.frameLayout.widget(self.frameLayoutManager.top()).generateRequestButtons()
                self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def cancelRequestFunction(self):
        cancelRequestDialogBox = QMessageBox.question(self.centralwidget, "Request Cancel Confirmation",
                                               "Are you sure you want to cancel this request",
                                               QMessageBox.Yes | QMessageBox.No)
        if cancelRequestDialogBox == QMessageBox.Yes:
            self.request.cancelAppointment()
            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.widget(self.frameLayoutManager.top()).generateRequestButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def assignDoctorFunction(self):
        self.assignDoctorDialog = AssignDoctorDialog(self)
        self.assignDoctorDialog.setData(self.request)
        print("FINISHED SETTING REQUEST")
        self.assignDoctorDialog.exec_()

        if len(self.request.getDoctorID()) == 0:
            assignedDoctor = "None"
        else:
            doctor = Doctor.getDoctorfromID(self.request.getDoctorID())
            assignedDoctor = doctor.getDoctorName()

        self.assignedDoctorLabel.setText(assignedDoctor)

       