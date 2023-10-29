import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from .PageManager import PageManager

class PatientRegisterWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.pageManager = PageManager()



        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)


                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                # Main Title for Patient Register set as Label 
                self.patientRegMainTitle = QtWidgets.QLabel(self.centralwidget)
                self.patientRegMainTitle.setGeometry(20, 40, 541, 51)
                self.patientRegMainTitle.setText("Registration for Call-A-Doctor!")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(28)
                font.setBold(True)
                font.setWeight(75)
                self.patientRegMainTitle.setFont(font)
                self.patientRegMainTitle.setObjectName("PatientRegMainTitle")


                # Sub TItle for Patient Register set  as Label 2
                self.patientRegSubTitle = QtWidgets.QLabel(self.centralwidget)
                self.patientRegSubTitle.setGeometry(60, 90, 451, 41)
                self.patientRegSubTitle.setText("Get yourself registered now!")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.patientRegSubTitle.setFont(font)
                self.patientRegSubTitle.setObjectName("PatientRegSubTitle")


                # First Name Text - set as Label 3
                self.patientFirstNameLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientFirstNameLabel.setGeometry(30, 150, 221, 21)
                self.patientFirstNameLabel.setText("First Name as per IC/Passport")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientFirstNameLabel.setFont(font)
                self.patientFirstNameLabel.setObjectName("PatientFirstNameLabel")


                # Line Edit for Entering First Name 
                self.patientFirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientFirstNameLineEdit.setGeometry(30, 170, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientFirstNameLineEdit.setFont(font)
                self.patientFirstNameLineEdit.setObjectName("patientFirstNameLineEdit")
                self.patientFirstNameLineEdit.setPlaceholderText("example - John")


                # Last Name Text - set as Label 4
                self.patientLastNameLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientLastNameLabel.setGeometry(30, 240, 221, 16)
                self.patientLastNameLabel.setText("Last Name as per IC/Passport")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientLastNameLabel.setFont(font)
                self.patientLastNameLabel.setObjectName("PatientLastNameLabel")


                # Line Edit for Entering Last Name 
                self.patientLastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientLastNameLineEdit.setGeometry(30, 260, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientLastNameLineEdit.setFont(font)
                self.patientLastNameLineEdit.setObjectName("patientLastNameLineEdit")
                self.patientLastNameLineEdit.setPlaceholderText("example - Monroe")



                # Email Text - set as label 5
                self.patientEmailLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientEmailLabel.setGeometry(30, 330, 221, 16)
                self.patientEmailLabel.setText("Email")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientEmailLabel.setFont(font)
                self.patientEmailLabel.setObjectName("PatientEmailLabel")


                #Line Edit for Entering Email 
                self.patientEmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientEmailLineEdit.setGeometry(30, 350, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientEmailLineEdit.setFont(font)
                self.patientEmailLineEdit.setObjectName("patientEmailLineEdit")
                self.patientEmailLineEdit.setPlaceholderText("example - superhero@miro.com")



                # Contact Numebr Text - set as label 6
                self.patientContactLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientContactLabel.setGeometry(30, 420, 221, 16)
                self.patientContactLabel.setText("Contact Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientContactLabel.setFont(font)
                self.patientContactLabel.setObjectName("PatientContactLabel")


                # Line Edit for Entering Contact Number
                self.patientContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientContactLineEdit.setGeometry(30, 440, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientContactLineEdit.setObjectName("patientContactLineEdit")
                self.patientContactLineEdit.setPlaceholderText("example - +60xxxxxxxx")


                # Current Residence Address Text - Set as Label 7
                self.patientResidenceLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientResidenceLabel.setGeometry(280, 150, 221, 16)
                self.patientResidenceLabel.setText("Current Residence Address")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientResidenceLabel.setFont(font)
                self.patientResidenceLabel.setObjectName("PatientResidenceLabel")


                # Line Edit for Entering Address
                self.patientResidenceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientResidenceLineEdit.setGeometry(280, 170, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientResidenceLineEdit.setFont(font)
                self.patientResidenceLineEdit.setObjectName("patientResidenceLineEdit")
                self.patientResidenceLineEdit.setPlaceholderText("example - Bayan Lepas, Penang")


                # Date of Birth Text - Set as Label 8
                self.patientDOBLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientDOBLabel.setGeometry(280, 240, 221, 16)
                self.patientDOBLabel.setText("Date Of Birth")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientDOBLabel.setFont(font)
                self.patientDOBLabel.setObjectName("PatientDOBLabel")


                # Date-Edit for Selecting the DOB (The Function allows user to 
                # directly select their Date, can add validation for age restrictions) 
                self.patientDOBDateEdit = QtWidgets.QDateEdit(self.centralwidget)
                self.patientDOBDateEdit.setGeometry(280, 260, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientDOBDateEdit.setFont(font)
                self.patientDOBDateEdit.setObjectName("patientDOBDateEdit")


                # IC or Passport Numebr Text - Set as Label 9
                self.patientPassportLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientPassportLabel.setGeometry(280, 330, 221, 16)
                self.patientPassportLabel.setText("IC/Passport Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientPassportLabel.setFont(font)
                self.patientPassportLabel.setObjectName("PatientPassportLabel")


                # Line-Edit for Entering the IC or passport number
                self.patientPassportLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientPassportLineEdit.setGeometry(280, 350, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientPassportLineEdit.setFont(font)
                self.patientPassportLineEdit.setObjectName("patientPassportLineEdit")
                self.patientPassportLineEdit.setPlaceholderText("example - i123133xx")


                # Blood Type Text - Set as Label
                self.patientBloodTypeLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientBloodTypeLabel.setGeometry(530, 150, 221, 16)
                self.patientBloodTypeLabel.setText("Blood Type")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientBloodTypeLabel.setFont(font)
                self.patientBloodTypeLabel.setObjectName("PatientBloodType")


                # Line Edit for entering Blood Type
                self.patientBloodTypeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientBloodTypeLineEdit.setGeometry(530, 170, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientBloodTypeLineEdit.setFont(font)
                self.patientBloodTypeLineEdit.setObjectName("patientBloodType")
                self.patientBloodTypeLineEdit.setPlaceholderText("example -  AB+")


                # Password Text - Set as Label 10
                self.patientPasswordLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientPasswordLabel.setGeometry(530, 240, 221, 16)
                self.patientPasswordLabel.setText("Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientPasswordLabel.setFont(font)
                self.patientPasswordLabel.setObjectName("PatientPasswordLabel")


                # Line-Edit for Entering the password (Need to add validation)
                #(Validation needs constraints like passwords needs to have - 
                # Minimum 8 characters, upper case and lower case letters, numbers
                # and Special Characters) 
                self.patientPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientPasswordLineEdit.setGeometry(530, 260, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientPasswordLineEdit.setFont(font)
                self.patientPasswordLineEdit.setObjectName("patientPasswordLineEdit")
                self.patientPasswordLineEdit.setPlaceholderText("example - SoMeThiNg@123")
                self.patientPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.patientPasswordLineEdit.textChanged.connect(self.validatePatientPasswordMatch)

                self.showPatientPasswordCheckbox = QtWidgets.QCheckBox("Show Password", self.centralwidget)
                self.showPatientPasswordCheckbox.setGeometry(530, 290, 221, 31)
                self.showPatientPasswordCheckbox.stateChanged.connect(self.togglePatientPasswordVisibility)


                # Confirm Password Text - set as Label 11
                self.patientReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
                self.patientReEnterPassLabel.setGeometry(530, 330, 221, 16)
                self.patientReEnterPassLabel.setText("Confirm Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.patientReEnterPassLabel.setFont(font)
                self.patientReEnterPassLabel.setObjectName("PatientReEnterPassLabel")


                # Line-Edit for Entering the password again to confirm. 
                # need validation to check if previously written password and
                # re-entered password same or not, if not, error 404)
                self.patientReEnterPassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.patientReEnterPassLineEdit.setGeometry(530, 350, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.patientReEnterPassLineEdit.setFont(font)
                self.patientReEnterPassLineEdit.setObjectName("patientReEnterPassLineEdit")
                self.patientReEnterPassLineEdit.setPlaceholderText("Re-enter Password")
                self.patientReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.patientReEnterPassLineEdit.textChanged.connect(self.validatePatientPasswordMatch)

                self.showPatientRePasswordCheckbox = QtWidgets.QCheckBox("Show Password", self.centralwidget)
                self.showPatientRePasswordCheckbox.setGeometry(530, 380, 221, 31)
                self.showPatientRePasswordCheckbox.stateChanged.connect(self.togglePatientReEnterPasswordVisibility)


                # Register PushButton for Registering Account - (Saves the Data)
                self.patientRegPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.patientRegPushButton.setGeometry(530, 440, 221, 41)
                self.patientRegPushButton.setText("Register")

                # DONT MIND THIS - This is just me editing the STYLE SHEET for
                # the button to have color, and the text being White
                stylesheet5 = """
                QPushButton {
                        background-color: rgb(53, 63, 203);
                        color: rgb(255, 255, 255);
                }

                QPushButton:disabled {
                        background-color: rgb(53, 63, 203);
                        color: rgb(120, 120, 120);
                }
                """
                # StyleSheet customization ends here ^^^^^^^^^^^^^

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                self.patientRegPushButton.setFont(font)
                self.patientRegPushButton.setAutoFillBackground(False)
                self.patientRegPushButton.setStyleSheet(stylesheet5)
                self.patientRegPushButton.setObjectName("patientRegPushButton")
                self.patientRegPushButton.clicked.connect(self.patient_save_data)


                # Push Button for "Going Back to Login page" - 

                self.patientGoBackLoginButton = QtWidgets.QPushButton(self.centralwidget)
                self.patientGoBackLoginButton.setGeometry(530, 490, 221, 41)
                self.patientGoBackLoginButton.setText("Go Back To Login")
                #stylesheeet editing vv
                stylesheet6 = """
                QPushButton {
                        background-color: rgba(255, 255, 255, 10);
                        color: rgb(0, 67, 202);
                        text-decoration: underline;
                }

                QPushButton:disabled {
                         background-color: rgba(255, 255, 255, 10);
                         color: rgb(120, 120, 120);
                }
                """
                # The StyleSheet Customization ends here ^^^^^^
                self.patientGoBackLoginButton.setAutoFillBackground(True)
                self.patientGoBackLoginButton.setStyleSheet(stylesheet6)
                self.patientGoBackLoginButton.setObjectName("GoBackLogin")
                self.patientGoBackLoginButton.clicked.connect(self.goBackLogin)

                # Icon for LOGO - Set as Label 12        
                self.patientRegisterLogo = QtWidgets.QLabel(self.centralwidget)
                self.patientRegisterLogo.setGeometry(650, 50, 91, 61)
                self.patientRegisterLogo.setText("LOGO Here")
                self.patientRegisterLogo.setFrameShape(QtWidgets.QFrame.Box)
                self.patientRegisterLogo.setObjectName("PatientRegisterLogo")

                # Code for All Labels, Buttons, Line-Edits end here ^^^^^^^

                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                MainWindow.setWindowTitle("Patient Register")

        # Creating Code for User (Patient) to save their data
        def patient_save_data(self):

                patient_data = {
                        "patientFirstNameLineEdit": self.patientFirstNameLineEdit.text(),
                        "patientLastNameLineEdit": self.patientLastNameLineEdit.text(),
                        "patientEmailLineEdit": self.patientEmailLineEdit.text(),
                        "patientContactLineEdit": self.patientContactLineEdit.text(),
                        "patientResidenceLineEdit": self.patientResidenceLineEdit.text(),
                        "patientDOBDateEdit": self.patientDOBDateEdit.date().toString(Qt.ISODate),
                        "patientPassportLineEdit": self.patientPassportLineEdit.text(),
                        "patientPasswordLineEdit": self.patientPasswordLineEdit.text(),
                }

                # marcus post to databasee here

                
                goRegisterDialogBox = QMessageBox.question(self.centralwidget, "Registration Confirmation",
                                                                "Are you sure you all your details are correct?",
                                                        QMessageBox.Yes | QMessageBox.No)
                if goRegisterDialogBox == QMessageBox.Yes:
                        self.pageManager.goBack()

        def goBackLogin(self):
                goBackLoginDialogBox = QMessageBox.question(self.centralwidget, "Go Back Login",
                                                                "Are you sure you want to go back?",
                                                QMessageBox.Yes | QMessageBox.No)
                if goBackLoginDialogBox == QMessageBox.Yes:
                        self.pageManager.goBack()


        def togglePatientPasswordVisibility(self, state):
                if state == Qt.Checked:
                        self.patientPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                        self.patientPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)


        def togglePatientReEnterPasswordVisibility(self, state):
                if state == Qt.Checked:
                        self.patientReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                        self.patientReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        
        def validatePatientPasswordMatch(self):
                password = self.patientPasswordLineEdit.text()
                reenter_password = self.patientReEnterPassLineEdit.text()

                if password == reenter_password:
                        # Passwords match, Color of the field will be green
                        self.patientReEnterPassLineEdit.setStyleSheet("border: 2px solid green;")
                else:
                        # Passwords do not match, indicate an error, Color of the field will be red
                        self.patientReEnterPassLineEdit.setStyleSheet("border: 2px solid red;")
