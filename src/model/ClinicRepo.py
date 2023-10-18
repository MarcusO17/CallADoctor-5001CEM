import requests
from Clinic import Clinic

class ClinicRepository():
        
      def __init__(self):
            self.clinicList = []


      def getClinicList():
            clinicList = []
            response = requests.get('http://127.0.0.1:5000/clinics')
            recordsList = response.json()
            for records in recordsList:
                  tempClinic = Clinic("","","","","")

                  tempClinic.setClinicID(records['clinicID'])
                  tempClinic.setClinicName(records['clinicName'])
                  tempClinic.setClinicAddress(records['address'])
                  tempClinic.setClinicContact(records['clinicContact'])
                  tempClinic.setClinicStatus(records['governmentApproved'])

                  clinicList.append(tempClinic)
                  
            return clinicList      
      
     

      

