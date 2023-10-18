class Prescription:
    def __init__(self,prescriptionID, appointmentID, medicationName, pillsPerDay, food, dosage):
        self.prescriptionID = prescriptionID
        self.appointmentID = appointmentID
        self.medicationName = medicationName
        self.pillsPerDay = pillsPerDay
        self.food = food
        self.dosage = dosage

    def getPrescriptionID(self):
        return self.prescriptionID

    def setPrescriptionID(self, prescriptionID):
        self.prescriptionID = prescriptionID

    def getAppointmentID(self):
        return self.appointmentID

    def setAppointmentID(self, appointmentID):
        self.appointmentID = appointmentID

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
    