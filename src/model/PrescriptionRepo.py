import requests
from .Prescription import Prescription
from .Prescription import PrescriptionDetails

class PrescriptionRepository():
        
      def __init__(self):
            self.prescriptionDetailList = []


      def getPrescriptionDetailList():
            prescriptionDetailList = []
            response = requests.get('http://127.0.0.1:5000/prescriptions')
            recordsList = response.json()
            for records in recordsList:
                  tempPrescription = Prescription("","","","","")
                  tempPrescriptionDetail = PrescriptionDetails("","","","")

                  tempPrescription.setPrescriptionID(records['prescriptionID'])
                  tempPrescription.setAppointmentID(records['appointmentID'])
                  tempPrescriptionDetail.setMedicationName(records['medicationName'])
                  tempPrescriptionDetail.setPillsPerDay(records['pillsPerDay'])
                  tempPrescriptionDetail.setFood(records['food'])
                  tempPrescriptionDetail.setDosage(records['dosage'])

                  prescriptionDetailList.append(tempPrescription, tempPrescriptionDetail)
                  
            return prescriptionDetailList      
      
     

      

