import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore

class ClinicRegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ClinicRegisterPushButton.clicked.connect(self.ClinicSaveData)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


# Main Title for Clinic Register set as Label
        self.ClinicRegMainTitle = QtWidgets.QLabel(self.centralwidget)
        self.ClinicRegMainTitle.setGeometry(20, 40, 551, 51)
        self.ClinicRegMainTitle.setText("Registration for Call-A-Doctor!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ClinicRegMainTitle.setFont(font)
        self.ClinicRegMainTitle.setObjectName("ClinicRegMainTitle")

# Sub Title for Clinic Register set as Label 2
        self.ClinicRegSubTitle = QtWidgets.QLabel(self.centralwidget)
        self.ClinicRegSubTitle.setGeometry(60, 90, 451, 41)
        self.ClinicRegSubTitle.setText("Get your Clinic registered now!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ClinicRegSubTitle.setFont(font)
        self.ClinicRegSubTitle.setObjectName("ClinicRegSubTitle")


# Clinic ID Number - Set as Label 3
        self.ClinicIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicIDLabel.setGeometry(30, 150, 221, 21)
        self.ClinicIDLabel.setText("Clinic ID Number")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicIDLabel.setFont(font)
        self.ClinicIDLabel.setObjectName("ClinicIDLabel")


# Line Edit for Entering Clinic ID Number
        self.ClinicIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicIDLineEdit.setGeometry(30, 170, 221, 31)
        self.ClinicIDLineEdit.setText("example - P21002")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicIDLineEdit.setFont(font)
        self.ClinicIDLineEdit.setObjectName("ClinicIDLineEdit")


# Address of Clinic - Set as Label 4
        self.ClinicAddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicAddressLabel.setGeometry(30, 240, 221, 16)
        self.ClinicAddressLabel.setText("Address of Clinic")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicAddressLabel.setFont(font)
        self.ClinicAddressLabel.setObjectName("ClinicAddressLabel")


# Line Edit for Entering the Clinic Address
        self.ClinicAddressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicAddressLineEdit.setGeometry(30, 260, 221, 31)
        self.ClinicAddressLineEdit.setText("example - Bayan Lepas, Penang")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicAddressLineEdit.setFont(font)
        self.ClinicAddressLineEdit.setObjectName("ClinicAddressLineEdit")


# Name Of Clinic - Set As Label 5
        self.ClinicNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicNameLabel.setGeometry(30, 330, 221, 16)
        self.ClinicNameLabel.setText("Name of Clinic")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicNameLabel.setFont(font)
        self.ClinicNameLabel.setObjectName("ClinicNameLabel")


# Line Edit for Entering Clinic Name
        self.ClinicNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicNameLineEdit.setGeometry(30, 350, 221, 31)
        self.ClinicNameLineEdit.setText("example - ABCD Clinic")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicNameLineEdit.setFont(font)
        self.ClinicNameLineEdit.setObjectName("ClinicNameLineEdit")


# Clinic Contact Number - Set as Label 6
        self.ClinicContactLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicContactLabel.setGeometry(30, 420, 221, 16)
        self.ClinicContactLabel.setText("Clinic Contact Number")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicContactLabel.setFont(font)
        self.ClinicContactLabel.setObjectName("ClinicContactLabel")


# Line Edit for Entering Clinic Contact Number 
        self.ClinicContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicContactLineEdit.setGeometry(30, 440, 221, 31)
        self.ClinicContactLineEdit.setText("example - +60xxxxxxxx")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicContactLineEdit.setFont(font)
        self.ClinicContactLineEdit.setObjectName("ClinicContactLineEdit")


# Clinic Email - Set as Label 7
        self.ClinicEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicEmailLabel.setGeometry(280, 150, 221, 16)
        self.ClinicEmailLabel.setText("Clinic Email")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicEmailLabel.setFont(font)
        self.ClinicEmailLabel.setObjectName("ClinicEmailLabel")


# Line Edit for Entering Clinic Email
        self.ClinicEmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicEmailLineEdit.setGeometry(280, 170, 221, 31)
        self.ClinicEmailLineEdit.setText("example - abcklinik@new.com")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicEmailLineEdit.setFont(font)
        self.ClinicEmailLineEdit.setObjectName("ClinicEmailLineEdit")


# Clinic Post Code - Set as Label 8
        self.ClinicPostCodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicPostCodeLabel.setGeometry(280, 240, 221, 16)
        self.ClinicPostCodeLabel.setText("Clinic Post Code")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicPostCodeLabel.setFont(font)
        self.ClinicPostCodeLabel.setObjectName("ClinicPostCodeLabel")


# Line Edit for Entering Clinic Postal Code
        self.ClinicPostCodeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicPostCodeLineEdit.setGeometry(280, 260, 221, 31)
        self.ClinicPostCodeLineEdit.setText("example - 19000")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicPostCodeLineEdit.setFont(font)
        self.ClinicPostCodeLineEdit.setObjectName("ClinicPostCodeLineEdit")


# Verification Document - Set as Label 9
        self.ClinicDocumentLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicDocumentLabel.setGeometry(280, 330, 221, 16)
        self.ClinicDocumentLabel.setText("Verification Document")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicDocumentLabel.setFont(font)
        self.ClinicDocumentLabel.setObjectName("ClinicDocumentLabel")


# Actually for Now I set this Line Edit to show Attachnent of Document
# But need to change the functionality of this, probably into a push button
# which would allow to open file explorer to attach Document 
        self.ClinicDocumentLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicDocumentLineEdit.setGeometry(280, 350, 221, 31)
        self.ClinicDocumentLineEdit.setText("Attach Certification Document                    +")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicDocumentLineEdit.setFont(font)
        self.ClinicDocumentLineEdit.setObjectName("ClinicDocumentLineEdit")


# Clinic Password - Set as Label 10 
        self.ClinicPasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicPasswordLabel.setGeometry(530, 150, 221, 16)
        self.ClinicPasswordLabel.setText("Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicPasswordLabel.setFont(font)
        self.ClinicPasswordLabel.setObjectName("ClinicPasswordLabel")


# Line Edit for Clinic to Enter the Password
# (Validation needs constraints like passwords needs to have - 
# Minimum 8 characters, upper case and lower case letters, numbers
# and Special Characters)
        self.ClinicPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicPasswordLineEdit.setGeometry(530, 170, 221, 31)
        self.ClinicPasswordLineEdit.setText("example - SoMeThiNg@123")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicPasswordLineEdit.setFont(font)
        self.ClinicPasswordLineEdit.setObjectName("ClinicPasswordLineEdit")


# Confirm Password for CLinic - Set as Label 11
        self.ClinicReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClinicReEnterPassLabel.setGeometry(530, 240, 221, 16)
        self.ClinicReEnterPassLabel.setText("Confirm Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClinicReEnterPassLabel.setFont(font)
        self.ClinicReEnterPassLabel.setObjectName("ClinicReEnterPassLabel")


# Line Edit for Clinic to Enter Password again to confirm
# need validation to check if previously written password and
# re-entered password same or not, if not, error 404)
        self.ClinicReEnterPassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClinicReEnterPassLineEdit.setGeometry(530, 260, 221, 31)
        self.ClinicReEnterPassLineEdit.setText("Re-enter Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ClinicReEnterPassLineEdit.setFont(font)
        self.ClinicReEnterPassLineEdit.setObjectName("ClinicReEnterPassLineEdit")

        
# Register PushButton For Registering Account - Saves the Data
        self.ClinicRegisterPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClinicRegisterPushButton.setGeometry(530, 400, 221, 41)
        self.ClinicRegisterPushButton.setText("Register")

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
        self.ClinicRegisterPushButton.setPalette(palette)
# StyleSheet customization ends here ^^^^^^^^^^^^^
    
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ClinicRegisterPushButton.setFont(font)
        self.ClinicRegisterPushButton.setAutoFillBackground(False)
        self.ClinicRegisterPushButton.setStyleSheet("background-color: rgb(53, 63, 203)")
        self.ClinicRegisterPushButton.setObjectName("ClinicRegisterPushButton")
        
        
#  Push Button for "Going Back to Login page" - This needed a lot of
# Style sheet editting as, i had to make the Button transparent so 
# that it looks like a Link, so im sorry if the customization code 
# Looks a mess, please bear with it :)

        self.ClinicRegisterGoBackLogin = QtWidgets.QPushButton(self.centralwidget)
        self.ClinicRegisterGoBackLogin.setGeometry(530, 450, 221, 41)
        self.ClinicRegisterGoBackLogin.setText("Go Back To Login")

# Style Sheet Code for the transparent button start here vvvvvvvv
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
        self.ClinicRegisterGoBackLogin.setPalette(palette)
# Style Sheet code ends here ^^^^^^^^^^^^^^^

        self.ClinicRegisterGoBackLogin.setAutoFillBackground(False)
        self.ClinicRegisterGoBackLogin.setStyleSheet("background-color: rgba(255, 255, 255, 10)")
        self.ClinicRegisterGoBackLogin.setObjectName("ClinicGoBackLogin")
        
        
# Icon For LOGO - Set as Label 12 (Need to Add Image)
        self.ClinicRegisterLogo = QtWidgets.QLabel(self.centralwidget)
        self.ClinicRegisterLogo.setGeometry(650, 50, 91, 61)
        self.ClinicRegisterLogo.setText("LOGO Here")
        self.ClinicRegisterLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.ClinicRegisterLogo.setObjectName("ClinicRegisterLogo")
        
# Code for all Label, Buttons and even the Line Edits ends here ^^^^^^^^^^^^

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setWindowTitle("ClinicRegister")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



def ClinicSaveData(self):
     
        data = {
            "ClinicIDLineEdit": self.ClinicIDLineEdit.text(),
            "ClinicAddressLineEdit": self.ClinicAddressLineEdit.text(),
            "ClinicNameLineEdit": self.ClinicNameLineEdit.text(),
            "ClinicContactLineEdit": self.ClinicContactLineEdit.text(),
            "ClinicEmailLineEdit": self.ClinicEmailLineEdit.text(),
            "ClinicPostCodeLineEdit": self.ClinicPostCodeLineEdit.text(),
            "ClinicDocumentLineEdit": self.ClinicDocumentLineEdit.text(),
            "ClinicPasswordLineEdit": self.ClinicPasswordLineEdit.text()
            
        }