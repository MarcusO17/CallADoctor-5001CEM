from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton


class PatientHomepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Homepage")
        self.setGeometry(100, 100, 400, 300)

        headerFont = QFont()
        headerFont.setFamily("Poppins")
        headerFont.setBold(True)
        headerFont.setPointSize(48)

        patientHomepageLayout = QVBoxLayout()

        title = QLabel("Welcome!")
        title.setFont(headerFont)
        patientHomepageLayout.addWidget(title)

        central_widget = QWidget()
        central_widget.setLayout(patientHomepageLayout)
        self.setCentralWidget(central_widget)



