import requests
import unittest
from unittest.mock import Mock, patch


def getPatients():
    response = requests.get('http://127.0.0.1:5000/patients')
    return response.json

class testAPI(unittest.TestCase):
    URL = 'http://127.0.0.1:5000'

    def test_index(self):
        response  = requests.get(f'{self.URL}/')
        assert response.status_code == 200


    @patch('requests.get')
    def test_get_patient(self,mockGet):
        mockResponse = Mock()

        mockResult = {
                "patientID": "12345",
                "patientName": "John Doe",
                "address": "123 Main St, City, Country",
                "dateOfBirth": "1990-05-15",
                "bloodType": "A+",
                "race": "Caucasian"
            }
        
        mockResponse.json.return_value = mockResult 
        mockGet.return_value = mockResponse

        result = getPatients()
        mockGet.assert_called_with(f'{self.URL}/patients')
       
        self.assertEqual(result, mockResult)

if __name__ == '__main__':
    unittest.main()