from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
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

        self.emailLabel = QLabel("Email:")
        self.emailInput = QLineEdit()

        self.passwordLabel = QLabel("Password:")
        self.passwordInput = QLineEdit()

        self.loginButton = QPushButton("Login")
        self.loginButton.setDefault(True)

        self.loginButton.clicked.connect(self.login)

        loginFormLayout.addWidget(self.emailLabel)
        loginFormLayout.addWidget(self.emailInput)
        loginFormLayout.addWidget(self.passwordLabel)
        loginFormLayout.addWidget(self.passwordInput)
        loginFormLayout.addWidget(self.loginButton)

        self.setLayout(loginFormLayout)


    def login(self):
        self.patientHomepage = PatientHomepage()
        self.patientHomepage.show()
        self.close()




