import unittest
import requests
from unittest.mock import Mock, patch
from src.model import Appointment, AppointmentRepo


class TestAppointment(unittest.TestCase):

    @patch('requests.get')
    def test_getAppointmentfromID_success(self, mockGet):
        # Create a mock response
        mockAppointmentData = {
            "appointmentID" : "A001",
            "doctorID": "D005",
            "clinicID": "392",
            "patientID": "P00004",
            "appointmentStatus" : "Pending",
            "startTime": "14:00",
            "endTime" : "15:00",
            "appointmentDate": "2023-10-12",
            "visitReasons": "Testing"
            }
        
        mockResponse = Mock()
        mockResponse.json.return_value = [mockAppointmentData]
        mockGet.return_value = mockResponse


        # Call the function with a appointment ID
        result = Appointment.getAppointmentfromID("A00299")

        # Assert that the function returned the expected Appointment object
        self.assertEqual(result.getAppointmentID(), mockAppointmentData["appointmentID"])
        self.assertEqual(result.getDoctorID(),  mockAppointmentData["doctorID"])
        self.assertEqual(result.getClinicID(),  mockAppointmentData["clinicID"])
        self.assertEqual(result.getPatientID(),  mockAppointmentData["patientID"])
        self.assertEqual(result.getAppointmentStatus(),  mockAppointmentData["appointmentStatus"])
        self.assertEqual(result.getStartTime(),  mockAppointmentData["startTime"])
        #self.assertEqual(result.getEndTime(),  mockAppointmentData["endTime"])
        self.assertEqual(result.getAppointmentDate(),  mockAppointmentData["appointmentDate"])
        self.assertEqual(result.getVisitReason(),  mockAppointmentData["visitReasons"])
    
    @patch('requests.get')
    def test_getAppointmentfromID_failure(self, mockGet):
        # Create a mock response
        mockAppointmentData = {}
        mockResponse = Mock()
        mockResponse.json.return_value = [mockAppointmentData]
        mockGet.return_value = mockResponse


        # Call the function with a appointment ID
        result = Appointment.getAppointmentfromID("A0031239")

        # Assert that the function returned the expected Appointment object
        self.assertEqual(result.getAppointmentID(),"")
        self.assertEqual(result.getDoctorID(), "")
        self.assertEqual(result.getClinicID(), "")
        self.assertEqual(result.getPatientID(), "")
        self.assertEqual(result.getAppointmentStatus(),  "")
        self.assertEqual(result.getStartTime(),  "")
        #self.assertEqual(result.getEndTime(),  mockAppointmentData["endTime"])
        self.assertEqual(result.getAppointmentDate(),  "")
        self.assertEqual(result.getVisitReason(), "")
    
    
    @patch('requests.get')
    def test_getAppointmentWeek_success(self, mockGet):
        # Creating Mock Response Failure
        mockAppointmentListData = [{
            "appointmentDate": "Tue, 24 Oct 2023 00:00:00 GMT",
            "appointmentID": "A002",
            "appointmentStatus": "Approved",
            "clinicID": "0",
            "doctorID": "D000",
            "patientID": "P00004",
            "startTime": "8:00:00",
            "visitReasons": "Testing 2"
        },
        {
            "appointmentDate": "Tue, 24 Oct 2023 00:00:00 GMT",
            "appointmentID": "A003",
            "appointmentStatus": "Cancelled",
            "clinicID": "0",
            "doctorID": "",
            "patientID": "P00004",
            "startTime": "8:00:00",
            "visitReasons": "dad"
        },
        {
            "appointmentDate": "Tue, 24 Oct 2023 00:00:00 GMT",
            "appointmentID": "A004",
            "appointmentStatus": "Cancelled",
            "clinicID": "0",
            "doctorID": "",
            "patientID": "P00004",
            "startTime": "8:00:00",
            "visitReasons": "testing testing"
        },
        {
            "appointmentDate": "Tue, 24 Oct 2023 00:00:00 GMT",
            "appointmentID": "A005",
            "appointmentStatus": "Cancelled",
            "clinicID": "0",
            "doctorID": "",
            "patientID": "P00004",
            "startTime": "12:00:00",
            "visitReasons": "submit button testing, "
        }]
        
        mockResponse = Mock()
        mockResponse.json.return_value = mockAppointmentListData
        mockGet.return_value = mockResponse

        resultList = AppointmentRepo.AppointmentRepository.getAppointmentsWeekly("D003")

        #Test Length 
        self.assertEqual(len(resultList),len(mockAppointmentListData))


        for i in range(len(resultList)):
            self.assertEqual(resultList[i].getAppointmentID(), mockAppointmentListData[i]["appointmentID"])
            self.assertEqual(resultList[i].getDoctorID(),  mockAppointmentListData[i]["doctorID"])
            self.assertEqual(resultList[i].getClinicID(),  mockAppointmentListData[i]["clinicID"])
            self.assertEqual(resultList[i].getPatientID(),  mockAppointmentListData[i]["patientID"])
            self.assertEqual(resultList[i].getAppointmentStatus(),  mockAppointmentListData[i]["appointmentStatus"])
            self.assertEqual(resultList[i].getStartTime(),  mockAppointmentListData[i]["startTime"])
            #self.assertEqual(resultList[i].getEndTime(),  mockAppointmentListData[i]["endTime"])
            #Not tested as it is processed
            #self.assertEqual(resultList[i].getAppointmentDate(),  mockAppointmentListData[i]["appointmentDate"])
            self.assertEqual(resultList[i].getVisitReason(),  mockAppointmentListData[i]["visitReasons"])

    @patch('requests.get')
    def test_getAppointmentWeek_failure(self, mockGet):
        # Creating Mock Response Failure
        mockAppointmentListData = []
        
        mockResponse = Mock()
        mockResponse.json.return_value = mockAppointmentListData
        mockGet.return_value = mockResponse

        resultList = AppointmentRepo.AppointmentRepository.getAppointmentsWeekly("D003")

        #Test Length 
        self.assertEqual(len(resultList),0)


        for i in range(len(resultList)):
            self.assertEqual(resultList[i].getAppointmentID(), "")
            self.assertEqual(resultList[i].getDoctorID(),  "")
            self.assertEqual(resultList[i].getClinicID(),  "")
            self.assertEqual(resultList[i].getPatientID(),  "")
            self.assertEqual(resultList[i].getAppointmentStatus(),  "")
            self.assertEqual(resultList[i].getStartTime(),  "")
            #self.assertEqual(resultList[i].getEndTime(),  mockAppointmentListData[i]["endTime"])
            #Not tested as it is processed
            #self.assertEqual(resultList[i].getAppointmentDate(),  mockAppointmentListData[i]["appointmentDate"])
            self.assertEqual(resultList[i].getVisitReason(),  "")
    
    


if __name__=="__main__":
    unittest.main()