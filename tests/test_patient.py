import unittest
import requests
from unittest.mock import Mock, patch
from src.model import Clinic, ClinicRepo


class TestPatient(unittest.TestCase):
    """Class to test Patient and Patient Repo Models.
    """