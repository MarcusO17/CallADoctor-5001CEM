import sys

from PyQt5.QtWidgets import QApplication
from LoginWindow import LoginWindow


def main():
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()