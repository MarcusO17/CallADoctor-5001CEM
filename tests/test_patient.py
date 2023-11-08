import unittest
import requests
from unittest.mock import Mock, patch
from src.model import Patient


class TestPatient(unittest.TestCase):
    """Class to test Patient and Patient Repo Models.
    """

    @patch('requests.get')
    def test_getPatientfromID_success(self, mockGet):
        # Create a mock response
        mockPatientData = {
            "patientID": "P00992",
            "patientName": "James",
            "address": "12-B-A Malaysian Heights",
            "dateOfBirth": "1980-05-15",
            "bloodType": "A+",
            "race": "Asian",
            "lat" : "123.2",
            "lon" : "132"
            }

        mockResponse = Mock()
        mockResponse.json.return_value = [mockPatientData]
        mockGet.return_value = mockResponse


        # Call the function with a patient ID
        result = Patient.getPatientfromID("P00092")

        # Assert that the function returned the expected Patient object
        self.assertEqual(result.getPatientID(), mockPatientData["patientID"])
        self.assertEqual(result.getPatientName(),  mockPatientData["patientName"])
        self.assertEqual(result.getPatientAddress(),  mockPatientData["address"])
        self.assertEqual(result.getPatientDOB(),  mockPatientData["dateOfBirth"])
        self.assertEqual(result.getPatientBlood(),  mockPatientData["bloodType"])
        self.assertEqual(result.getPatientRace(),  mockPatientData["race"])

    @patch('requests.get')
    def test_getPatientfromID_failure(self, mockGet):
        # Create a mock response
        mockPatientData = {}

        mockResponse = Mock()
        mockResponse.json.return_value = [mockPatientData]
        mockGet.return_value = mockResponse


        # Call the function with a patient ID
        result = Patient.getPatientfromID("P19200")

        # Assert that the function returned the expected Patient object
        self.assertEqual(result.getPatientID(), "")
        self.assertEqual(result.getPatientName(), "")
        self.assertEqual(result.getPatientAddress(),  "")
        self.assertEqual(result.getPatientDOB(), "")
        self.assertEqual(result.getPatientBlood(),  "")
        self.assertEqual(result.getPatientRace(), "")
