import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

def test_index():
    try:
        #Requesting index
        response = requests.get(BASE_URL + "/") 
        #Test if index is OK
        assert response.status_code == 200

    except requests.exceptions.ConnectionError as e:
        assert False, f"Connection Closed : {e}"

def test_get_users():
    try:
        #Requesting index
        response = requests.get(BASE_URL + "/users") 
        #Test if index is OK
        assert response.status_code == 200

    except requests.exceptions.RequestException as e:
        assert False, f"Failure : {e}"

