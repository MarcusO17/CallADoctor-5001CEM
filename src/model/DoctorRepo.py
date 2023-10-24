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
      
      def getDoctor(doctorID):
            try:
                  response = requests.get(f'http://127.0.0.1:5000/doctors/{doctorID}')
                  doctor = response.json()[0]
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return Doctor("","","","","","","","")
          
            tempDoctor = Doctor("","","","","","","","")

            tempDoctor.setClinicID(doctor['clinicID'])
            tempDoctor.setDoctorID(doctor['doctorID'])
            tempDoctor.setDoctorName(doctor['doctorName'])
            tempDoctor.setStatus(doctor['status'])
            tempDoctor.setDoctorType(doctor['doctorType'])
            tempDoctor.setDoctorContact(doctor['doctorContact'])
            tempDoctor.setDoctorICNumber(doctor['doctorICNumber'])
            tempDoctor.setYearOfExperience(doctor['yearOfExperience'])

            return tempDoctor   
      

      
      def getDoctorListClinic(clinicID):
            doctorList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/doctors/clinics/{clinicID}')
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
      

      def getUnassignedDoctors():
            doctorList = []
            try:
                  response = requests.get('http://127.0.0.1:5000/doctors/unassigned')
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


      def assignDoctorClinic(clinicID,doctorID):
            response = requests.patch(f'http://127.0.0.1:5000/doctors/{clinicID}/assign/{doctorID}')
            assignStatus = response.text

            if response.status_code == 200:
                  return assignStatus, True
            else:
                  return assignStatus, False

      def unassignDoctorClinic(doctorID):
            response = requests.patch(f'http://127.0.0.1:5000/doctors/unassign/{doctorID}')
            assignStatus = response.text

            if response.status_code == 200:
                  return assignStatus, True
            else:
                  return assignStatus, False
