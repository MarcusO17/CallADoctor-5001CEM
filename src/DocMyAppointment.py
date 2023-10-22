import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtWidgets
from .model import Clinic
from .model import Doctor
from .model import Appointment
from .PageManager import PageManager


class DocMyAppointmentWindow(QMainWindow):
    def __init__(self):
        super().__init__()