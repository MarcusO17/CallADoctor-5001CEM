import os
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


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


# Main Title for Doctor Register set as Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")


# Sub Title for Clinic Register set as Label 2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


# First Name for Doctor - Set as Label 3
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


# Line Edit for Entering doctor's First Name 
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("DocFirstName")


# Last Name for Doctor - Set as Label 4
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


# Line Edit for Entering Doctor's Last Name
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("DocLastName")


# Email for Doctor - Set as Label 5
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


# Line Edit for Doctor's Email 
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("DocEmail")


# Doctor's Contact Number - Set as Label 6
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 420, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")


# Line Edit for Doctor's Contact Number
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 440, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("DocContact")


# Doctor's Specialty - Set as Label 7
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 150, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")


# Line Edit for Entering Doctor's Specialty 
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("DocSpec")


# Doctor's Date of Birth - Set as Label 8
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 240, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")


# Date Edit option to Select doctor's DOB 
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(280, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("DocDOB")


# IC/Passport Number For Doctor - Set as label 9
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 330, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")


# Line Edit for Entering Doctor's IC/Passport Number
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("DocPassport")


# Highest Achievement & Verification Documents Attachment 
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(280, 400, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet("")
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")


# (NEED TO CHANGE FORMAT)
# Right Now, its just for building UI, so it is Line Edit, need to change - important
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(280, 440, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("DocAttach")


# Years of Experience for Doctor - Set as Label 10
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(530, 150, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")


# Line Edit for Entering Doc's Years of Experience
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(530, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("DocExp")


# Doctor's Password - Set as Label 11
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(530, 240, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        

# Line Edit for Entering Doctor's Password
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(530, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("DocPassword")
        
        
# Confirmation of Password for Doctor - Set as Label 14
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 330, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        
        
# Line Edit for Entering the password of Doctor Again
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(530, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("DocReEnterPass")

        
# PushButton for registering - Saves Data of Doctor        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 410, 221, 41))
        
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
        self.pushButton.setPalette(palette)

        #Style Sheet Code for Register End ^^^^^^^^^^^^^^^^^^^^^^^
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(53, 63, 203)")
        self.pushButton.setObjectName("Register")


# Push Button for Going Back to Login Page
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 460, 221, 41))

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
        self.pushButton_2.setPalette(palette)
        #Style Sheet code for transparent Block End ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 10)")
        self.pushButton_2.setObjectName("DocGoBackLogin")

        
# Icon For LOGO - Set as Label 12 (Need to Add Image)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(650, 50, 91, 61))
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setObjectName("label_12")
        
# Code for all Label, Buttons and even the Line Edits ends here ^^^^^^^^^^^^



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


# After a thorough Research, i learnt that this below class is
# importantn for Seting a text for the things we put up in the Application, 
# Like for example - we made the label 1, put it up in the application, then 
# to setup a visible text for user to see, we see the below functions
# ( READ AND DELETE THE COMMENT, IT IS ONLY FOR US TO KNOW )
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_7.setText(_translate("MainWindow", "example - 5 years"))
        self.label_9.setText(_translate("MainWindow", "IC/Passport Number"))
        self.lineEdit_6.setText(_translate("MainWindow", "example - 1232123xx"))
        self.label_7.setText(_translate("MainWindow", "Specialty (Type Of Doctor)"))
        self.label_6.setText(_translate("MainWindow", "Doctor Contact Number"))
        self.label_8.setText(_translate("MainWindow", "Date Of Birth"))
        self.label_2.setText(_translate("MainWindow", "Register yourself as a Doctor now!"))
        self.lineEdit_2.setText(_translate("MainWindow", "example - Monroe"))
        self.label_4.setText(_translate("MainWindow", "Last Name as per IC/Passport"))
        self.lineEdit_3.setText(_translate("MainWindow", "example - Doc123@new.com"))
        self.label_12.setText(_translate("MainWindow", "LOGO Here"))
        self.label.setText(_translate("MainWindow", "Registration for Call-A-Doctor!"))
        self.lineEdit.setText(_translate("MainWindow", "example - John"))
        self.label_3.setText(_translate("MainWindow", "First Name as per IC/Passport"))
        self.label_11.setText(_translate("MainWindow", "Password"))
        self.lineEdit_8.setText(_translate("MainWindow", "example - SoMeThiNg@123"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.lineEdit_5.setText(_translate("MainWindow", "example - Pediatrician, Surgeion etc"))
        self.lineEdit_4.setText(_translate("MainWindow", "example - +60xxxxxxxx"))
        self.pushButton_2.setText(_translate("MainWindow", "Go Back To Login"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.label_10.setText(_translate("MainWindow", "How many Years of Experience"))
        self.label_13.setText(_translate("MainWindow", "Highest Achievement & Verification Documents "))
        self.lineEdit_10.setText(_translate("MainWindow", "Attach Here                                              +"))
        self.label_14.setText(_translate("MainWindow", "Confirm Password"))
        self.lineEdit_11.setText(_translate("MainWindow", "Re-enter Password"))