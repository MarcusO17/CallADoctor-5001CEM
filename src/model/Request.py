import requests

class Request:
    def __init__(self,requestID, requestType, clientID, approvalStatus, dateSubmitted, requestReason, appointmentID):
        self.requestID = requestID
        self.requestType = requestType
        self.clientID = clientID
        self.approvalStatus = approvalStatus
        self.dateSubmitted = dateSubmitted
        self.requestReason = requestReason
        self.appointmentID = appointmentID

    def getRequestID(self):
        return self.requestID

    def setRequestID(self, requestID):
        self.requestID = requestID

    def getRequestType(self):
        return self.requestType

    def setRequestType(self, requestType):
        self.requestType = requestType

    def getClientID(self):
        return self.clientID

    def setClientID(self, clientID):
        self.clientID = clientID

    def getApprovalStatus(self):
        return self.approvalStatus

    def setApprovalStatus(self, approvalStatus):
        self.approvalStatus = approvalStatus

    def getDateSubmitted(self):
        return self.dateSubmitted

    def setDateSubmitted(self, dateSubmitted):
        self.dateSubmitted = dateSubmitted

    def getRequestReason(self):
        return self.requestReason

    def setRequestReason(self, requestReason):
        self.requestReason = requestReason

    def getAppointmentID(self):
        return self.appointmentID

    def setAppointmentID(self, appointmentID):
        self.appointmentID = appointmentID
    
    def getRequests(clinicID):
        requestList  =[]
        try:
            response = requests.get(f'http://127.0.0.1:5000/requests/{clinicID}')
            recordsList = response.json()
        
        except requests.RequestException as e:
            print(f'Error : {e}')
            return []

        if response.status_code == 500:
            print(recordsList)
            return requestList

        for records in recordsList:
            tempRequest= Request("","","","","","","")
            
            tempRequest.setRequestID(records['requestsID'])
            tempRequest.setRequestType(records['requestsType'])
            tempRequest.setClientID(records['clientID'])
            tempRequest.setApprovalStatus(records['approvalStatus'])
            tempRequest.setRequestReason(records['requestReason'])
            tempRequest.setDateSubmitted(records['dateSubmitted'])
            tempRequest.setAppointmentID(records['appointmentID'])
            
            requestList.append(tempRequest)
            
        return requestList
        

    def cancelRequest(self):
        response = requests.patch(f'http://127.0.0.1:5000/requests/cancel/{self.getRequestID()}')
        denyStatus = response.text

        if response.status_code == 200:
            return denyStatus , True
        else:
            return denyStatus , False
        

           
    def approveRequest(self):
        response = requests.patch(f'http://127.0.0.1:5000/requests/approve/{self.getRequestID()}')
        requests.patch(f'http://127.0.0.1:5000/appointments/{self.getAppointmentID()}/deny')
        completeStatus = response.text

        if response.status_code == 200:
            return completeStatus , True
        else:
            return completeStatus , False
        

    def existingAppointments(appointmentID):
        response = requests.get(f'http://127.0.0.1:5000/requests/exists/{appointmentID}')
        completeStatus = response.text

        if response.status_code == 200:
            print(True)
            return True
        else:
            print(False)
            return False