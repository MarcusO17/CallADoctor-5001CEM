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
            recordsListP = responsePrescription.json()

          
            for records in recordsListP:
                  tempPrescription = Prescription("","","")
                  
                  prescriptionID = records['prescriptionID']
                  tempPrescription.setPrescriptionID(records['prescriptionID'])
                  tempPrescription.setAppointmentID(records['appointmentID'])
                  tempPrescription.setExpiryDate(records['expiryDate'])

                  responsePrescriptionDetails = requests.get(f'http://127.0.0.1:5000/prescriptionDetails/{prescriptionID}')
                  recordsListPD = responsePrescriptionDetails.json()

                  for records in recordsListPD:
                     
                        tempPrescriptionDetail = PrescriptionDetails("","","","")
                        tempPrescriptionDetail.setMedicationName(records['medicationName'])
                        tempPrescriptionDetail.setPillsPerDay(records['pillsPerDay'])
                        tempPrescriptionDetail.setFood(records['food'])
                        tempPrescriptionDetail.setDosage(records['dosage'])

                        tempPrescription.setPrescriptionDetails(tempPrescriptionDetail)

                 

              
                  prescriptionList.append(tempPrescription)
            
                        
            return prescriptionList     
      
      def getPrescriptionListByPatient(patientID):
            prescriptionList = []
            prescriptionDetailList = []
            responsePrescription = requests.get(f'http://127.0.0.1:5000/prescriptions/patients/{patientID}')
            recordsListP = responsePrescription.json()

          
            for records in recordsListP:
                  tempPrescription = Prescription("","","")
                  
                  prescriptionID = records['prescriptionID']
                  tempPrescription.setPrescriptionID(records['prescriptionID'])
                  tempPrescription.setAppointmentID(records['appointmentID'])
                  tempPrescription.setExpiryDate(records['expiryDate'])

                  responsePrescriptionDetails = requests.get(f'http://127.0.0.1:5000/prescriptionDetails/{prescriptionID}')
                  recordsListPD = responsePrescriptionDetails.json()

                  for records in recordsListPD:
                     
                        tempPrescriptionDetail = PrescriptionDetails("","","","")
                        tempPrescriptionDetail.setMedicationName(records['medicationName'])
                        tempPrescriptionDetail.setPillsPerDay(records['pillsPerDay'])
                        tempPrescriptionDetail.setFood(records['food'])
                        tempPrescriptionDetail.setDosage(records['dosage'])

                        tempPrescription.setPrescriptionDetails(tempPrescriptionDetail)

                 

              
                  prescriptionList.append(tempPrescription)
            
                        
            return prescriptionList    
      

      def postPrescription(prescription):
            prID = requests.get('http://127.0.0.1:5000/prescriptions/idgen').text

            prescriptionJSON = {
                  "prescriptionID" : prID,
                  "appointmentID": prescription.getAppointmentID(),
                  "expiryDate" : prescription.getExpiryDate()
            }

            requests.post(f'http://127.0.0.1:5000/prescriptions',
                                           json=prescriptionJSON)
            
            for items in prescription.getPrescriptionDetails():
                  prescriptionDetailsJSON = {
                        "prescriptionID" : prID,
                        "appointmentID"  : prescription.getAppointmentID(),
                        "medicationName" : items.getMedicationName(),
                        "pillsPerDay"    : items.getPillsPerDay(),
                        "food"           : items.getFood(),
                        "dosage"         : items.getDosage(),
                  }

                  requests.post(f'http://127.0.0.1:5000/prescriptionDetails',
                                           json=prescriptionDetailsJSON)
                  
                  
           
         

     

      

