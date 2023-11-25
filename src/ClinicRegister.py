import os
import sys
import base64
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QMessageBox, QFileDialog, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from .PageManager import PageManager
from .model import Registration

class ClinicRegisterWindow(QtWidgets.QMainWindow):
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


        # Main Title for Clinic Register set as Label
                self.clinicRegMainTitle = QtWidgets.QLabel(self.centralwidget)
                self.clinicRegMainTitle.setGeometry(35, 50, 541, 51)
                self.clinicRegMainTitle.setText("Registration for Call-A-Doctor!")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(28)
                font.setBold(True)
                font.setWeight(75)
                self.clinicRegMainTitle.setFont(font)
                self.clinicRegMainTitle.setObjectName("clinicRegMainTitle")

        # Sub Title for Clinic Register set as Label 2
                self.clinicRegSubTitle = QtWidgets.QLabel(self.centralwidget)
                self.clinicRegSubTitle.setGeometry(35, 100, 451, 41)
                self.clinicRegSubTitle.setText("Get your Clinic registered now!")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.clinicRegSubTitle.setFont(font)
                self.clinicRegSubTitle.setObjectName("clinicRegSubTitle")


        # Name Of Clinic - Set As Label 5
                self.clinicNameLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicNameLabel.setGeometry(90, 220, 250, 21)
                self.clinicNameLabel.setText("Name of Clinic")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicNameLabel.setFont(font)
                self.clinicNameLabel.setObjectName("clinicNameLabel")


        # Line Edit for Entering Clinic Name
                self.clinicNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicNameLineEdit.setGeometry(90, 240, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicNameLineEdit.setFont(font)
                self.clinicNameLineEdit.setObjectName("clinicNameLineEdit")
                self.clinicNameLineEdit.setPlaceholderText("example - ABCD Clinic")


        # Address of Clinic - Set as Label 4
                self.clinicAddressLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicAddressLabel.setGeometry(90, 310, 250, 16)
                self.clinicAddressLabel.setText("Address of Clinic")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicAddressLabel.setFont(font)
                self.clinicAddressLabel.setObjectName("clinicAddressLabel")


        # Line Edit for Entering the Clinic Address
                self.clinicAddressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicAddressLineEdit.setGeometry(90, 330, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicAddressLineEdit.setFont(font)
                self.clinicAddressLineEdit.setObjectName("clinicAddressLineEdit")
                self.clinicAddressLineEdit.setPlaceholderText("example - Bayan Lepas, Penang")


        # Clinic Contact Number - Set as Label 6
                self.clinicContactLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicContactLabel.setGeometry(90, 400, 250, 16)
                self.clinicContactLabel.setText("Clinic Contact Number")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicContactLabel.setFont(font)
                self.clinicContactLabel.setObjectName("clinicContactLabel")


        # Line Edit for Entering Clinic Contact Number 
                self.clinicContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicContactLineEdit.setGeometry(90, 420, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicContactLineEdit.setFont(font)
                self.clinicContactLineEdit.setObjectName("clinicContactLineEdit")
                self.clinicContactLineEdit.setPlaceholderText("example - +60xxxxxxxx")


        # Clinic Email - Set as Label 7
                self.clinicEmailLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicEmailLabel.setGeometry(410, 220, 250, 16)
                self.clinicEmailLabel.setText("Clinic Email")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicEmailLabel.setFont(font)
                self.clinicEmailLabel.setObjectName("clinicEmailLabel")


        # Line Edit for Entering Clinic Email
                self.clinicEmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicEmailLineEdit.setGeometry(410, 240, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicEmailLineEdit.setFont(font)
                self.clinicEmailLineEdit.setObjectName("clinicEmailLineEdit")
                self.clinicEmailLineEdit.setPlaceholderText("example - abcklinik@new.com")


        # Verification Document - Set as Label 9
                self.clinicDocumentLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicDocumentLabel.setGeometry(410, 310, 250, 16)
                self.clinicDocumentLabel.setText("Verification Document")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicDocumentLabel.setFont(font)
                self.clinicDocumentLabel.setObjectName("clinicDocumentLabel")


        # Actually for Now I set this Line Edit to show Attachnent of Document
        # But need to change the functionality of this, probably into a push button
        # which would allow to open file explorer to attach Document 
                self.clinicDocumentLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicDocumentLineEdit.setGeometry(410, 330, 250, 40)
                self.clinicDocumentLineEdit.setDisabled(True)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicDocumentLineEdit.setFont(font)
                self.clinicDocumentLineEdit.setObjectName("clinicDocumentLineEdit")
                self.clinicDocumentLineEdit.setPlaceholderText("Attach Certification Document")

                self.uploadDocumentButton = QtWidgets.QPushButton("+", self.centralwidget)
                self.uploadDocumentButton.setGeometry(620, 330, 40, 40)
                self.uploadDocumentButton.clicked.connect(self.uploadDocument)

                self.clinicRemoveDocumentButton = QtWidgets.QPushButton("Remove file", self.centralwidget)
                self.clinicRemoveDocumentButton.setGeometry(410, 370, 100, 20)
                self.clinicRemoveDocumentButton.clicked.connect(self.clinicRemoveDocument)
                self.clinicRemoveDocumentButton.setDisabled(True)


        # Clinic Password - Set as Label 10 
                self.clinicPasswordLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicPasswordLabel.setGeometry(720, 220, 250, 16)
                self.clinicPasswordLabel.setText("Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicPasswordLabel.setFont(font)
                self.clinicPasswordLabel.setObjectName("clinicPasswordLabel")


        # Line Edit for Clinic to Enter the Password
        # (Validation needs constraints like passwords needs to have - 
        # Minimum 8 characters, upper case and lower case letters, numbers
        # and Special Characters)
                self.clinicPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicPasswordLineEdit.setGeometry(720, 240, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicPasswordLineEdit.setFont(font)
                self.clinicPasswordLineEdit.setObjectName("clinicPasswordLineEdit")
                self.clinicPasswordLineEdit.setPlaceholderText("example - SoMeThiNg@123")
                self.clinicPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.clinicPasswordLineEdit.textChanged.connect(self.validatePasswordMatch)

                self.showPasswordCheckbox = QtWidgets.QCheckBox("Show Password", self.centralwidget)
                self.showPasswordCheckbox.setGeometry(720, 270, 250, 40)
                self.showPasswordCheckbox.stateChanged.connect(self.togglePasswordVisibility)


        # Confirm Password for CLinic - Set as Label 11
                self.clinicReEnterPassLabel = QtWidgets.QLabel(self.centralwidget)
                self.clinicReEnterPassLabel.setGeometry(720, 310, 250, 16)
                self.clinicReEnterPassLabel.setText("Confirm Password")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.clinicReEnterPassLabel.setFont(font)
                self.clinicReEnterPassLabel.setObjectName("clinicReEnterPassLabel")


        # Line Edit for Clinic to Enter Password again to confirm
        # need validation to check if previously written password and
        # re-entered password same or not, if not, error 404)
                self.clinicReEnterPassLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.clinicReEnterPassLineEdit.setGeometry(720, 330, 250, 40)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.clinicReEnterPassLineEdit.setFont(font)
                self.clinicReEnterPassLineEdit.setObjectName("clinicReEnterPassLineEdit")
                self.clinicReEnterPassLineEdit.setPlaceholderText("Re-enter Password")
                self.clinicReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.clinicReEnterPassLineEdit.textChanged.connect(self.validatePasswordMatch)

                self.showRePasswordCheckbox = QtWidgets.QCheckBox("Show Password", self.centralwidget)
                self.showRePasswordCheckbox.setGeometry(720, 360, 250, 40)
                self.showRePasswordCheckbox.stateChanged.connect(self.toggleReEnterPasswordVisibility)


                self.clinicNameLineEdit.textChanged.connect(self.removeHighlight)
                self.clinicAddressLineEdit.textChanged.connect(self.removeHighlight)
                self.clinicContactLineEdit.textChanged.connect(self.removeHighlight)
                self.clinicEmailLineEdit.textChanged.connect(self.removeHighlight)
                self.clinicPasswordLineEdit.textChanged.connect(self.removeHighlight)
                self.clinicReEnterPassLineEdit.textChanged.connect(self.removeHighlight)
                
        # Register PushButton For Registering Account - Saves the Data
                self.clinicRegisterPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.clinicRegisterPushButton.setGeometry(410, 580, 250, 41)
                self.clinicRegisterPushButton.setText("Register")

        # DONT MIND THIS - This is just me editing the STYLE SHEET for
        # the button to have color, and the text being White
                stylesheet4 = """
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
                self.clinicRegisterPushButton.setFont(font)
                self.clinicRegisterPushButton.setAutoFillBackground(False)
                self.clinicRegisterPushButton.setStyleSheet(stylesheet4)
                self.clinicRegisterPushButton.setObjectName("clinicRegisterPushButton")
                self.clinicRegisterPushButton.clicked.connect(lambda checked: self.clinicSaveData())

                

                self.clinicRegisterGoBackLogin = QtWidgets.QPushButton(self.centralwidget)
                self.clinicRegisterGoBackLogin.setGeometry(410, 640, 250, 41)
                self.clinicRegisterGoBackLogin.setText("Go Back To Login")

        # Style Sheet Code for the transparent button start here vvvvvvvv
                stylesheet3 = """
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
        # Style Sheet code ends here ^^^^^^^^^^^^^^^

                self.clinicRegisterGoBackLogin.setAutoFillBackground(False)
                self.clinicRegisterGoBackLogin.setStyleSheet(stylesheet3)
                self.clinicRegisterGoBackLogin.setObjectName("clinicGoBackLogin")
                self.clinicRegisterGoBackLogin.clicked.connect(self.clinicGoBackLogin)
                
                
        # Icon For LOGO - Set as Label 12 (Need to Add Image)
                self.clinicRegisterLogo = QtWidgets.QLabel(self.centralwidget)
                self.clinicRegisterLogo.setGeometry(700, 30, 400, 150)
                self.clinicRegisterLogo.setObjectName("clinicRegisterLogo")
                filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo.png")
                
                self.clinicRegisterLogoIcon = QPixmap(filepath)
                self.clinicRegisterLogoIcon = self.clinicRegisterLogoIcon.scaled(300, 300)
                self.clinicRegisterLogo.setPixmap(self.clinicRegisterLogoIcon)
                self.clinicRegisterLogo.setStyleSheet("margin-left: 60px;")
        # Code for all Label, Buttons and even the Line Edits ends here ^^^^^^^^^^^^

                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                MainWindow.setWindowTitle("ClinicRegister")
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

        def removeHighlight(self):
                sender = self.sender()  # Get the object that triggered the signal
                sender.setStyleSheet("")

        def highlightEmptyFields(self):
                emptyFields = []

                if self.clinicNameLineEdit.text().strip() == "":
                        emptyFields.append(self.clinicNameLineEdit)
                if self.clinicAddressLineEdit.text().strip() == "":
                        emptyFields.append(self.clinicAddressLineEdit)
                if self.clinicContactLineEdit.text().strip() == "":
                        emptyFields.append(self.clinicContactLineEdit)
                if self.clinicEmailLineEdit.text().strip() == "":
                        emptyFields.append(self.clinicEmailLineEdit)
                if self.clinicPasswordLineEdit.text().strip() == "":
                        emptyFields.append(self.clinicPasswordLineEdit)
                if self.clinicReEnterPassLineEdit.text().strip() == "":
                        emptyFields.append(self.clinicReEnterPassLineEdit)

                for field in emptyFields:
                        field.setStyleSheet("border: 2px solid red;")

                return not emptyFields

        def resetFieldStyles(self):
                self.clinicNameLineEdit.setStyleSheet("")
                self.clinicAddressLineEdit.setStyleSheet("")
                self.clinicContactLineEdit.setStyleSheet("")
                self.clinicEmailLineEdit.setStyleSheet("")
                self.clinicPasswordLineEdit.setStyleSheet("")
                self.clinicReEnterPassLineEdit.setStyleSheet("")



        def clinicSaveData(self):
                self.resetFieldStyles()

                if not self.highlightEmptyFields():
                        QMessageBox.critical(self.centralwidget, "Empty Fields", "Please enter all details.")
                        return
                
                if not self.validatePasswordMatch():
                        QMessageBox.critical(self.centralwidget, "Password Mismatch", "Passwords do not match.")
                        return

                documentPath = self.clinicDocumentLineEdit.text()

                if not documentPath:
                        QMessageBox.critical(self.centralwidget, "Missing Document", "Please attach a document.")
                        return

                files = {'file': ('clinicDoc.jpg', open(documentPath, 'rb'))}
                 
                clinicData = {
                "address": f'{self.clinicAddressLineEdit.text()}',
                "clinicName": self.clinicNameLineEdit.text(),
                "clinicContact": self.clinicContactLineEdit.text(),
                "clinicEmail": self.clinicEmailLineEdit.text(),
                "clinicPassword": self.clinicPasswordLineEdit.text()
                }

                #Marcus post to Database here

                clinicGoRegisterDialogBox = QMessageBox.question(self.centralwidget, "Registration Confirmation",
                                                                "Are you sure you all your details are correct?",
                                                        QMessageBox.Yes | QMessageBox.No)
                if clinicGoRegisterDialogBox == QMessageBox.Yes:
                        response,registerFlag = Registration.registerClinic(clinicData,files)
                        if registerFlag:
                                pass
                        else:
                                print(response)
                        self.pageManager.goBack()

        
        def clinicGoBackLogin(self):
                clinicGoBackLoginDialogBox = QMessageBox.question(self.centralwidget, "Go Back Login",
                                                                  "Are you sure you want to go back?",
                                                                  QMessageBox.Yes | QMessageBox.No)
                if clinicGoBackLoginDialogBox == QMessageBox.Yes:
                        self.pageManager.goBack()

        
        def togglePasswordVisibility(self, state):
                if state == Qt.Checked:
                        self.clinicPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                        self.clinicPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)


        def toggleReEnterPasswordVisibility(self, state):
                if state == Qt.Checked:
                        self.clinicReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                        self.clinicReEnterPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        
        def validatePasswordMatch(self):
                password = self.clinicPasswordLineEdit.text()
                reenterPassword = self.clinicReEnterPassLineEdit.text()

                if password != reenterPassword:
                        # Passwords match, Color of the field will be green
                        self.clinicReEnterPassLineEdit.setStyleSheet("border: 2px solid red;")
                        return False
                else:
                        # Passwords do not match, indicate an error, Color of the field will be red
                        self.clinicReEnterPassLineEdit.setStyleSheet("border: 2px solid green;")
                        return True
        

        def uploadDocument(self):
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                document,  _ = QFileDialog.getOpenFileName(self, "Open Documents", "", "All files (*)", options=options)

                if document:
                        self.clinicDocumentLineEdit.setText(document)
                        self.clinicRemoveDocumentButton.setDisabled(False)

        
        def clinicRemoveDocument(self):
                self.clinicDocumentLineEdit.clear()
                self.clinicRemoveDocumentButton.setDisabled(True)