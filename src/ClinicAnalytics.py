import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit
from PyQt5 import QtWidgets

from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .model.DoctorRepo import DoctorRepository
from .PageManager import FrameLayoutManager


class ClinicAnalytics(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.generateClinicGraph()


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(self.graphWidget)

        self.setLayout(mainLayout)


    def generateClinicGraph(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        self.graphWidget = QLabel()
        self.graphWidget.setFixedSize(700,500)

        #make your graph here, this is just a place holder
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")

        graphImage = QPixmap(filepath)
        self.graphWidget.setPixmap(graphImage)
        self.graphWidget.setAlignment(Qt.AlignCenter)


