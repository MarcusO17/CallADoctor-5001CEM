from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore

class HomepageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomepageWindow()
        self.ui.setupUi(self)
    
class Ui_HomepageWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
#Push Button 1 (Schedule Button)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("schedule")


#Push button_2 (Patient Record)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 150, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("PatientRecord")


#Icon for Schedule - set as label 1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 170, 51, 51))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")


#icon for Patient Record - set as label 2        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 170, 51, 51))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")


#Push Button 3 (My Appointments)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 310, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("MyAppointments")


#icon for My Appointments - set as label 3
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 330, 51, 51))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")


#icon for the mainpage LOGO - set as Label 4
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")


#Main Page Title - Set as Label 5
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 40, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setObjectName("label_5")


#Push Button 4 (My Account)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 40, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("MyAccount")


#Push Button 5 (Log Out)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 40, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("LogOut")


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Schedule"))
        self.pushButton_2.setText(_translate("MainWindow", "          Patient Record"))
        self.label.setText(_translate("MainWindow", "Icon"))
        self.label_2.setText(_translate("MainWindow", "Icon"))
        self.pushButton_3.setText(_translate("MainWindow", "          My Appointments"))
        self.label_3.setText(_translate("MainWindow", "Icon"))
        self.label_4.setText(_translate("MainWindow", "LOGO"))
        self.label_5.setText(_translate("MainWindow", "Welcome Dr.Username!"))
        self.pushButton_4.setText(_translate("MainWindow", "My Account"))
        self.pushButton_5.setText(_translate("MainWindow", "Log out"))