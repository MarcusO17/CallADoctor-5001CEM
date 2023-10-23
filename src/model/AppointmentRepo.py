from .Appointment import Appointment
import requests
from datetime import timedelta

class AppointmentRepository():


      def getAppointmentsWeekly(doctorID):
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
     

      

