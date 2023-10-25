import requests
from .Prescription import Prescription
from .Prescription import PrescriptionDetails

class PrescriptionRepository():
        
      def __init__(self):
            self.prescriptionDetailList = []


      def getPrescriptionListByAppointment(appointmentID):
            prescriptionList = []
            prescriptionDetailList = []
            responsePrescription = requests.get(f'http://127.0.0.1:5000/prescriptions/appointments/{appointmentID}')
            recordsListP = responsePrescription.json()[0]

          
            for records in recordsListP:
                  tempPrescription = Prescription("","","")
                  
                  prescriptionID = records['prescriptionID']
                  tempPrescription.setPrescriptionID(records['prescriptionID'])
                  tempPrescription.setAppointmentID(records['appointmentID'])
                  tempPrescription.setAppointmentID(records['expiryDate'])

                  responsePrescriptionDetails = requests.get(f'http://127.0.0.1:5000/prescriptionsDetails/{prescriptionID}')
                  recordsListPD = responsePrescriptionDetails.json()

                  for records in recordsListPD:
                     
                        tempPrescriptionDetail = PrescriptionDetails("","","","")
                        tempPrescriptionDetail.setMedicationName(records['medicationName'])
                        tempPrescriptionDetail.setPillsPerDay(records['pillsPerDay'])
                        tempPrescriptionDetail.setFood(records['food'])
                        tempPrescriptionDetail.setDosage(records['dosage'])

                        prescriptionDetailList.append(tempPrescriptionDetail)

                  prescriptionDetailList.append(tempPrescriptionDetail)
                  prescriptionDetailList.clear()

                  tempPrescription.setPrescriptionDetails(prescriptionDetailList)
                  prescriptionList.append(tempPrescription)
                        
            return prescriptionList      
      
     

      

