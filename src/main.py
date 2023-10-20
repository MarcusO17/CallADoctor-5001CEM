import sys
import os
from PyQt5.QtWidgets import QApplication
from LoginWindow import LoginWindow
from PatientRegister import PatientRegisterWindow
from DoctorRegister import DoctorRegisterWindow

def main():
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()