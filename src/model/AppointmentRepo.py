from .Appointment import Appointment
from .Patient import Patient
import requests
from datetime import timedelta

class AppointmentRepository():

      def getAppointmentsWeekly(doctorID):
            """Converts Weekly Appointments into Appointment Objects
            """
            appointmentList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/week/{doctorID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                tempAppointment = Appointment("","","","","","","","","")
                
                tempAppointment.setAppointmentID(records['appointmentID'])
                tempAppointment.setDoctorID(records['doctorID'])
                tempAppointment.setClinicID(records['clinicID'])
                tempAppointment.setPatientID(records['patientID'])
                tempAppointment.setAppointmentStatus(records['appointmentStatus'])
                tempAppointment.setStartTime(records['startTime'])
                tempAppointment.setEndTime(records['startTime'])
                tempAppointment.setAppointmentDate(records['appointmentDate'])
                tempAppointment.setVisitReason(records['visitReasons'])
                
                appointmentList.append(tempAppointment)
                  
            return appointmentList      
      
      def getAppointmentsPending(clinicID):
            """Converts Pending Appointments into Appointment Objects
            """
            appointmentList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/{clinicID}/pending')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                tempAppointment = Appointment("","","","","","","","","")
                
                tempAppointment.setAppointmentID(records['appointmentID'])
                tempAppointment.setDoctorID(records['doctorID'])
                tempAppointment.setClinicID(records['clinicID'])
                tempAppointment.setPatientID(records['patientID'])
                tempAppointment.setAppointmentStatus(records['appointmentStatus'])
                tempAppointment.setStartTime(records['startTime'])
                tempAppointment.setEndTime(records['startTime'])
                tempAppointment.setAppointmentDate(records['appointmentDate'])
                tempAppointment.setVisitReason(records['visitReasons'])
                
                appointmentList.append(tempAppointment)
                  
            return appointmentList      
     
      def getAppointmentsByDoctor(doctorID):
            """Converts Appointments depending on DoctorID into Appointment Objects
            """
            appointmentList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/doctor/{doctorID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                tempAppointment = Appointment("","","","","","","","","")
                
                tempAppointment.setAppointmentID(records['appointmentID'])
                tempAppointment.setDoctorID(records['doctorID'])
                tempAppointment.setClinicID(records['clinicID'])
                tempAppointment.setPatientID(records['patientID'])
                tempAppointment.setAppointmentStatus(records['appointmentStatus'])
                tempAppointment.setStartTime(records['startTime'])
                tempAppointment.setEndTime(records['startTime'])
                tempAppointment.setAppointmentDate(records['appointmentDate'])
                tempAppointment.setVisitReason(records['visitReasons'])
                
                appointmentList.append(tempAppointment)
                  
            return appointmentList 
      

      def getAppointmentsByPatients(patientID):
            """Converts Appointments depending on PatientID into Appointment Objects
            """
            appointmentList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/past/{patientID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                tempAppointment = Appointment("","","","","","","","","")
                
                tempAppointment.setAppointmentID(records['appointmentID'])
                tempAppointment.setDoctorID(records['doctorID'])
                tempAppointment.setClinicID(records['clinicID'])
                tempAppointment.setPatientID(records['patientID'])
                tempAppointment.setAppointmentStatus(records['appointmentStatus'])
                tempAppointment.setStartTime(records['startTime'])
                tempAppointment.setEndTime(records['startTime'])
                tempAppointment.setAppointmentDate(records['appointmentDate'])
                tempAppointment.setVisitReason(records['visitReasons'])
                
                appointmentList.append(tempAppointment)
                  
            return appointmentList 
      
      def getDoctorDashboardAppointments(doctorID):
            """Converts Appointments to be listed on the doctor's dashboard into Appointment Objects
            """
            appointmentList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/upcoming/doctor/{doctorID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                tempAppointment = Appointment("","","","","","","","","")
                
                tempAppointment.setAppointmentID(records['appointmentID'])
                tempAppointment.setDoctorID(records['doctorID'])
                tempAppointment.setClinicID(records['clinicID'])
                tempAppointment.setPatientID(records['patientID'])
                tempAppointment.setAppointmentStatus(records['appointmentStatus'])
                tempAppointment.setStartTime(records['startTime'])
                tempAppointment.setEndTime(records['startTime'])
                tempAppointment.setAppointmentDate(records['appointmentDate'])
                tempAppointment.setVisitReason(records['visitReasons'])
                
                appointmentList.append(tempAppointment)
                  
            return appointmentList
      
      def getPatientDashboardAppointments(patientID):
            """Converts Patient Dashboard Appointments into Appointment Objects
            """
            appointmentList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/upcoming/patient/{patientID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                tempAppointment = Appointment("","","","","","","","","")
                
                tempAppointment.setAppointmentID(records['appointmentID'])
                tempAppointment.setDoctorID(records['doctorID'])
                tempAppointment.setClinicID(records['clinicID'])
                tempAppointment.setPatientID(records['patientID'])
                tempAppointment.setAppointmentStatus(records['appointmentStatus'])
                tempAppointment.setStartTime(records['startTime'])
                tempAppointment.setEndTime(records['startTime'])
                tempAppointment.setAppointmentDate(records['appointmentDate'])
                tempAppointment.setVisitReason(records['visitReasons'])
                
                appointmentList.append(tempAppointment)
                  
            return appointmentList

      def getPatientLocations(clinicID):
            """Get's patients from today's appointments
            """
            patientList = []
            try:
                  response = requests.get(f'http://127.0.0.1:5000/appointments/today/{clinicID}')
                  recordsList = response.json()
            except requests.RequestException as e:
                  print(f'Error : {e}')
                  return []

            for records in recordsList:
                 patientList.append(Patient.getPatientfromID(records['patientID']))
          
                  
                  
            return patientList


      

