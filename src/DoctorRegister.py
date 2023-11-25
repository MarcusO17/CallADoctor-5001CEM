import os
import requests
import json
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QMessageBox, QFileDialog, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from .model import Registration
from .PageManager import PageManager

class DoctorRegisterWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.pageManager = PageManager()


        def setupUi(self, MainWindow):
                CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
   
                MainWindow.setObjectName("MainWindow")
                MainWindow.setFixedWidth(1080)
                MainWindow.setFixedHeight(720)

                self.setAutoFillBackground(True)
                palette = self.palette()
                gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
                palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))
                self.setPalette(palette)
                self.setStyleSheet(f"QWidget#MainWindow {{background: {gradient}}};")


                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")


        # Main Title for Doctor Register set as Label
                self.mainTitleLabel = QtWidgets.QLabel(self.centralwidget)
                self.mainTitleLabel.setGeometry(35, 50, 541, 51)
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
                self.subtitleLabel.setGeometry(35, 100, 451, 41)
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
                self.docFirstNameLabel.setGeometry(90, 220, 250, 21)
                self.docFirstNameLabel.setText("First Name as per IC/Passport")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docFirstNameLabel.setFont(font)
                self.docFirstNameLabel.setObjectName("docFirstNameLabel")


        # Line Edit for Entering doctor's First Name 
                self.docFirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docFirstNameLineEdit.setGeometry(90, 240, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docFirstNameLineEdit.setFont(font)
                self.docFirstNameLineEdit.setObjectName("docFirstNameLineEdit")
                self.docFirstNameLineEdit.setPlaceholderText("example - John")


        # Last Name for Doctor - Set as Label 4
                self.docLastNameLabel = QtWidgets.QLabel(self.centralwidget)
                self.docLastNameLabel.setGeometry(90, 310, 250, 16)
                self.docLastNameLabel.setText("Last Name as per IC/Passport")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docLastNameLabel.setFont(font)
                self.docLastNameLabel.setObjectName("docLastNameLabel")


        # Line Edit for Entering Doctor's Last Name
                self.docLastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docLastNameLineEdit.setGeometry(90, 330, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docLastNameLineEdit.setFont(font)
                self.docLastNameLineEdit.setObjectName("docLastNameLineEdit")
                self.docLastNameLineEdit.setPlaceholderText("example - Monroe")


        # Email for Doctor - Set as Label 5
                self.docEmailLabel = QtWidgets.QLabel(self.centralwidget)
                self.docEmailLabel.setGeometry(90, 400, 250, 16)
                self.docEmailLabel.setText("Email")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docEmailLabel.setFont(font)
                self.docEmailLabel.setObjectName("docEmailLabel")


        # Line Edit for Doctor's Email 
                self.docEmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docEmailLineEdit.setGeometry(90, 420, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docEmailLineEdit.setFont(font)
                self.docEmailLineEdit.setObjectName("docEmailLineEdit")
                self.docEmailLineEdit.setPlaceholderText("example - Doc123@new.com")


        # Doctor's Contact Number - Set as Label 6
                self.docContactLabel = QtWidgets.QLabel(self.centralwidget)
                self.docContactLabel.setGeometry(90, 490, 250, 16)
                self.docContactLabel.setText("Doctor Contact Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docContactLabel.setFont(font)
                self.docContactLabel.setObjectName("docContactLabel")


        # Line Edit for Doctor's Contact Number
                self.docContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docContactLineEdit.setGeometry(90, 510, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docContactLineEdit.setFont(font)
                self.docContactLineEdit.setObjectName("docContactLineEdit")
                self.docContactLineEdit.setPlaceholderText("example - +60xxxxxxxx")


        # Doctor's Specialty - Set as Label 7
                self.docSpecialtyLabel = QtWidgets.QLabel(self.centralwidget)
                self.docSpecialtyLabel.setGeometry(410, 220, 250, 16)
                self.docSpecialtyLabel.setText("Specialty (Type Of Doctor)")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docSpecialtyLabel.setFont(font)
                self.docSpecialtyLabel.setObjectName("docSpecialtyLabel")


        # Line Edit for Entering Doctor's Specialty 
                self.docSpecialtyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docSpecialtyLineEdit.setGeometry(410, 240, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docSpecialtyLineEdit.setFont(font)
                self.docSpecialtyLineEdit.setObjectName("docSpecialtyLineEdit")
                self.docSpecialtyLineEdit.setPlaceholderText("example - Pediatrician, Surgeon")


        # Doctor's Date of Birth - Set as Label 8
                self.docDOBLabel = QtWidgets.QLabel(self.centralwidget)
                self.docDOBLabel.setGeometry(410, 310, 250, 16)
                self.docDOBLabel.setText("Date Of Birth")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docDOBLabel.setFont(font)
                self.docDOBLabel.setObjectName("docDOBLabel")


        # Date Edit option to Select doctor's DOB 
                self.docDOBDateEdit = QtWidgets.QDateEdit(self.centralwidget)
                self.docDOBDateEdit.setGeometry(410, 330, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docDOBDateEdit.setFont(font)
                self.docDOBDateEdit.setObjectName("docDOBDateEdit")


        # IC/Passport Number For Doctor - Set as label 9
                self.docPassportLabel = QtWidgets.QLabel(self.centralwidget)
                self.docPassportLabel.setGeometry(410, 400, 250, 16)
                self.docPassportLabel.setText("IC/Passport Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docPassportLabel.setFont(font)
                self.docPassportLabel.setObjectName("docPassportLabel")


        # Line Edit for Entering Doctor's IC/Passport Number
                self.docPassportLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docPassportLineEdit.setGeometry(410, 420, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docPassportLineEdit.setFont(font)
                self.docPassportLineEdit.setObjectName("docPassportLineEdit")
                self.docPassportLineEdit.setPlaceholderText("example - 1232123xx")


        # Highest Achievement & Verification Documents Attachment 
                self.docAttachmentLabel = QtWidgets.QLabel(self.centralwidget)
                self.docAttachmentLabel.setGeometry(410, 490, 250, 16)
                self.docAttachmentLabel.setText("Verification Documents")
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
                self.docAttachmentLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docAttachmentLineEdit.setGeometry(410, 510, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docAttachmentLineEdit.setFont(font)
                self.docAttachmentLineEdit.setObjectName("docAttachmentLineEdit")
                self.docAttachmentLineEdit.setPlaceholderText("Attach Certificates")
                self.docAttachmentLineEdit.setDisabled(True)

                self.doctorAttachDocumentButton = QtWidgets.QPushButton("+",self.centralwidget)
                self.doctorAttachDocumentButton.setGeometry(620, 510, 40, 40)
                self.doctorAttachDocumentButton.clicked.connect(self.doctorAttachDocument)

                self.doctorRemoveDocumentButton = QtWidgets.QPushButton("Remove file", self.centralwidget)
                self.doctorRemoveDocumentButton.setGeometry(410, 550, 100, 20)
                self.doctorRemoveDocumentButton.clicked.connect(self.doctorRemoveDocument)
                self.doctorRemoveDocumentButton.setDisabled(True)


        # Years of Experience for Doctor - Set as Label 10
                self.docExpLabel = QtWidgets.QLabel(self.centralwidget)
                self.docExpLabel.setGeometry(720, 220, 250, 16)
                self.docExpLabel.setText("How many Years of Experience")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docExpLabel.setFont(font)
                self.docExpLabel.setObjectName("docExpLabel")


        # Line Edit for Entering Doc's Years of Experience
                self.docExpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docExpLineEdit.setGeometry(720, 240, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docExpLineEdit.setFont(font)
                self.docExpLineEdit.setObjectName("docExpLineEdit")
                self.docExpLineEdit.setPlaceholderText("example - 5 years")


        # Doctor's Password - Set as Label 11
                self.docPasswordLabel = QtWidgets.QLabel(self.centralwidget)
                self.docPasswordLabel.setGeometry(720, 310, 250, 16)
                self.docPasswordLabel.setText("Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docPasswordLabel.setFont(font)
                self.docPasswordLabel.setObjectName("docPasswordLabel")
                

        # Line Edit for Entering Doctor's Password
                self.docPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docPasswordLineEdit.setGeometry(720, 330, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docPasswordLineEdit.setFont(font)
                self.docPasswordLineEdit.setObjectName("docPasswordLineEdit")
                self.docPasswordLineEdit.setPlaceholderText("example - SoMeThiNg@123")
                self.docPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.docPasswordLineEdit.textChanged.connect(self.docValidatePasswordMatch)

                self.docShowPasswordCheckBox = QtWidgets.QCheckBox("Show Password", self.centralwidget)
                self.docShowPasswordCheckBox.setGeometry(720, 360, 250, 40)
                self.docShowPasswordCheckBox.stateChanged.connect(self.docTogglePasswordVisibility)
                
                
        # Confirmation of Password for Doctor - Set as Label 14
                self.docReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
                self.docReEnterPassLabel.setGeometry(720, 400, 250, 16)
                self.docReEnterPassLabel.setText("Confirm Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.docReEnterPassLabel.setFont(font)
                self.docReEnterPassLabel.setObjectName("docReEnterPassLabel")
                
                
        # Line Edit for Entering the password of Doctor Again
                self.docReEnterPassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.docReEnterPassLineEdit.setGeometry(720, 420, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.docReEnterPassLineEdit.setFont(font)
                self.docReEnterPassLineEdit.setObjectName("docReEnterPassLineEdit")
                self.docReEnterPassLineEdit.setPlaceholderText("Re-enter Password")
                self.docReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.docReEnterPassLineEdit.textChanged.connect(self.docValidatePasswordMatch)
                
                self.docShowRePasswordCheckbox = QtWidgets.QCheckBox("Show Password", self.centralwidget)
                self.docShowRePasswordCheckbox.setGeometry(720, 450, 250, 40)
                self.docShowRePasswordCheckbox.stateChanged.connect(self.docToggleReEnterPasswordVisibility)

                
        # PushButton for registering - Saves Data of Doctor        
                self.docRegisterPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.docRegisterPushButton.setGeometry(410, 580, 250, 41)
                self.docRegisterPushButton.setText("Register")
                
                #Style Sheet Code for Register vvvvvvvvvvvvvvvvvvvvvv
                stylesheet2 = """
                QPushButton {
                        background-color: rgb(53, 63, 203);
                        color: rgb(255, 255, 255);
                }

                QPushButton:disabled {
                        background-color: rgb(53, 63, 203);
                        color: rgb(120, 120, 120);
                }
                """

                #Style Sheet Code for Register End ^^^^^^^^^^^^^^^^^^^^^^^
                self.docRegisterPushButton.setStyleSheet(stylesheet2)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                self.docRegisterPushButton.setFont(font)
                self.docRegisterPushButton.setAutoFillBackground(False)
                self.docRegisterPushButton.setObjectName("Register")
                self.docRegisterPushButton.clicked.connect(lambda checked: self.saveData())



        # Push Button for Going Back to Login Page
                self.docGoBackLoginPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.docGoBackLoginPushButton.setGeometry(410, 640, 250, 41)
                self.docGoBackLoginPushButton.setText("Go Back To Login")

                #Style SHeet code for Transparent Block white differnt text color vvvvvvvv
                stylesheet = """
                QPushButton {
                        background-color: rgba(255, 255, 255, 10);
                        color: rgb(225, 225, 225);
                        text-decoration: underline;
                }

                QPushButton:disabled {
                         background-color: rgba(255, 255, 255, 10);
                         color: rgb(120, 120, 120);
                }
                """
                #Style Sheet code for transparent Block End ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                self.docGoBackLoginPushButton.setStyleSheet(stylesheet)
                self.docGoBackLoginPushButton.setAutoFillBackground(False)
                self.docGoBackLoginPushButton.setObjectName("docGoBackLoginPushButton")
                self.docGoBackLoginPushButton.clicked.connect(self.docGoBackLogin)

                
        # Icon For LOGO - Set as Label 12 (Need to Add Image)
                self.docPageLogo = QtWidgets.QLabel(self.centralwidget)
                self.docPageLogo.setGeometry(700, 30, 400, 150)
                self.docPageLogo.setObjectName("docPageLogo")
                filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo.png")
                
                self.doctorRegisterLogoIcon = QPixmap(filepath)
                self.doctorRegisterLogoIcon = self.doctorRegisterLogoIcon.scaled(300, 300)
                self.docPageLogo.setPixmap(self.doctorRegisterLogoIcon)
                self.docPageLogo.setStyleSheet("margin-left: 60px;")
        # Code for all Label, Buttons and even the Line Edits ends here ^^^^^^^^^^^^



                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                MainWindow.setWindowTitle("Doctor Registration")
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)


        def saveData(self):
                doctorDocumentPath = self.docAttachmentLineEdit.text()
                files = {'file': ('docCertification.jpg', open(doctorDocumentPath , 'rb'))}

                doctorName  = f'{self.docFirstNameLineEdit.text()} {self.docLastNameLineEdit.text()}'
                doctorEmail = self.docEmailLineEdit.text()
                doctorPassword = self.docPasswordLineEdit.text()
                doctorContact = self.docContactLineEdit.text()
                doctorType = self.docSpecialtyLineEdit.text()
                yearsOfExperience = self.docExpLineEdit.text()
                doctorICNumber = self.docPassportLineEdit.text()
                

                doctorJSON = {
                        "doctorName": doctorName,
                        "doctorPassword": doctorPassword,
                        "doctorICNumber": doctorICNumber,
                        "doctorContact": doctorContact,
                        "doctorType": doctorType,
                        "yearOfExperience": yearsOfExperience,
                        "doctorEmail": doctorEmail,
                        "status": "Inactive",
                }


                docGoRegisterDialogBox = QMessageBox.question(self.centralwidget, "Registration Confirmation",
                                                                "Are you sure you all your details are correct?",
                                                        QMessageBox.Yes | QMessageBox.No)
                if docGoRegisterDialogBox == QMessageBox.Yes:
                                
                        response,registerFlag = Registration.registerDoctor(doctorJSON,files)
                        if registerFlag:
                                pass
                        else:
                                print(response)
                        self.pageManager.goBack()


        def docGoBackLogin(self):
                docGoBackLoginDialogBox = QMessageBox.question(self.centralwidget, "Go Back Login",
                                                                "Are you sure you want to go back?",
                                                QMessageBox.Yes | QMessageBox.No)
                if docGoBackLoginDialogBox == QMessageBox.Yes:
                        self.pageManager.goBack()

        
        def doctorAttachDocument(self):
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                document, _ = QFileDialog.getOpenFileName(self, "Open Documents", "", "All fiels (*)", options=options)

                if document:
                        self.docAttachmentLineEdit.setText(document)
                        self.doctorRemoveDocumentButton.setDisabled(False)


        def doctorRemoveDocument(self):
                self.docAttachmentLineEdit.clear()
                self.doctorRemoveDocumentButton.setDisabled(True)

        
        def docTogglePasswordVisibility(self, state):
                if state == Qt.Checked:
                        self.docPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                        self.docPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        
        def docToggleReEnterPasswordVisibility(self, state):
                if state == Qt.Checked:
                        self.docReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                        self.docReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)


        def docValidatePasswordMatch(self):
                doctorPassword = self.docPasswordLineEdit.text()
                doctorReEnterPassword = self.docReEnterPassLineEdit.text()

                if doctorPassword == doctorReEnterPassword:
                        self.docReEnterPassLineEdit.setStyleSheet("border: 2px solid green;")
                else:
                        self.docReEnterPassLineEdit.setStyleSheet("border: 2px solid red;")