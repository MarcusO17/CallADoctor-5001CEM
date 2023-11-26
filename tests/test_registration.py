import unittest
from unittest.mock import Mock, patch
from src.model.Registration import Registration


class TestRegistration(unittest.TestCase):
    @patch('requests.post')
    def test_registerDoctor_Success(self, mock_get):
        response_data = 'Successful POST : D001',201
        mock_get.return_value = Mock(status_code=201, text=response_data[0])

       
        expectedResult = 'Successful POST : D001',201

        jsonDetails = {
                        "doctorName": "Dr. John Doe",
                        "doctorPassword": "securePassword123",
                        "doctorICNumber": "1234567890",
                        "doctorContact": "123-456-7890",
                        "doctorType": "General Physician",
                        "yearOfExperience": 10,
                        "doctorEmail": "johndoe@example.com",
                        "status": "Active",
                        "clinicID": "C001"
                      }

        doctorImage = {'image': 'fakeImageData'}
        
        result,status = Registration.registerDoctor(jsonDetails, doctorImage)
        self.assertEqual(result[0][0], expectedResult[0][0])
        self.assertTrue(status)
      
    @patch('requests.post')
    def test_registerClinic_Success(self, mock_get):
        response_data = 'Successful POST : D001',201
        mock_get.return_value = Mock(status_code=201, text=response_data[0])
       
        expectedResult = 'Successful POST : D001',201

        jsonDetails = {
                        "clinicName": "John Doe Clinic",
                        "clinicPassword": "securePassword123",
                        "clinicContact": "123-456-7890",
                        "address": "30, Lintang Delima 4, Taman Island Glades, 11600 Jelutong, Pulau Pinang",
                        "clinicEmail": "johndoeClinic@example.com",
                      }
        
        clinicImage = {'image': 'fakeImageData'}

        result,status = Registration.registerClinic(jsonDetails,clinicImage)
        self.assertEqual(result[0][0], expectedResult[0][0])
        self.assertTrue(status)



    @patch('requests.post')
    def test_registerPatient_Success(self, mock_get):
        response_data = 'Successful POST : C001',201
        mock_get.return_value = Mock(status_code=201, text=response_data[0])

       
        expectedResult = 'Successful POST : P000',201

        jsonDetails = {
                        "patientName": "John Doe",
                        "patientPassword": "securePassword123",
                        "patientICNumber": "1234567890",
                        "patientContact": "123-456-7890",
                        "address": "30, Lintang Delima 4, Taman Island Glades, 11600 Jelutong, Pulau Pinang",
                        "dateOfBirth": 10,
                        "patientEmail": "johndoe@example.com",
                        "bloodType": "O+",
                        "race": "Indian"
                      }
        
        result,status = Registration.registerPatient(jsonDetails)
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

        doctorImage = {'image': 'fakeImageData'}

        result, status = Registration.registerDoctor(jsonDetails, doctorImage)
        self.assertEqual(result, expectedResult)
        self.assertFalse(status)

    @patch('requests.post')
    def test_registerPatient_Failure(self, mock_get):
        response_data = {'error':Exception}
        mock_get.return_value = Mock(status_code=400, text=response_data)
        expectedResult = {'error':Exception}

        jsonDetails = {
                        "patientName": "John Doe",
                        "patientPassword": "securePassword123",
                        "patientICNumber": "1234567890",
                        "patientContact": "123-456-7890",
                        "address": "30, Lintang Delima 4, Taman Island Glades, 11600 Jelutong, Pulau Pinang",
                        "dateOfBirth": 10,
                        "patientEmail": "johndoe@example.com",
                        "bloodType": "O+",
                        "race": "Indian"
                      }
        
        result,status = Registration.registerPatient(jsonDetails)
        self.assertEqual(result['error'], expectedResult['error'])
        self.assertFalse(status)
