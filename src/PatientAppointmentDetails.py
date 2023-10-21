import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea
from PyQt5 import QtCore, QtWidgets
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .PageManager import PageManager


class PatientAppointmentDetailsWindow(QMainWindow):

    def __init__(self, appointmentTemp):
        super().__init__()
        self.pageManager = PageManager()