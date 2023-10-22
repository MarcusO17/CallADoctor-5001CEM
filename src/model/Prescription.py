class Prescription:
    def __init__(self,prescriptionID, appointmentID,expiryDate):
        self.prescriptionID = prescriptionID
        self.appointmentID = appointmentID
        self.expiryDate = expiryDate
      
    def getPrescriptionID(self):
        return self.prescriptionID

    def setPrescriptionID(self, prescriptionID):
        self.prescriptionID = prescriptionID

    def getAppointmentID(self):
        return self.appointmentID

    def setAppointmentID(self, appointmentID):
        self.appointmentID = appointmentID

    def getAppointmentID(self):
        return self.expiryDate

    def setAppointmentID(self, expiryDate):
        self.expiryDate = expiryDate

  