from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton


class PatientHomepage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Homepage")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome!")
        layout.addWidget(welcome_label)

        self.setCentralWidget(layout)
