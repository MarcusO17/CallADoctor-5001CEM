import os
import json
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore

class DoctorRegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.RegisterPushButton.clicked.connect(self.save_data)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


# Main Title for Doctor Register set as Label
        self.MainTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainTitleLabel.setGeometry(20, 40, 551, 53)
        self.MainTitleLabel.setText("Registration for Call-A-Doctor!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        self.MainTitleLabel.setFont(font)
        font.setWeight(75)
        self.MainTitleLabel.setObjectName("MainTitleLabel")


# Sub Title for Clinic Register set as Label 2
        self.SubtitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.SubtitleLabel.setGeometry(60, 90, 451, 41)
        self.SubtitleLabel.setText("Register yourself as a Doctor now!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.SubtitleLabel.setFont(font)
        self.SubtitleLabel.setObjectName("SubTitleLabel")


# First Name for Doctor - Set as Label 3
        self.DocFirstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocFirstNameLabel.setGeometry(30, 150, 221, 21)
        self.DocFirstNameLabel.setText("First Name as per IC/Passport")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocFirstNameLabel.setFont(font)
        self.DocFirstNameLabel.setObjectName("DocFirstNameLabel")


# Line Edit for Entering doctor's First Name 
        self.DocFirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocFirstNameLineEdit.setGeometry(30, 170, 221, 31)
        self.DocFirstNameLineEdit.setText("example - John")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocFirstNameLineEdit.setFont(font)
        self.DocFirstNameLineEdit.setObjectName("DocFirstNameLineEdit")


# Last Name for Doctor - Set as Label 4
        self.DocLastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocLastNameLabel.setGeometry(30, 240, 221, 16)
        self.DocLastNameLabel.setText("Last Name as per IC/Passport")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocLastNameLabel.setFont(font)
        self.DocLastNameLabel.setObjectName("DocLastNameLabel")


# Line Edit for Entering Doctor's Last Name
        self.DocLastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocLastNameLineEdit.setGeometry(30, 260, 221, 31)
        self.DocLastNameLineEdit.setText("example - Monroe")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocLastNameLineEdit.setFont(font)
        self.DocLastNameLineEdit.setObjectName("DocLastNameLineEdit")


# Email for Doctor - Set as Label 5
        self.DocEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocEmailLabel.setGeometry(30, 330, 221, 16)
        self.DocEmailLabel.setText("Email")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocEmailLabel.setFont(font)
        self.DocEmailLabel.setObjectName("DocEmailLabel")


# Line Edit for Doctor's Email 
        self.DocEmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocEmailLineEdit.setGeometry(30, 350, 221, 31)
        self.DocEmailLineEdit.setText("example - Doc123@new.com")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocEmailLineEdit.setFont(font)
        self.DocEmailLineEdit.setObjectName("DocEmailLineEdit")


# Doctor's Contact Number - Set as Label 6
        self.DocContactLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocContactLabel.setGeometry(30, 420, 221, 16)
        self.DocContactLabel.setText("Doctor Contact Number")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocContactLabel.setFont(font)
        self.DocContactLabel.setObjectName("DocContactLabel")


# Line Edit for Doctor's Contact Number
        self.DocContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocContactLineEdit.setGeometry(30, 440, 221, 31)
        self.DocContactLineEdit.setText("example - +60xxxxxxxx")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocContactLineEdit.setFont(font)
        self.DocContactLineEdit.setObjectName("DocContactLineEdit")


# Doctor's Specialty - Set as Label 7
        self.DocSpecialtyLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocSpecialtyLabel.setGeometry(280, 150, 221, 16)
        self.DocSpecialtyLabel.setText("Specialty (Type Of Doctor)")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocSpecialtyLabel.setFont(font)
        self.DocSpecialtyLabel.setObjectName("DocSpecialtyLabel")


# Line Edit for Entering Doctor's Specialty 
        self.DocSpecialtyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocSpecialtyLineEdit.setGeometry(280, 170, 221, 31)
        self.DocSpecialtyLineEdit.setText("example - Pediatrician, Surgeion etc")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocSpecialtyLineEdit.setFont(font)
        self.DocSpecialtyLineEdit.setObjectName("DocSpecialtyLineEdit")


# Doctor's Date of Birth - Set as Label 8
        self.DocDOBLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocDOBLabel.setGeometry(280, 240, 221, 16)
        self.DocDOBLabel.setText("Date Of Birth")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocDOBLabel.setFont(font)
        self.DocDOBLabel.setObjectName("DocDOBLabel")


# Date Edit option to Select doctor's DOB 
        self.DocDOBDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.DocDOBDateEdit.setGeometry(280, 260, 221, 31)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocDOBDateEdit.setFont(font)
        self.DocDOBDateEdit.setObjectName("DocDOBDateEdit")


# IC/Passport Number For Doctor - Set as label 9
        self.DocPassportLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocPassportLabel.setGeometry(280, 330, 221, 16)
        self.DocPassportLabel.setText("IC/Passport Number")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocPassportLabel.setFont(font)
        self.DocPassportLabel.setObjectName("DocPassportLabel")


# Line Edit for Entering Doctor's IC/Passport Number
        self.DocPassportLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocPassportLineEdit.setGeometry(280, 350, 221, 31)
        self.DocPassportLineEdit.setText("example - 1232123xx")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocPassportLineEdit.setFont(font)
        self.DocPassportLineEdit.setObjectName("DocPassportLineEdit")


# Highest Achievement & Verification Documents Attachment 
        self.DocAttachmentLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocAttachmentLabel.setGeometry(280, 400, 221, 40)
        self.DocAttachmentLabel.setText("Highest Achievement & Verification Documents")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocAttachmentLabel.setFont(font)
        self.DocAttachmentLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DocAttachmentLabel.setStyleSheet("")
        self.DocAttachmentLabel.setWordWrap(True)
        self.DocAttachmentLabel.setObjectName("DocAttachmentLabel")


# (NEED TO CHANGE FORMAT)
# Right Now, its just for building UI, so it is Line Edit, need to change - important
        self.DocAttachmentLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocAttachmentLineEdit.setGeometry(280, 440, 221, 31)
        self.DocAttachmentLineEdit.setText("Attach Here                                              +")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocAttachmentLineEdit.setFont(font)
        self.DocAttachmentLineEdit.setObjectName("DocAttachmentLineEdit")


# Years of Experience for Doctor - Set as Label 10
        self.DocExpLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocExpLabel.setGeometry(530, 150, 221, 16)
        self.DocExpLabel.setText("How many Years of Experience")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocExpLabel.setFont(font)
        self.DocExpLabel.setObjectName("DocExpLabel")


# Line Edit for Entering Doc's Years of Experience
        self.DocExpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocExpLineEdit.setGeometry(530, 170, 221, 31)
        self.DocExpLineEdit.setText("example - 5 years")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocExpLineEdit.setFont(font)
        self.DocExpLineEdit.setObjectName("DocExpLineEdit")


# Doctor's Password - Set as Label 11
        self.DocPasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocPasswordLabel.setGeometry(530, 240, 221, 16)
        self.DocPasswordLabel.setText("Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocPasswordLabel.setFont(font)
        self.DocPasswordLabel.setObjectName("DocPasswordLabel")
        

# Line Edit for Entering Doctor's Password
        self.DocPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocPasswordLineEdit.setGeometry(530, 260, 221, 31)
        self.DocPasswordLineEdit.setText("example - SoMeThiNg@123")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocPasswordLineEdit.setFont(font)
        self.DocPasswordLineEdit.setObjectName("DocPasswordLineEdit")
        
        
# Confirmation of Password for Doctor - Set as Label 14
        self.DocReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocReEnterPassLabel.setGeometry(530, 330, 221, 16)
        self.DocReEnterPassLabel.setText("Confirm Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DocReEnterPassLabel.setFont(font)
        self.DocReEnterPassLabel.setObjectName("DocReEnterPassLabel")
        
        
# Line Edit for Entering the password of Doctor Again
        self.DocReEnterPassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DocReEnterPassLineEdit.setGeometry(530, 350, 221, 31)
        self.DocReEnterPassLineEdit.setText("Re-enter Password")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DocReEnterPassLineEdit.setFont(font)
        self.DocReEnterPassLineEdit.setObjectName("DocReEnterPassLineEdit")

        
# PushButton for registering - Saves Data of Doctor        
        self.RegisterPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterPushButton.setGeometry(530, 410, 221, 41)
        self.RegisterPushButton.setText("Register")
        
        #Style Sheet Code for Register vvvvvvvvvvvvvvvvvvvvvv
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
        self.RegisterPushButton.setPalette(palette)

        #Style Sheet Code for Register End ^^^^^^^^^^^^^^^^^^^^^^^
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.RegisterPushButton.setFont(font)
        self.RegisterPushButton.setAutoFillBackground(False)
        self.RegisterPushButton.setStyleSheet("background-color: rgb(53, 63, 203)")
        self.RegisterPushButton.setObjectName("Register")


# Push Button for Going Back to Login Page
        self.DocGoBackLoginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.DocGoBackLoginPushButton.setGeometry(530, 460, 221, 41)
        self.DocGoBackLoginPushButton.setText("Go Back To Login")

        #Style SHeet code for Transparent Block white differnt text color vvvvvvvv
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
        self.DocGoBackLoginPushButton.setPalette(palette)
        #Style Sheet code for transparent Block End ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        self.DocGoBackLoginPushButton.setAutoFillBackground(False)
        self.DocGoBackLoginPushButton.setStyleSheet("background-color: rgba(255, 255, 255, 10)")
        self.DocGoBackLoginPushButton.setObjectName("DocGoBackLoginPushButton")

        
# Icon For LOGO - Set as Label 12 (Need to Add Image)
        self.DocPageLogo = QtWidgets.QLabel(self.centralwidget)
        self.DocPageLogo.setGeometry(650, 50, 91, 61)
        self.DocPageLogo.setText("LOGO Here")
        self.DocPageLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.DocPageLogo.setObjectName("DocPageLogo")
        
# Code for all Label, Buttons and even the Line Edits ends here ^^^^^^^^^^^^



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setWindowTitle("Doctor Registration")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


def save_data(self):
        doctorName  = f'{self.DocFirstNameLineEdit.text()} {self.DocLastNameLineEdit.text()}'
        doctorEmail = 
    
        doctor_data = {
            "DocFirstName": self.DocFirstNameLineEdit.text(),
            "DocLastName": self.DocLastNameLineEdit.text(),
            "DocEmail": self.DocEmailLineEdit.text(),
            "DocCon": self.DocContactLineEdit.text(),
            "specialty": self.DocSpecialtyLineEdit.text(),
            "date_of_birth": self.DocDOBDateEdit.date().toString(Qt.ISODate),
            "ic_passport_number": self.DocPassportLineEdit.text(),
            "years_of_experience": self.DocExpLineEdit.text(),
            "password": self.DocPasswordLineEdit.text(),
        }

        

        
        
        
        
        
      
       
