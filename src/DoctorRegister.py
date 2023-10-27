import os
import requests
import json
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from .model import Registration
from .PageManager import PageManager

class DoctorRegisterWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.pageManager = PageManager()
                self.RegisterPushButton.clicked.connect(lambda checked: self.saveData)


        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)


                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")


        # Main Title for Doctor Register set as Label
                self.mainTitleLabel = QtWidgets.QLabel(self.centralwidget)
                self.mainTitleLabel.setGeometry(20, 40, 551, 53)
                self.mainTitleLabel.setText("Registration for Call-A-Doctor!")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(28)
                font.setBold(True)
                self.mainTitleLabel.setFont(font)
                font.setWeight(75)
                self.mainTitleLabel.setObjectName("mainTitleLabel")


        # Sub Title for Clinic Register set as Label 2
                self.subtitleLabel = QtWidgets.QLabel(self.centralwidget)
                self.subtitleLabel.setGeometry(60, 90, 451, 41)
                self.subtitleLabel.setText("Register yourself as a Doctor now!")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.subtitleLabel.setFont(font)
                self.subtitleLabel.setObjectName("subtitleLabel")


        # First Name for Doctor - Set as Label 3
                self.docFirstNameLabel = QtWidgets.QLabel(self.centralwidget)
                self.docFirstNameLabel.setGeometry(30, 150, 221, 21)
                self.docFirstNameLabel.setText("First Name as per IC/Passport")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docFirstNameLabel.setFont(font)
                self.docFirstNameLabel.setObjectName("docFirstNameLabel")


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
                self.docLastNameLabel = QtWidgets.QLabel(self.centralwidget)
                self.docLastNameLabel.setGeometry(30, 240, 221, 16)
                self.docLastNameLabel.setText("Last Name as per IC/Passport")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docLastNameLabel.setFont(font)
                self.docLastNameLabel.setObjectName("docLastNameLabel")


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
                self.docEmailLabel = QtWidgets.QLabel(self.centralwidget)
                self.docEmailLabel.setGeometry(30, 330, 221, 16)
                self.docEmailLabel.setText("Email")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docEmailLabel.setFont(font)
                self.docEmailLabel.setObjectName("docEmailLabel")


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
                self.docContactLabel = QtWidgets.QLabel(self.centralwidget)
                self.docContactLabel.setGeometry(30, 420, 221, 16)
                self.docContactLabel.setText("Doctor Contact Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docContactLabel.setFont(font)
                self.docContactLabel.setObjectName("docContactLabel")


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
                self.docSpecialtyLabel = QtWidgets.QLabel(self.centralwidget)
                self.docSpecialtyLabel.setGeometry(280, 150, 221, 16)
                self.docSpecialtyLabel.setText("Specialty (Type Of Doctor)")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docSpecialtyLabel.setFont(font)
                self.docSpecialtyLabel.setObjectName("docSpecialtyLabel")


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
                self.docDOBLabel = QtWidgets.QLabel(self.centralwidget)
                self.docDOBLabel.setGeometry(280, 240, 221, 16)
                self.docDOBLabel.setText("Date Of Birth")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docDOBLabel.setFont(font)
                self.docDOBLabel.setObjectName("docDOBLabel")


        # Date Edit option to Select doctor's DOB 
                self.DocDOBDateEdit = QtWidgets.QDateEdit(self.centralwidget)
                self.DocDOBDateEdit.setGeometry(280, 260, 221, 31)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.DocDOBDateEdit.setFont(font)
                self.DocDOBDateEdit.setObjectName("DocDOBDateEdit")


        # IC/Passport Number For Doctor - Set as label 9
                self.docPassportLabel = QtWidgets.QLabel(self.centralwidget)
                self.docPassportLabel.setGeometry(280, 330, 221, 16)
                self.docPassportLabel.setText("IC/Passport Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docPassportLabel.setFont(font)
                self.docPassportLabel.setObjectName("docPassportLabel")


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
                self.docAttachmentLabel = QtWidgets.QLabel(self.centralwidget)
                self.docAttachmentLabel.setGeometry(280, 400, 221, 40)
                self.docAttachmentLabel.setText("Highest Achievement & Verification Documents")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docAttachmentLabel.setFont(font)
                self.docAttachmentLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.docAttachmentLabel.setStyleSheet("")
                self.docAttachmentLabel.setWordWrap(True)
                self.docAttachmentLabel.setObjectName("docAttachmentLabel")


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
                self.docExpLabel = QtWidgets.QLabel(self.centralwidget)
                self.docExpLabel.setGeometry(530, 150, 221, 16)
                self.docExpLabel.setText("How many Years of Experience")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docExpLabel.setFont(font)
                self.docExpLabel.setObjectName("docExpLabel")


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
                self.docPasswordLabel = QtWidgets.QLabel(self.centralwidget)
                self.docPasswordLabel.setGeometry(530, 240, 221, 16)
                self.docPasswordLabel.setText("Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docPasswordLabel.setFont(font)
                self.docPasswordLabel.setObjectName("docPasswordLabel")
                

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
                self.docReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
                self.docReEnterPassLabel.setGeometry(530, 330, 221, 16)
                self.docReEnterPassLabel.setText("Confirm Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docReEnterPassLabel.setFont(font)
                self.docReEnterPassLabel.setObjectName("docReEnterPassLabel")
                
                
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
                self.docPageLogo = QtWidgets.QLabel(self.centralwidget)
                self.docPageLogo.setGeometry(650, 50, 91, 61)
                self.docPageLogo.setText("LOGO Here")
                self.docPageLogo.setFrameShape(QtWidgets.QFrame.Box)
                self.docPageLogo.setObjectName("docPageLogo")
                
        # Code for all Label, Buttons and even the Line Edits ends here ^^^^^^^^^^^^



                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                MainWindow.setWindowTitle("Doctor Registration")
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)


        def saveData(self):
                doctorName  = f'{self.DocFirstNameLineEdit.text()} {self.DocLastNameLineEdit.text()}'
                doctorEmail = self.DocEmailLineEdit.text()
                doctorPassword = self.DocPasswordLineEdit.text()
                doctorContact = self.DocContactLineEdit.text()
                doctorType = self.DocSpecialtyLineEdit.text()
                yearsOfExperience = self.DocExpLineEdit.text()
                doctorICNumber = self.DocPassportLineEdit.text()
                

                doctorJSON = {
                        "doctorName": doctorName,
                        "doctorPassword": doctorPassword,
                        "doctorICNumber": doctorICNumber,
                        "doctorContact": doctorContact,
                        "doctorType": doctorType,
                        "yearOfExperience": yearsOfExperience,
                        "doctorEmail": doctorEmail,
                        "status": "Inactive",
                        "clinicID": 0
                }

                response,registerFlag = Registration.registerDoctor(doctorJSON)
                if registerFlag:
                        pass
                else:
                        print(response)