import requests
from .Prescription import Prescription

class PrescriptionRepository():
        
      def __init__(self):
            self.prescriptionList = []


      def getPrescriptionList():
            prescriptionList = []
            response = requests.get('http://127.0.0.1:5000/prescriptions')
            recordsList = response.json()
            for records in recordsList:
                  tempPrescription = Prescription("","","","","")

                  tempPrescription.setPrescriptionID(records['prescriptionID'])
                  tempPrescription.setAppointmentID(records['appointmentID'])
                  tempPrescription.setMedicationName(records['medicationName'])
                  tempPrescription.setPillsPerDay(records['pillsPerDay'])
                  tempPrescription.setFood(records['food'])
                  tempPrescription.setDosage(records['dosage'])

                  prescriptionList.append(tempPrescription)
                  
            return prescriptionList      
      
     

      

