import unittest
from unittest.mock import Mock, patch
from src.model.Registration import Registration


class TestRegistration(unittest.TestCase):
    @patch('requests.post')
    def test_registerDoctor_Success(self, mock_get):
        response_data = ('Successful POST', 201),True
        mock_get.return_value = Mock(status_code=201, text=response_data)

       
        expectedResult = ('Successful POST', 201),True

        jsonDetails = {
                        "doctorName": "Dr. John Doe",
                        "doctorPassword": "securePassword123",
                        "doctorICNumber": "1234567890",
                        "doctorContact": "123-456-7890",
                        "doctorType": "General Physician",
                        "yearOfExperience": 10,
                        "doctorEmail": "johndoe@example.com",
                        "status": "Active",
                        "clinicID": "CLINIC001"
                      }

        
        result,status = Registration.registerDoctor(jsonDetails)
        self.assertEqual(result[0][0], expectedResult[0][0])
        self.assertTrue(status)
    
    @patch('requests.post')
    def test_registerDoctor_Failure(self, mock_get):
        response_data = {'error':Exception}
        mock_get.return_value = Mock(status_code=400, text=response_data)

       
        expectedResult = {'error':Exception}

        jsonDetails = {
                        "doctorName": "Dr. John Doe",
                        "doctorPassword": "securePassword123",
                        "doctorICNumber": "1234567890",
                        "doctorContact": "123-456-7890",
                        "doctorType": "General Physician",
                        "yearOfExperience": 10,
                        "doctorEmail": "johndoe@example.com",
                        "status": "Active",
                        "clinicID": "CLINIC001"
                      }

        
        result, status = Registration.registerDoctor(jsonDetails)
        self.assertEqual(result, expectedResult)
        self.assertFalse(status)
