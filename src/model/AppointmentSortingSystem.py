import Appointment
from Doctor import Doctor
from DoctorRepo import DoctorRepository

class AppointmentSortSystem:
    def init(self,clinicID):
        self.appointmentManager = {}
        self.clinicDoctorSet = DoctorRepository.getDoctorList(clinicID=clinicID)
        for doctors in self.clinicDoctorSet:
            self.appointmentManager[doctors] = set('0900','1000','1100',
                                                   '1200','1300','1400',
                                                   '1500','1600')
            
    def insertExistingAppointments():
        

    def findDoctor(self,time):
        for doctors in self.clinicSet:
            if time in self.clinicSet[doctors]:
                return doctors
            else:
                continue
        return False

    def displaySystem(self):
        print(self.appointmentManager)



APS = AppointmentSortSystem("789")

APS.displaySystem()
