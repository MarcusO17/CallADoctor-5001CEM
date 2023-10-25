class Prescription:
    def __init__(self,prescriptionID, appointmentID,expiryDate):
        self.prescriptionID = prescriptionID
        self.appointmentID = appointmentID
        self.expiryDate = expiryDate
        self.prescriptionDetails = []
      
    def getPrescriptionID(self):
        return self.prescriptionID

    def setPrescriptionID(self, prescriptionID):
        self.prescriptionID = prescriptionID

    def getAppointmentID(self):
        return self.appointmentID
    
    def getPrescriptionDetails(self):
        return self.prescriptionDetails

    def setPrescriptionDetails(self, prescriptionDetails):
        self.prescriptionDetails.append(prescriptionDetails)

    def setAppointmentID(self, appointmentID):
        self.appointmentID = appointmentID

    def getExpiryDate(self):
        return self.expiryDate

    def setExpiryDate(self, expiryDate):
        self.expiryDate = expiryDate
    


class PrescriptionDetails():
    def __init__(self,medicationName, pillsPerDay, food, dosage):
        self.medicationName = medicationName
        self.pillsPerDay = pillsPerDay
        self.food = food
        self.dosage = dosage


    def getPillsPerDay(self):
        return self.pillsPerDay

    def setPillsPerDay(self, pillsPerDay):
        self.pillsPerDay = pillsPerDay

    def getMedicationName(self):
        return self.medicationName

    def setMedicationName(self, medicationName):
        self.medicationName = medicationName

    def getFood(self):
        return self.food

    def setFood(self, food):
        self.food = food

    def getDosage(self):
        return self.dosage

    def setDosage(self, dosage):
        self.dosage = dosage
    
  