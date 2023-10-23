import requests
from datetime import timedelta, datetime

class Appointment:
    def __init__(self,appointmentID, doctorID, clinicID, patientID, appointmentStatus, startTime, endTime, appointmentDate, visitReason):
        self.appointmentID = appointmentID
        self.doctorID = doctorID
        self.clinicID = clinicID
        self.patientID = patientID
        self.appointmentStatus = appointmentStatus
        self.startTime = startTime
        try:
            self.endTime = str((datetime.strptime(endTime,"%H:%M:%S")+timedelta(hours=1)).time())
        except:
            self.endTime = endTime

        try:
            self.appointmentDate = datetime.strptime(appointmentDate,'%a, %d %b %Y %H:%M:%S %Z').date()
        except:
            self.appointmentDate = appointmentDate

        self.visitReason = visitReason

    def getAppointmentID(self):
        return self.appointmentID

    def setAppointmentID(self, appointmentID):
        self.appointmentID = appointmentID

    def getDoctorID(self):
        return self.doctorID

    def setDoctorID(self, doctorID):
        self.doctorID = doctorID
    
    def getClinicID(self):
        return self.clinicID

    def setClinicID(self, clinicID):
        self.clinicID = clinicID

    def getPatientID(self):
        return self.patientID

    def setPatientID(self, patientID):
        self.patientID = patientID

    def getAppointmentStatus(self):
        return self.appointmentStatus

    def setAppointmentStatus(self, appointmentStatus):
        self.appointmentStatus = appointmentStatus

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, startTime):
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, endTime):
        self.endTime = str((datetime.strptime(endTime,"%H:%M:%S")+timedelta(hours=1)).time())

    def getAppointmentDate(self):
        return self.appointmentDate

    def setAppointmentDate(self, appointmentDate):
        self.appointmentDate = datetime.strptime(appointmentDate,'%a, %d %b %Y %H:%M:%S %Z').date()

    def getVisitReason(self):
        return self.visitReason

    def setVisitReason(self, visitReason):
        self.visitReason = visitReason

    @classmethod
    def getAppointmentfromID(self,appointmentID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/appointments/{appointmentID}')
            appointment = response.json()[0]
        except Exception as e:
            print(e)
            return Appointment("","","","","","","","")
        
        return Appointment(
              appointment['appointmentID'],
              appointment['doctorID'],
              appointment['patientID'],
              appointment['appointmentStatus'],
              appointment['startTime'],
              appointment['startTime'],
              appointment['appointmentDate'],
              appointment['visitReasons'],
        )

    def postAppointment(self):
        newAppointment = {
                    "doctorID": "",
                    "clinicID" : self.getClinicID(),
                    "patientID": self.getPatientID(),
                    "startTime": self.getStartTime(),
                    "appointmentDate": self.getAppointmentDate(),
                    "visitReasons": self.getVisitReason()
        }
        
        response = requests.post(f'http://127.0.0.1:5000/appointments',json=newAppointment)
        postStatus = response.text

        if response.status_code == 201:
            return postStatus, True
        else:
            return postStatus, False
        
    def assignDoctorAppointment(self,doctorID):
        
        response = requests.patch(f'http://127.0.0.1:5000/appointments/{self.getAppointmentID()}/assign/{doctorID}')
        assignedStatus = response.text

        if response.status_code == 200:
            return assignedStatus, True
        else:
            return assignedStatus, False
        
    def denyAppointment(self):
        response = requests.patch(f'http://127.0.0.1:5000/appointments/{self.getAppointmentID()}/deny')
        denyStatus = response.text

        if response.status_code == 200:
            return denyStatus , True
        else:
            return denyStatus , False
        

