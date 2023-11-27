import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets
from .AdminViewClinicDetails import AdminViewClinicDetailsWindow
from .model.Clinic import Clinic
from .model.ClinicRepo import ClinicRepository
from .PageManager import PageManager


class AdminViewClinicsWindow(QMainWindow):
    def __init__(self, adminID):
        super().__init__()
        self.adminID = adminID
        self.pageManager = PageManager()
        self.setWindowTitle("View Clinics Under CaD")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AdminViewClinics")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
        palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)
        self.setStyleSheet(f"QWidget#centralwidget {{background: {gradient}}};")

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Clinics Under CaD")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(225, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-back-64.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonFunction)
        self.backButton.setStyleSheet("""QPushButton#backButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;

                                                        }
                                                        QPushButton#backButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                        }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.backButton.setGraphicsEffect(effect)

        self.buttonContainer = QWidget()
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        buttonLayout = QVBoxLayout(self.buttonContainer)
        buttonLayout.setSpacing(20)
        self.buttonContainer.setContentsMargins(20, 20, 20, 20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Get Clinics
        clinicList = ClinicRepository.getClinicList()

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)

        # Inserting All the Clinics
        for count, clinic in enumerate(clinicList):
            self.clinicButton = QPushButton()
            self.clinicButton.setText(clinic.getClinicID() + " - " + clinic.getClinicName())
            self.clinicButton.setFont(buttonFont)
            self.clinicButton.setFixedSize(QSize(900, 150))
            self.clinicButton.clicked.connect(lambda checked, clinic=clinic: self.clinicButtonFunction(clinic, self.adminID))
            self.buttonContainer.layout().addWidget(self.clinicButton)
            self.clinicButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: center; 
                                                    padding-left: 20px;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: center; 
                                                      padding-left: 20px;
                                                    }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            self.clinicButton.setGraphicsEffect(effect)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000, 500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    }""")

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def clinicButtonFunction(self, clinic, adminID):

        self.adminClinicDetails = AdminViewClinicDetailsWindow(clinic, adminID)
        self.pageManager.add(self.adminClinicDetails)

    def backButtonFunction(self):
        self.pageManager.goBack()