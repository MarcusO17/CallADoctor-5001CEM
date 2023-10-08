from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore
from src.PatientHomepage import PatientHomepage


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

        logoLabel = QLabel()

        try:
            logoPixmap = QPixmap("src/resources/logo-placeholder-image.png")  # Replace with the path to your logo image
            logoLabel.setPixmap(logoPixmap)
        except Exception as e:
            print(e)

        field1Layout = QVBoxLayout()
        field2Layout = QVBoxLayout()

        labelFont = QFont()
        labelFont.setFamily("Poppins")
        labelFont.setPointSize(12)

        self.emailLabel = QLabel("Email:")
        self.emailLabel.setFont(labelFont)
        self.emailInput = QLineEdit()
        field1Layout.addWidget(self.emailLabel)
        field1Layout.addWidget(self.emailInput)
        field1Layout.setContentsMargins(0,30,0,20)

        self.passwordLabel = QLabel("Password:")
        self.passwordLabel.setFont(labelFont)
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)

        field2Layout.addWidget(self.passwordLabel)
        field2Layout.addWidget(self.passwordInput)
        field2Layout.setContentsMargins(0, 0, 0, 40)

        self.loginButton = QPushButton("Login")
        self.loginButton.setDefault(True)

        self.loginButton.clicked.connect(self.loginValidation)

        loginFormLayout.addWidget(logoLabel)
        loginFormLayout.addLayout(field1Layout)
        loginFormLayout.addLayout(field2Layout)
        loginFormLayout.addWidget(self.loginButton)
        loginFormLayout.setContentsMargins(30,30,30,60)

        self.setLayout(loginFormLayout)


    def login(self):
        self.patientHomepage = PatientHomepage()
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




