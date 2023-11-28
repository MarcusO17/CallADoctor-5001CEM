import unittest
import requests
from unittest.mock import Mock, patch
from src.model import Doctor, DoctorRepo, Patient


class TestDoctor(unittest.TestCase):

    @patch('requests.get')
    def test_getDoctorFromID_success(self, mock_get):
        doctorID = "D123"
        mockDoctorData = {
            "doctorID": doctorID,
            "doctorName": "Dr. John Doe",
            "clinicID": "C456",
            "status": "Active",
            "doctorType": "General",
            "doctorContact": "123-456-7890",
            "doctorICNumber": "123456-7890",
            "yearOfExperience": 5
        }

        mockResponse = Mock()
        mockResponse.json.return_value = [mockDoctorData]
        mock_get.return_value = mockResponse

        result = Doctor.getDoctorfromID(doctorID)

        self.assertIsInstance(result, Doctor)
        self.assertEqual(result.getDoctorID(),mockDoctorData['doctorID'])
        self.assertEqual(result.getDoctorName(),mockDoctorData['doctorName'])
        self.assertEqual(result.getClinicID(),mockDoctorData['clinicID'])
        self.assertEqual(result.getStatus(),mockDoctorData['status'])
        self.assertEqual(result.getDoctorType(),mockDoctorData['doctorType'])
        self.assertEqual(result.getDoctorContact(),mockDoctorData['doctorContact'])
        self.assertEqual(result.getDoctorICNumber(),mockDoctorData['doctorICNumber'])
        self.assertEqual(result.getYearsOfExperience(),mockDoctorData['yearOfExperience'])

    @patch('requests.get')
    def test_getDoctorFromID_failure(self, mock_get):
        doctorID = "D100"

        mock_get.side_effect = Exception("Mock Error")
        result = Doctor.getDoctorfromID(doctorID)

        self.assertIsInstance(result, Doctor)
        self.assertEqual(result.getDoctorID(),"")
        self.assertEqual(result.getDoctorName(),"")
        self.assertEqual(result.getClinicID(),"")
        self.assertEqual(result.getStatus(),"")
        self.assertEqual(result.getDoctorType(),"")
        self.assertEqual(result.getDoctorContact(),"")
        self.assertEqual(result.getDoctorICNumber(),"")
        self.assertEqual(result.getYearsOfExperience(),"")

    @patch('requests.get')
    def test_getDoctorPastPatients_success(self, mock_get):
        doctorID = "D123"

        mockPatientData = [
            {"patientID": "P1", 
             "patientName": "John Doe", 
             "address": "123 Main St",
             "dateOfBirth": "1990-01-01",
             "bloodType": "A", 
             "race": "Caucasian", 
             "lat": 40.7128, 
             "lon": -74.0060},
        ]

      
        mockResponse = Mock()
        mockResponse.json.return_value = mockPatientData
        mock_get.return_value = mockResponse

      
        result = Doctor.getDoctorPastPatients(doctorID)


        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(mockPatientData))

        for patient, mockPatientData in zip(result, mockPatientData):
            self.assertIsInstance(patient, Patient)
            self.assertEqual(patient.getPatientID(), mockPatientData['patientID'])
            self.assertEqual(patient.getPatientName(), mockPatientData['patientName'])
            self.assertEqual(patient.getPatientAddress(), mockPatientData['address'])
            self.assertEqual(patient.getPatientDOB(), mockPatientData['dateOfBirth'])
            self.assertEqual(patient.getPatientBlood(), mockPatientData['bloodType'])
            self.assertEqual(patient.getPatientRace(), mockPatientData['race'])
            self.assertEqual(patient.getPatientLat(), mockPatientData['lat'])
            self.assertEqual(patient.getPatientLon(), mockPatientData['lon'])


    @patch('requests.get')
    def test_getDoctorPastPatients_failure(self, mock_get):
        doctorID = "D123"

        mock_get.side_effect = requests.RequestException("Mock Error")

        result = Doctor.getDoctorPastPatients(doctorID)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0) 

    @patch('requests.get')
    def test_getCertification_success(self, mock_get):
        doctorID = "D123"

        mockContent = b'MockImageContent'

        mockResponse = Mock()
        mockResponse.status_code = 200
        mockResponse.content = mockContent
        mock_get.return_value = mockResponse

        doctorObj = Doctor(
                            doctorID="D123",
                            doctorName="Dr. John Doe",
                            clinicID="C456",
                            status="Active",
                            doctorType="General",
                            doctorContact="123-456-7890",
                            doctorICNumber="123456-7890",
                            yearsOfExperience=5
                        )

        result = doctorObj.getCertification()
       
        self.assertIsNotNone(result) 
        self.assertEqual(result, mockContent)  
    

    @patch('requests.get')
    def test_getCertification_failure(self, mock_get):
        doctorID = "D123"

        mock_response = Mock()
        mock_response.status_code = 404  
        mock_get.return_value = mock_response 

        doctorObj = Doctor(
                            doctorID="D123",
                            doctorName="Dr. John Doe",
                            clinicID="C456",
                            status="Active",
                            doctorType="General",
                            doctorContact="123-456-7890",
                            doctorICNumber="123456-7890",
                            yearsOfExperience=5
                        )

        result = doctorObj.getCertification()

        self.assertIsNone(result)  
    
    @patch('requests.get')
    def test_getDoctorList_success(self, mock_get):
   
        mockDoctorData = [
            {"clinicID": "C001", 
             "doctorID": "D001", 
             "doctorName": "Dr. John Doe", 
             "status": "Active",
             "doctorType": "General", 
             "doctorContact": "123-456-7890", 
             "doctorICNumber": "123456-7890",
             "yearOfExperience": 5},
        
        ]

    
        mockResponse = Mock()
        mockResponse.json.return_value = mockDoctorData
        mock_get.return_value = mockResponse

      
        result = DoctorRepo.DoctorRepository.getDoctorList()

        
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(mockDoctorData))


        for doctor, mockDoctorData in zip(result, mockDoctorData):
            self.assertIsInstance(doctor, Doctor)
            self.assertEqual(doctor.getClinicID(), mockDoctorData['clinicID'])
            self.assertEqual(doctor.getDoctorID(), mockDoctorData['doctorID'])
            self.assertEqual(doctor.getDoctorName(), mockDoctorData['doctorName'])
            self.assertEqual(doctor.getStatus(), mockDoctorData['status'])
            self.assertEqual(doctor.getDoctorType(), mockDoctorData['doctorType'])
            self.assertEqual(doctor.getDoctorContact(), mockDoctorData['doctorContact'])
            self.assertEqual(doctor.getDoctorICNumber(), mockDoctorData['doctorICNumber'])
            self.assertEqual(doctor.getYearsOfExperience(), mockDoctorData['yearOfExperience'])


if __name__=="__main__":
    unittest.main()