import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore

class PatientRegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PatientRegPushButton.clicked.connect(self.patient_save_data)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

# Main Title for Patient Register set as Label 
        self.PatientRegMainTitle = QtWidgets.QLabel(self.centralwidget)
        self.PatientRegMainTitle.setGeometry(20, 40, 541, 51)
        self.PatientRegMainTitle.setText("Registration for Call-A-Doctor!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PatientRegMainTitle.setFont(font)
        self.PatientRegMainTitle.setObjectName("PatientRegMainTitle")


# Sub TItle for Patient Register set  as Label 2
        self.PatientRegSubTitle = QtWidgets.QLabel(self.centralwidget)
        self.PatientRegSubTitle.setGeometry(60, 90, 451, 41)
        self.PatientRegSubTitle.setText("Get yourself registered now!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PatientRegSubTitle.setFont(font)
        self.PatientRegSubTitle.setObjectName("PatientRegSubTitle")


# First Name Text - set as Label 3
        self.PatientFirstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientFirstNameLabel.setGeometry(30, 150, 221, 21)
        self.PatientFirstNameLabel.setText("First Name as per IC/Passport")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientFirstNameLabel.setFont(font)
        self.PatientFirstNameLabel.setObjectName("PatientFirstNameLabel")


# Line Edit for Entering First Name 
        self.PatientFirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientFirstNameLineEdit.setGeometry(30, 170, 221, 31)
        self.PatientFirstNameLineEdit.setText("example - John")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientFirstNameLineEdit.setFont(font)
        self.PatientFirstNameLineEdit.setObjectName("PatientFirstNameLineEdit")

    
# Last Name Text - set as Label 4
        self.PatientLastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientLastNameLabel.setGeometry(30, 240, 221, 16)
        self.PatientLastNameLabel.setText("Last Name as per IC/Passport")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientLastNameLabel.setFont(font)
        self.PatientLastNameLabel.setObjectName("PatientLastNameLabel")


# Line Edit for Entering Last Name 
        self.PatientLastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientLastNameLineEdit.setGeometry(30, 260, 221, 31)
        self.PatientLastNameLineEdit.setText("example - Monroe")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientLastNameLineEdit.setFont(font)
        self.PatientLastNameLineEdit.setObjectName("PatientLastNameLineEdit")


# Email Text - set as label 5
        self.PatientEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientEmailLabel.setGeometry(30, 330, 221, 16)
        self.PatientEmailLabel.setText("Email")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientEmailLabel.setFont(font)
        self.PatientEmailLabel.setObjectName("PatientEmailLabel")


#Line Edit for Entering Email 
        self.PatientEmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientEmailLineEdit.setGeometry(30, 350, 221, 31)
        self.PatientEmailLineEdit.setText("example - superhero@miro.com")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientEmailLineEdit.setFont(font)
        self.PatientEmailLineEdit.setObjectName("PatientEmailLineEdit")


# Contact Numebr Text - set as label 6
        self.PatientContactLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientContactLabel.setGeometry(30, 420, 221, 16)
        self.PatientContactLabel.setText("Contact Number")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientContactLabel.setFont(font)
        self.PatientContactLabel.setObjectName("PatientContactLabel")


# Line Edit for Entering Contact Number
        self.PatientContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientContactLineEdit.setGeometry(30, 440, 221, 31)
        self.PatientContactLineEdit.setText("example - +60xxxxxxxx")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientContactLineEdit.setObjectName("PatientContactLineEdit")


# Current Residence Address Text - Set as Label 7
        self.PatientResidenceLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientResidenceLabel.setGeometry(280, 150, 221, 16)
        self.PatientResidenceLabel.setText("Current Residence Address")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientResidenceLabel.setFont(font)
        self.PatientResidenceLabel.setObjectName("PatientResidenceLabel")


# Line Edit for Entering Address
        self.PatientResidenceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientResidenceLineEdit.setGeometry(280, 170, 221, 31)
        self.PatientResidenceLineEdit.setText("example - Bayan Lepas, Penang")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientResidenceLineEdit.setFont(font)
        self.PatientResidenceLineEdit.setObjectName("PatientResidenceLineEdit")


# Date of Birth Text - Set as Label 8
        self.PatientDOBLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientDOBLabel.setGeometry(280, 240, 221, 16)
        self.PatientDOBLabel.setText("Date Of Birth")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientDOBLabel.setFont(font)
        self.PatientDOBLabel.setObjectName("PatientDOBLabel")


# Date-Edit for Selecting the DOB (The Function allows user to 
# directly select their Date, can add validation for age restrictions) 
        self.PatientDOBDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.PatientDOBDateEdit.setGeometry(280, 260, 221, 31)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientDOBDateEdit.setFont(font)
        self.PatientDOBDateEdit.setObjectName("PatientDOBDateEdit")


# IC or Passport Numebr Text - Set as Label 9
        self.PatientPassportLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientPassportLabel.setGeometry(280, 330, 221, 16)
        self.PatientPassportLabel.setText("IC/Passport Number")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientPassportLabel.setFont(font)
        self.PatientPassportLabel.setObjectName("PatientPassportLabel")


# Line-Edit for Entering the IC or passport number
        self.PatientPassportLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientPassportLineEdit.setGeometry(280, 350, 221, 31)
        self.PatientPassportLineEdit.setText("example - i123133xx")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientPassportLineEdit.setFont(font)
        self.PatientPassportLineEdit.setObjectName("PatientPassportLineEdit")


# Password Text - Set as Label 10
        self.PatientPasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientPasswordLabel.setGeometry(530, 150, 221, 16)
        self.PatientPasswordLabel.setText("Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientPasswordLabel.setFont(font)
        self.PatientPasswordLabel.setObjectName("PatientPasswordLabel")


# Line-Edit for Entering the password (Need to add validation)
#(Validation needs constraints like passwords needs to have - 
# Minimum 8 characters, upper case and lower case letters, numbers
# and Special Characters) 
        self.PatientPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientPasswordLineEdit.setGeometry(530, 170, 221, 31)
        self.PatientPasswordLineEdit.setText("example - SoMeThiNg@123")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientPasswordLineEdit.setFont(font)
        self.PatientPasswordLineEdit.setObjectName("PatientPasswordLineEdit")


# Confirm Password Text - set as Label 11
        self.PatientReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientReEnterPassLabel.setGeometry(530, 240, 221, 16)
        self.PatientReEnterPassLabel.setText("Confirm Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PatientReEnterPassLabel.setFont(font)
        self.PatientReEnterPassLabel.setObjectName("PatientReEnterPassLabel")


# Line-Edit for Entering the password again to confirm. 
# need validation to check if previously written password and
# re-entered password same or not, if not, error 404)
        self.PatientReEnterPassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientReEnterPassLineEdit.setGeometry(530, 260, 221, 31)
        self.PatientReEnterPassLineEdit.setText("Re-enter Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.PatientReEnterPassLineEdit.setFont(font)
        self.PatientReEnterPassLineEdit.setObjectName("PatientReEnterPassLineEdit")


# Register PushButton for Registering Account - (Saves the Data)
        self.PatientRegPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PatientRegPushButton.setGeometry(530, 400, 221, 41)
        self.PatientRegPushButton.setText("Register")

# DONT MIND THIS - This is just me editing the STYLE SHEET for
# the button to have color, and the text being White
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 63, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.PatientRegPushButton.setPalette(palette)
# StyleSheet customization ends here ^^^^^^^^^^^^^

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.PatientRegPushButton.setFont(font)
        self.PatientRegPushButton.setAutoFillBackground(False)
        self.PatientRegPushButton.setStyleSheet("background-color: rgb(53, 63, 203)")
        self.PatientRegPushButton.setObjectName("PatientRegPushButton")


# Push Button for "Going Back to Login page" - This needed a lot of
# Style sheet editting as, i had to make the Button transparent so 
# that it looks like a Link, so im sorry if the customization code 
# Looks a mess, please bear with it :) VVVVV

        self.PatientGoBackLoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.PatientGoBackLoginButton.setGeometry(530, 450, 221, 41)
        self.PatientGoBackLoginButton.setText("Go Back To Login")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 67, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 67, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
# The StyleSheet Customization ends here ^^^^^^

        self.PatientGoBackLoginButton.setPalette(palette)
        self.PatientGoBackLoginButton.setAutoFillBackground(True)
        self.PatientGoBackLoginButton.setStyleSheet("background-color: rgba(255, 255, 255, 10)")
        self.PatientGoBackLoginButton.setObjectName("GoBackLogin")

# Icon for LOGO - Set as Label 12        
        self.PatientRegisterLogo = QtWidgets.QLabel(self.centralwidget)
        self.PatientRegisterLogo.setGeometry(650, 50, 91, 61)
        self.PatientRegisterLogo.setText("LOGO Here")
        self.PatientRegisterLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.PatientRegisterLogo.setObjectName("PatientRegisterLogo")

# Code for All Labels, Buttons, Line-Edits end here ^^^^^^^

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Patient Register")

# Creating Code for User (Patient) to save their data
def patient_save_data(self):
        
        patient_data = {
            "PatientFirstNameLineEdit": self.PatientFirstNameLineEdit.text(),
            "PatientLastNameLineEdit": self.PatientLastNameLineEdit.text(),
            "PatientEmailLineEdit": self.PatientEmailLineEdit.text(),
            "PatientContactLineEdit": self.PatientContactLineEdit.text(),
            "PatientResidenceLineEdit": self.PatientResidenceLineEdit.text(),
            "PatientDOBDateEdit": self.PatientDOBDateEdit.date().toString(Qt.ISODate),
            "PatientPassportLineEdit": self.PatientPassportLineEdit.text(),
            "PatientPasswordLineEdit": self.PatientPasswordLineEdit.text(),
        }


