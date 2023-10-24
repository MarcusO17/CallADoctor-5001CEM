import unittest
from unittest.mock import Mock, patch
from src.model import Clinic, ClinicRepo
import json

class TestClinic(unittest.TestCase):

    @patch('requests.get')
    def test_getClinicfromID_success(self, mockGet):
        # Create a mock response
        mockClinicData = {
            "clinicID": 134,
            "clinicName": "Test Clinic",
            "clinicContact": "Contact Info",
            "address": "10-29B Main St",
            "governmentApproved": True,
        }
        mockResponse = Mock()
        mockResponse.json.return_value = [mockClinicData]
        mockGet.return_value = mockResponse


        # Call the function with a clinic ID
        result = Clinic.getClinicfromID(134)

        # Assert that the function returned the expected Clinic object
        self.assertEqual(result.getClinicID(), mockClinicData["clinicID"])
        self.assertEqual(result.getClinicName(),  mockClinicData["clinicName"])
        self.assertEqual(result.getClinicContact(),  mockClinicData["clinicContact"])
        self.assertEqual(result.getClinicAddress(),  mockClinicData["address"])
        self.assertEqual(result.getClinicStatus(),  mockClinicData["governmentApproved"])


    @patch('requests.get')
    def test_getClinicfromID_failed(self, mockGet):
        # Creating Mock Response Failure
        mockClinicData = {}
        mockResponse = Mock()
        mockResponse.json.return_value = [mockClinicData]
        mockGet.return_value = mockResponse

        # Call the function with a clinic ID
        result = Clinic.getClinicfromID(134)

        # Assert that the function returned the expected Clinic object
        self.assertEqual(result.getClinicID(),"")
        self.assertEqual(result.getClinicName(),  "")
        self.assertEqual(result.getClinicContact(),  "")
        self.assertEqual(result.getClinicAddress(),  "")
        self.assertEqual(result.getClinicStatus(),  "")
