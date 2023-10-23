import requests
from .Doctor import Doctor

class DoctorRepository():
        
      def __init__(self):
            self.DoctorList = []


      def getDoctorList():
            doctorList = []
            try:
                  response = requests.get('http://127.0.0.1:5000/doctors')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return Doctor("","","","","","","")
            for records in recordsList:
                  tempDoctor = Doctor("","","","","","","")

                  tempDoctor.setClinicID = records['clinicID']
                  tempDoctor.setDoctorID = records['doctorID']
                  tempDoctor.setDoctorName = records['doctorName']
                  tempDoctor.setStatus = records['status']
                  tempDoctor.setDoctorType = records['doctorType']
                  tempDoctor.setDoctorContact = records['doctorContact']
                  tempDoctor.setDoctorICNumber = records['doctorICNumber']
                  tempDoctor.setYearOfExperience = records['yearOfExperience']

                  doctorList.append(tempDoctor)
                  
            return doctorList      
      
      def getDoctor(doctorID):
            doctorList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/doctors/{doctorID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return Doctor("","","","","","","","")
            for records in recordsList:
                  tempDoctor = Doctor("","","","","","","","")

                  tempDoctor.setClinicID(records['clinicID'])
                  tempDoctor.setDoctorID(records['doctorID'])
                  tempDoctor.setDoctorName(records['doctorName'])
                  tempDoctor.setStatus(records['status'])
                  tempDoctor.setDoctorType(records['doctorType'])
                  tempDoctor.setDoctorContact(records['doctorContact'])
                  tempDoctor.setDoctorICNumber(records['doctorICNumber'])
                  tempDoctor.setYearOfExperience(records['yearOfExperience'])

                  doctorList.append(tempDoctor)
                  
            return doctorList      
      

      
      def getDoctorList(clinicID):
            doctorList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/doctors/clinic/{clinicID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return Doctor("","","","","","","","")
            for records in recordsList:
                  tempDoctor = Doctor("","","","","","","","")

                  tempDoctor.setClinicID(records['clinicID'])
                  tempDoctor.setDoctorID(records['doctorID'])
                  tempDoctor.setDoctorName(records['doctorName'])
                  tempDoctor.setStatus(records['status'])
                  tempDoctor.setDoctorType(records['doctorType'])
                  tempDoctor.setDoctorContact(records['doctorContact'])
                  tempDoctor.setDoctorICNumber(records['doctorICNumber'])
                  tempDoctor.setYearOfExperience(records['yearOfExperience'])

                  doctorList.append(tempDoctor)
                  
            return doctorList      
      
    
      def getAvailableDoctorList(self,appointmentID):
            doctorList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/{appointmentID}/find')
                  responseList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return Doctor("","","","","","","","")
            
            for doctors in responseList:
                 doctorList.append(self.getDoctor(doctors['doctorID']))
            
            return doctorList
      

