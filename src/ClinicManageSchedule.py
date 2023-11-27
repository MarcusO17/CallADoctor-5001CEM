import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .model.DoctorRepo import DoctorRepository
from .PageManager import FrameLayoutManager


class ClinicManageSchedule(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Manage Schedule")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setGeometry(QRect(80, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                            background: #D0BFFF;
                                            border-radius: 10px;
                                            }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QRect(80, 120, 800, 40))
        self.searchBar.setPlaceholderText("    Search Bar")
        self.searchBar.textChanged.connect(self.filterButtons)
        self.searchBar.setStyleSheet("""QLineEdit {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                }""")

        self.buttonContainer = QWidget()
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 100px;
                                                    }""")

        self.generateScheduleButtons()

        self.buttonContainer.setContentsMargins(20,20,20,20)
        buttonLayout = QVBoxLayout(self.buttonContainer)
        buttonLayout.setSpacing(20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setWidgetResizable(True)

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(900, 500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                            background: #D0BFFF;
                                            border-radius: 10px;
                                            margin-left: 80px;
                                            }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)
    def doctorButtonFunction(self, doctor, clinic):
        self.doctorSchedule = ClinicDetailedSchedule(doctor, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorSchedule)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def filterButtons(self):
        searchedText = self.searchBar.text().strip().lower()

        for i in range(self.buttonContainer.layout().count()):
            item = self.buttonContainer.layout().itemAt(i)
            if item and isinstance(item.widget(), QPushButton):
                button = item.widget()
                text = button.text().lower()
                button.setVisible(searchedText in text)

    def generateScheduleButtons(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            print("in the loop ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget")

        doctorList = DoctorRepository.getDoctorListClinic(self.clinic.getClinicID())

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-calendar-64.png")
        scheduleIcon = QIcon(filepath)

        for count, doctor in enumerate(doctorList):
            doctorButton = QPushButton()
            doctorButton.setText(f"    {doctor.getDoctorID()} - {doctor.getDoctorName()}")
            doctorButton.setFont(buttonFont)
            doctorButton.setIconSize(QSize(80, 80))
            doctorButton.setFixedSize(QSize(700, 100))
            doctorButton.setIcon(scheduleIcon)
            doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))
            doctorButton.setStyleSheet("""QPushButton {
                                                            background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                    stop: 0 rgba(10, 2, 85, 255), 
                                                                                    stop: 1 rgba(59, 41, 168, 255));
                                                            border-radius: 10px; color: white;
                                                            text-align: left; 
                                                            padding-left: 20px;
                                                            }
                                                            QPushButton:hover
                                                            {
                                                              background-color: #7752FE;
                                                              text-align: left; 
                                                              padding-left: 20px;
                                                            }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            doctorButton.setGraphicsEffect(effect)

            self.buttonContainer.layout().addWidget(doctorButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)