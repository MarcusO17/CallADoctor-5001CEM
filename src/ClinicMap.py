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


class ClinicMap(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):

        self.centralwidget = QWidget()

        self.generateMapWidget()


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mapWidget)

        self.setLayout(mainLayout)

    def generateMapWidget(self):
        self.mapWidget = QWidget()
        self.mapWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        self.widgetTitle = QLabel()
        self.widgetTitle.setFixedWidth(380)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.widgetTitle.setFont(font)
        self.widgetTitle.setText("Map")

        headerRow = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(200)
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.widgetTitle)

        self.mapWidgetLayout.addLayout(headerRow)
        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)


