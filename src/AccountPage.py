import os
import sys
import requests
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QLineEdit, QGraphicsDropShadowEffect
from PyQt5 import QtCore, QtWidgets
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager


class AccountPage(QWidget):

    def __init__(self):
        super().__init__()
        self.pageManager = PageManager()
        # set the information here
        self.user = None
        self.setWindowTitle("Account Page")
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QWidget()

        self.mode = None

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Account Page")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setGeometry(QRect(80, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.informationBox = QLabel(self.centralwidget)
        self.informationBox.setGeometry(QRect(50, 130, 850, 530))
        self.informationBox.setStyleSheet("""QLabel {
                                                background: #D0BFFF;
                                                border-radius: 10px;
                                                }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.informationBox.setGraphicsEffect(effect)

        self.nameTitle = QLabel(self.centralwidget)
        self.nameTitle.setGeometry(QRect(80, 150, 350, 30))
        self.nameTitle.setText("Name: ")

        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QRect(80, 180, 350, 50))
        self.nameLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.nameLabel.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")

        self.iDTitle = QLabel(self.centralwidget)
        self.iDTitle.setGeometry(QRect(80, 230, 350, 30))
        self.iDTitle.setText("ID: ")

        self.iDLabel = QLabel(self.centralwidget)
        self.iDLabel.setGeometry(QRect(80, 260, 350, 50))
        self.iDLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.iDLabel.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")

        self.flexTitle1 = QLabel(self.centralwidget)
        self.flexTitle1.setGeometry(QRect(80, 310, 350, 30))
        self.flexTitle1.hide()

        self.flexLabel1 = QLabel(self.centralwidget)
        self.flexLabel1.setGeometry(QRect(80, 340, 350, 50))
        self.flexLabel1.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel1.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")
        self.flexLabel1.hide()

        self.flexTitle2 = QLabel(self.centralwidget)
        self.flexTitle2.setGeometry(QRect(80, 390, 350, 30))
        self.flexTitle2.hide()

        self.flexLabel2 = QLabel(self.centralwidget)
        self.flexLabel2.setGeometry(QRect(80, 420, 350, 50))
        self.flexLabel2.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel2.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")
        self.flexLabel2.hide()

        self.flexTitle3 = QLabel(self.centralwidget)
        self.flexTitle3.setGeometry(QRect(80, 470, 350, 30))
        self.flexTitle3.hide()

        self.flexLabel3 = QLabel(self.centralwidget)
        self.flexLabel3.setGeometry(QRect(80, 500, 350, 50))
        self.flexLabel3.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel3.setStyleSheet("""QLabel {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")
        self.flexLabel3.hide()

        self.flexTitle4 = QLabel(self.centralwidget)
        self.flexTitle4.setGeometry(QRect(80, 550, 350, 30))
        self.flexTitle4.hide()

        self.flexLabel4 = QLabel(self.centralwidget)
        self.flexLabel4.setGeometry(QRect(80, 580, 350, 50))
        self.flexLabel4.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel4.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")
        self.flexLabel4.hide()

        self.flexTitle5 = QLabel(self.centralwidget)
        self.flexTitle5.setGeometry(QRect(500, 140, 350, 30))
        self.flexTitle5.hide()

        self.flexLabel5 = QLabel(self.centralwidget)
        self.flexLabel5.setGeometry(QRect(500, 170, 350, 50))
        self.flexLabel5.setFrameShape(QtWidgets.QFrame.Box)
        self.flexLabel5.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")
        self.flexLabel5.hide()

        self.addressTitle = QLabel(self.centralwidget)
        self.addressTitle.setGeometry(QRect(500, 150, 400, 30))
        self.addressTitle.setText("Address: ")
        self.addressTitle.hide()

        self.addressLabel = QLineEdit(self.centralwidget)
        self.addressLabel.setGeometry(QRect(500, 180, 350, 200))
        self.addressLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.addressLabel.setDisabled(True)
        self.addressLabel.hide()

        self.statusTitle = QLabel(self.centralwidget)
        self.statusTitle.setText("Status: ")
        self.statusTitle.setGeometry(QRect(500, 390, 350, 50))

        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.statusLabel.setGeometry(QRect(500, 420, 350, 50))
        self.statusLabel.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")
        self.statusLabel.hide()

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setGeometry(QRect(520, 495, 280, 100))
        self.editButton.setLayoutDirection(Qt.RightToLeft)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.editButton.setFont(font)
        self.editButton.setText("Edit")
        self.editButton.clicked.connect(self.editButtonFunction)
        self.editButton.setStyleSheet("""QPushButton {
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

        self.editButtonLabel = QLabel(self.centralwidget)
        self.editButtonLabel.setGeometry(QRect(540, 520, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")
        self.editButtonIcon = QPixmap(filepath)
        self.editButtonIcon = self.editButtonIcon.scaled(50, 50)
        self.editButtonLabel.setPixmap(self.editButtonIcon)

        self.editButtonState = True

        self.editButton.raise_()
        self.editButtonLabel.raise_()
        self.addressLabel.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)

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

                # implement here
                editedDetailsJSON = {
                    'address' : self.addressLabel.text(),
                    'patientID' : self.user.getPatientID()
                }
                
                requests.patch('http://127.0.0.1:5000/patient/geocode/address', json=editedDetailsJSON)


    def setUser(self, mode, user):
        self.user = user
        if mode == "Patient":
            self.mode = "Patient"
            self.nameLabel.setText(self.user.getPatientName())
            self.iDLabel.setText(self.user.getPatientID())
            self.flexTitle1.setText("Date of Birth: ")
            self.flexTitle1.show()
            self.flexLabel1.setText(self.user.getPatientDOB())
            self.flexLabel1.show()
            self.flexTitle2.setText("Blood Type: ")
            self.flexTitle2.show()
            self.flexLabel2.setText(self.user.getPatientBlood())
            self.flexLabel2.show()
            self.flexTitle3.setText("Race: ")
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
            self.flexTitle1.setText("Clinic Contact: ")
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
            self.flexTitle1.setText("IC Number: ")
            self.flexTitle1.show()
            self.flexLabel1.setText(str(self.user.getDoctorICNumber()))
            self.flexLabel1.show()
            self.flexTitle2.setText("Doctor Type: ")
            self.flexTitle2.show()
            self.flexLabel2.setText(self.user.getDoctorType())
            self.flexLabel2.show()
            self.flexTitle3.setText("Doctor Contact: ")
            self.flexTitle3.show()
            self.flexLabel3.setText(str(self.user.getDoctorContact()))
            self.flexLabel3.show()
            self.flexTitle4.setText("Years of Experience: ")
            self.flexTitle4.show()
            self.flexLabel4.setText(str(self.user.getYearsOfExperience()))
            self.flexLabel4.show()
            self.flexTitle5.setText("Assigned Clinic: ")
            self.flexTitle5.show()
            self.flexLabel5.setText(self.user.getClinicID())
            self.flexLabel5.show()
            self.statusLabel.setText(self.user.getStatus())
            self.statusLabel.show()
            self.editButtonLabel.hide()
            self.editButton.hide()
