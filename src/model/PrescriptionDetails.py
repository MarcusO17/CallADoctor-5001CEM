import Prescription
class PrescriptionDetails(Prescription):
    def __init__(self,prescriptionID, appointmentID,expiryDate,medicationName, pillsPerDay, food, dosage):
        super().__init__(prescriptionID, appointmentID,expiryDate)
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
    