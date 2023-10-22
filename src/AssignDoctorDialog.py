from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout, QWidget, QSizePolicy, QLabel
from PyQt5.QtCore import Qt

from .model import Doctor


class AssignDoctorDialog(QDialog):
    def __init__(self, parent=None):
        super(AssignDoctorDialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # Remove close button
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Assign An Appointment")
        self.request = None
        print(self.request)

        self.setFixedSize(600, 600)
        self.layout = QVBoxLayout()

        self.doctorList = list()

        self.doctorButtonLayout = QVBoxLayout()
        self.confirmationButtonLayout = QHBoxLayout()
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        self.doctorButtonList = list()
        self.selectedDoctor = None
        self.selectedButtonIndex = 0

        boxScrollArea.setLayout(self.doctorButtonLayout)
        boxScrollArea.setFixedSize(600, 500)

        self.confirmButton = QPushButton()
        self.confirmButton.setText("Confirm")
        self.confirmButton.clicked.connect(self.confirmButtonFunction)

        self.cancelButton = QPushButton()
        self.cancelButton.setText("Cancel")
        self.cancelButton.clicked.connect(self.cancelButtonFunction)

        self.confirmationButtonLayout.addWidget(self.cancelButton)
        self.confirmationButtonLayout.addWidget(self.confirmButton)

        self.title = QLabel()
        self.title.setText("Select a Doctor to Assign: ")

        self.layout.addWidget(self.title)
        self.layout.addWidget(boxScrollArea)
        self.layout.addLayout(self.confirmationButtonLayout)

        self.setLayout(self.layout)

        print("Finished creating assign doctor dialog")

    def buttonClicked(self, index):
        # logic so the user can only select one of the request
        if self.selectedDoctor == None:
            self.selectedButtonIndex = index
            self.selectedDoctor = self.sender()
            self.selectedDoctor.setChecked(True)
            self.selectedDoctor.setStyleSheet("border: 1px solid red;")
        elif self.selectedDoctor == self.sender():
            pass
        else:
            # return the previous selected to its default style
            self.selectedButtonIndex = index
            self.selectedDoctor.setStyleSheet("")
            self.selectedDoctor.setChecked(False)
            # setting new selected
            self.selectedDoctor = self.sender()
            self.selectedDoctor.setStyleSheet("border: 1px solid red;")
            self.selectedDoctor.setChecked(True)

    def confirmButtonFunction(self):
        # make the changes here
        print("CONFIRM BUTTON TRIGGERED")
        print(self.request.getAppointmentID())
        self.request.setDoctorID(self.doctorList[self.selectedButtonIndex-1].getDoctorID())
        self.close()

    def cancelButtonFunction(self):
        print("CANCEL BUTTON TRIGGERED")
        self.close()

    def setData(self, request):
        self.request = request

        # SET THE AVAILABLE DOCTORS HERE
        doctor1 = Doctor("D0001","Doctor 1", "C0001","AVAILABLE", "Junior", "0123456789", "030102091820", 2)
        doctor2 = Doctor("D0002","Doctor 2", "C0001","AVAILABLE", "Senior", "0198765432", "090502873626", 5)
        self.doctorList.append(doctor1)
        self.doctorList.append(doctor2)

        for count, doctor in enumerate(self.doctorList):
            button = QPushButton()
            button.clicked.connect(lambda checked, index=count: self.buttonClicked(index))
            button.setCheckable(True)
            button.setText(doctor.getDoctorName())
            self.doctorButtonList.append(button)
            self.doctorButtonLayout.addWidget(button)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.doctorButtonLayout.addWidget(spacer)

        print(self.request)