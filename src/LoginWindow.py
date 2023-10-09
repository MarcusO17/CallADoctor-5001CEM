from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore
from PatientHomepage import PatientHomepage
from DoctorHomePage import HomepageWindow
from PatientRegister import PatientRegisterWindow
from ClinicRegister import ClinicRegisterWindow
from DoctorRegister import DoctorRegisterWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedWidth(350)
        self.setFixedHeight(400)
        self.initUI()

    def initUI(self):
        loginFormLayout = QVBoxLayout()
        loginFormLayout.setSpacing(0)
        loginFormLayout.setContentsMargins(20, 20, 20, 20)

        labelFont = QFont()
        labelFont.setFamily("Poppins")
        labelFont.setPointSize(12)

        self.emailLabel = QLabel("Email:")
        self.emailLabel.setFont(labelFont)
        self.emailInput = QLineEdit()

        self.passwordLabel = QLabel("Password:")
        self.passwordLabel.setFont(labelFont)

        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.loginButton = QPushButton("Login")
        self.loginButton.setDefault(True)

        self.loginButton.clicked.connect(self.loginValidation)

        loginFormLayout.addWidget(self.emailLabel)
        loginFormLayout.addWidget(self.emailInput)
        loginFormLayout.addWidget(self.passwordLabel)
        loginFormLayout.addWidget(self.passwordInput)
        loginFormLayout.addWidget(self.loginButton)

        self.setLayout(loginFormLayout)


    def login(self):
        self.patientHomepage = DoctorRegisterWindow()
        self.patientHomepage.show()
        self.close()


    def loginValidation(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()

        #backend
        tempemail = ""
        temppassword = ""

        if email == tempemail and temppassword == temppassword:
            print("login success")
            self.login()
        else:
            print("login failed")




