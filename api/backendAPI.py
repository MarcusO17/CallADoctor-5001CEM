from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymysql


app = Flask(__name__)


def configure():
    load_dotenv()

def dbConnect():    
    conn = None 
    try:
        conn = pymysql.connect(
        host=os.getenv('SQL_hostname'),
        database=os.getenv('SQL_database_name'),
        user=os.getenv('SQL_username'),
        passwd=os.getenv('PWD'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
         print(e)
    return conn

@app.route('/')
def index():
    return 'Welcome to Call a Doctor!'

@app.route('/users',methods=['GET'])
def users():
    conn = dbConnect()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM users')
        users = [
            dict(
            ID = row['ID'],
            email = row['email'],
            password = row['password'],
            role = row['role']
            )
            for row in cursor.fetchall()
        ]
    if users is not None:
        return jsonify(users), 200    
          
@app.route('/patients',methods=['GET','POST','DELETE'])
def patients():
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        #Add Error Handling
        cursor.execute("SELECT * FROM patients")
    
        patients = [
            dict(
                patientID = row['patientID'],
                patientName = row['patientName'],
                address = row['address'],
                dateOfBirth = row['dateOfBirth'],
                bloodType = row['bloodType'],
                race = row['race'],  
            )
            for row in cursor.fetchall()
        ]
        if patients is not None:
            return jsonify(patients),200
        
        

    if request.method == 'POST':
        contentJSON = request.get_json()

        patientID = contentJSON['patientID']
        patientName = contentJSON['patientName']
        patientEmail = contentJSON['patientEmail']
        patientPassword = contentJSON['patientPassword']
        address = contentJSON['address']
        dateOfBirth = contentJSON['dateOfBirth'] # YYYY-MM-DD
        bloodType = contentJSON['bloodType']
        race = contentJSON['race']
   
        insertQuery = """
                        INSERT INTO patients (patientID,patientName,address,patientEmail,patientPassword,
                                            dateOfBirth,bloodType,race)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(patientID,patientName,address,patientEmail,patientPassword,
                                             dateOfBirth,bloodType,race))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    
    if request.method == 'DELETE':
        try:
            cursor.execute("DROP TABLE patients")
        except pymysql.MySQLError as e:
            return 'Error : ',e
        return 'Successful DELETE', 200
    
@app.route('/patients/<string:id>',methods=['GET','DELETE'])
def patientID(id):
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM patients where patientID = %s",id)
        patient = [
            dict(
                patientID = row['patientID'],
                patientName = row['patientName'],
                address = row['address'],
                dateOfBirth = row['dateOfBirth'],
                bloodType = row['bloodType'],
                race = row['race'],  
            )
            for row in cursor.fetchall()
        ]
        if patients is not None:
            return jsonify(patient),200
    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM patients WHERE patientID = %s",id)
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
        conn.commit()
        return 'Successful DELETE', 200
    
@app.route('/clinics',methods=['GET','POST','DELETE'])  
def clinics():
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        #Add Error Handling
        cursor.execute("SELECT * FROM clinics")
    
        clinics = [
            dict(
                clinicID = row['clinicID'],
                clinicName = row['clinicName'],
                address = row['address'],
                governmentApproved = row['governmentApproved'],
            )
            for row in cursor.fetchall()
        ]
        if clinics is not None:
            return jsonify(clinics),200
        
        

    if request.method == 'POST':
        contentJSON = request.get_json()

        clinicName = contentJSON['clinicName']
        clinicEmail = contentJSON['clinicEmail']
        clinicPassword = contentJSON['clinicPassword']
        address = contentJSON['address']
        governmentApproved = contentJSON['governmentApproved']
   
        insertQuery = """
                        INSERT INTO clinics (clinicName,address,clinicEmail,clinicPassword,
                                            governmentApproved)
                        VALUES (%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(clinicName,address,clinicEmail,clinicPassword,
                                            governmentApproved))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    
    if request.method == 'DELETE':
        #cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute("DROP TABLE clinics")
        #cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        
        return 'Successful DELETE', 200

@app.route('/clinics/<string:id>',methods=['GET','DELETE'])
def clinicID(id):
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM clinics where clinicID = %s",id)
        clinic = [
            dict(
                clinicID = row['clinicID'],
                clinicName = row['clinicName'],
                address = row['address'],
                governmentApproved = row['governmentApproved'],
            )
            for row in cursor.fetchall()
        ]
        if clinics is not None:
            return jsonify(clinic),200
    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM clinics WHERE clinicID = %s",id)
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
        conn.commit()
        return 'Successful DELETE', 200
      
@app.route('/doctors', methods=['GET','POST','DELETE'])
def doctors():
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        #Add Error Handling
        cursor.execute("SELECT * FROM doctors")

        doctors = [
            dict(
                doctorID = row['doctorID'],
                doctorName = row['doctorName'],
                status = row['status'],
                clinicID = row['clinicID']
            )
            for row in cursor.fetchall()
        ]
        if doctors is not None:
            return jsonify(doctors),200
        
        

    if request.method == 'POST':
        contentJSON = request.get_json()

        doctorID = contentJSON['doctorID'],
        doctorName = contentJSON['doctorName'],
        doctorPassword = contentJSON['doctorPassword']
        doctorEmail = contentJSON['doctorEmail']
        status = contentJSON['status'],
        clinicID = contentJSON['clinicID']

        insertQuery = """
                        INSERT INTO doctors (doctorID,doctorName,doctorEmail,doctorPassword,
                                            status,clinicID)
                        VALUES (%s,%s,%s,%s,%s,%s)
                        """
        cursor = cursor.execute(insertQuery,(doctorID,doctorName,status,doctorEmail,doctorPassword,
                                                clinicID))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    


    if request.method == 'DELETE':
        try:
            cursor.execute("DROP TABLE doctors")
        except pymysql.MySQLError as e:
            return 'Error : ',e
        return 'Successful DELETE', 200

@app.route('/doctors/<string:id>',methods=['GET','DELETE'])
def doctorID(id):
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM doctors where doctorID = %s",id)
        doctor = [
            dict(
                doctorID = row['doctorID'],
                doctorName = row['doctorName'],
                status = row['status'],
                clinicID = row['clinicID']
            )
            for row in cursor.fetchall()
        ]
        if doctor is not None:
            return jsonify(doctor),200
    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM doctors WHERE doctorID = %s",id)
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
        conn.commit()
        return 'Successful DELETE', 200  

@app.route('/appointments', methods=['GET','POST','DELETE'])
def appointments():

    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        #Add Error Handling
        cursor.execute("SELECT * FROM appointments")

        appointments = [
            dict(
                appointmentID = row['appointmentID'],
                doctorID  = row['doctorID'],
                patientID = row['patientID '],
                appointmentStatus = row['appointmentStatus'],
                startTime = row['startTime '],
                endTime = row['endTime'],
                appointmentDate = row['appointmentDate'],
                visitReasons= row['visitReasons']
            )
            for row in cursor.fetchall()
        ]
        if appointments is not None:
            return jsonify(appointments),200
        
    if request.method == 'POST':

        contentJSON = request.get_json()

        appointmentID = contentJSON['appointmentID']
        doctorID  = contentJSON['doctorID']
        patientID = contentJSON['patientID']
        appointmentStatus = contentJSON['appointmentStatus']
        startTime = contentJSON['startTime']
        endTime = contentJSON['endTime']
        appointmentDate = contentJSON['appointmentDate']
        visitReasons= contentJSON['visitReasons']

        insertQuery = """
                        INSERT INTO doctors (appointmentID,doctorID,patientID,appointmentStatus,startTime,
                                            endTime,appointmentDate,visitReasons)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        cursor = cursor.execute(insertQuery,(appointmentID,doctorID,patientID,appointmentStatus,startTime,
                                            endTime,appointmentDate,visitReasons))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201

    if request.method == 'DELETE':
        try:
            cursor.execute("DROP TABLE appointments")
        except pymysql.MySQLError as e:
            return 'Error : ',e
        return 'Successful DELETE', 200

@app.route('/appointments/<string:id>',methods=['GET','DELETE'])
def appointmentID(id):

    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM appointments where appointmentID = %s",id)
        appointment = [
            dict(
                appointmentID = row['appointmentID'],
                doctorID  = row['doctorID'],
                patientID = row['patientID '],
                appointmentStatus = row['appointmentStatus'],
                startTime = row['startTime '],
                endTime = row['endTime'],
                appointmentDate = row['appointmentDate'],
                visitReasons= row['visitReasons']
            )
            for row in cursor.fetchall()
        ]
        if appointment is not None:
            return jsonify(appointment),200
    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM appointments WHERE appointmentID = %s",id)
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
        conn.commit()
        return 'Successful DELETE', 200  
    
@app.route('/prescriptions', methods=['GET','POST','DELETE'])
def prescriptions():

    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        #Add Error Handling
        cursor.execute("SELECT * FROM prescriptions")

        appointments = [
            dict(
                prescriptionID = row['prescriptionID'],
                appointmentID  = row['appointmentID'],
                expiryDate = row['expiryDate']
            )
            for row in cursor.fetchall()
        ]
        if appointments is not None:
            return jsonify(appointments),200
        
    if request.method == 'POST':

        contentJSON = request.get_json()

        prescriptionID = contentJSON['prescriptionID'],
        appointmentID  = contentJSON['appointmentID'],
        expiryDate = contentJSON['expiryDate']

        insertQuery = """
                        INSERT INTO doctors (prescriptionID,appointmentID,expiryDate
                                            )
                        VALUES (%s,%s,%s)
                    """
        cursor = cursor.execute(insertQuery,(prescriptionID,appointmentID,expiryDate
                                            ))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201

    if request.method == 'DELETE':
        try:
            cursor.execute("DROP TABLE prescriptions")
        except pymysql.MySQLError as e:
            return 'Error : ',e
        return 'Successful DELETE', 200

@app.route('/prescriptions/<string:id>',methods=['GET','DELETE'])
def prescriptionID(id):

    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM prescriptions where prescriptionID = %s",id)
        prescription = [
            dict(
                prescriptionID = row['prescriptionID'],
                appointmentID  = row['appointmentID'],
                expiryDate = row['expiryDate']
            )
            for row in cursor.fetchall()
        ]
        if prescription is not None:
            return jsonify(prescription),200
    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM prescriptions WHERE prescriptionID = %s",id)
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
        conn.commit()
        return 'Successful DELETE', 200

@app.route('/users/auth')
def userAuthentication():
    conn = dbConnect()  
    cursor = conn.cursor()
    
    contentJSON = request.get_json()

    email = contentJSON['email']
    password = contentJSON['password']

    cursor.execute('SELECT ID,role from users where email = %s AND password = %s',(email,password))

    try:
        sessionInfo = cursor.fetchone()
    except:
        sessionInfo = None;

    cursor.close()
    conn.close()

    if sessionInfo != None:
        return jsonify(sessionInfo), 200
    else:
        return {'ID': 'DENIED', 'role':'DENIED'}, 401

   
  


if __name__ == "__main__":
    app.run()