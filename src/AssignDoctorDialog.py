from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout, QWidget, QSizePolicy, QLabel
from PyQt5.QtCore import Qt

from .model import Doctor
from .model.DoctorRepo import DoctorRepository


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

        doctorList = DoctorRepository.getAvailableDoctorList(request.getAppointmentID())

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