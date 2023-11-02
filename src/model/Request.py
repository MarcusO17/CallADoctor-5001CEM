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
