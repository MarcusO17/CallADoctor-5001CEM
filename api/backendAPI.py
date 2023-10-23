from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests
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
    if conn == None:
        return None
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM users')
        users = [
            dict(
            ID = row['ID'],
            email = row['email'],
            password = row['password'],
            role = row['role'],
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
                patientICNumber = row['patientICNumber'],
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
        patientICNumber = contentJSON['patientICNumber']
        address = contentJSON['address']
        dateOfBirth = contentJSON['dateOfBirth'] # YYYY-MM-DD
        bloodType = contentJSON['bloodType']
        race = contentJSON['race']
   
        insertQuery = """
                        INSERT INTO patients (patientID,patientName,address,patientEmail,patientPassword,
                                            patientICNumber,dateOfBirth,bloodType,race)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(patientID,patientName,address,patientEmail,patientPassword,
                                             patientICNumber,dateOfBirth,bloodType,race))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    
    if request.method == 'DELETE':
        try:
            pass
            #cursor.execute("DELETE FROM patients")
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
                patientICNumber = row['patientICNumber'],
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
                clinicContact = row['clinicContact'],
                address = row['address'],
                governmentApproved = row['governmentApproved'],
            )
            for row in cursor.fetchall()
        ]
        if clinics is not None:
            return jsonify(clinics),200
        
        

    if request.method == 'POST':
        contentJSON = request.get_json()

        clinicID = contentJSON['clinicID']
        clinicName = contentJSON['clinicName']
        clinicEmail = contentJSON['clinicEmail']
        clinicPassword = contentJSON['clinicPassword']
        clinicContact = contentJSON['clinicContact']
        address = contentJSON['address']
        governmentApproved = contentJSON['governmentApproved']
   
        insertQuery = """
                        INSERT INTO clinics (clinicID,clinicName,address,clinicEmail,clinicPassword,
                                            clinicContact,governmentApproved)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(clinicID,clinicName,address,clinicEmail,clinicPassword,
                                            clinicContact,governmentApproved))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    
    if request.method == 'DELETE':
        #cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        #cursor.execute("DROP TABLE clinics")
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
                clinicContact = row['clinicContact'],
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
                doctorType = row['doctorType'],
                doctorICNumber = row['doctorICNumber'],
                doctorContact = row['doctorContact'],
                yearOfExperience = row['yearOfExperience'],
                status = row['status'],
                clinicID = row['clinicID']
            )
            for row in cursor.fetchall()
        ]
        if doctors is not None:
            return jsonify(doctors),200
        
        

    if request.method == 'POST':
        contentJSON = request.get_json()

        doctorID = requests.get('http://127.0.0.1:5000/doctors/idgen').text
        doctorName = contentJSON['doctorName'],
        doctorPassword = contentJSON['doctorPassword']
        doctorICNumber = contentJSON['doctorICNumber']
        doctorContact = contentJSON['doctorContact']
        doctorType = contentJSON['doctorType']
        yearOfExperience = contentJSON['yearOfExperience']
        doctorEmail = contentJSON['doctorEmail']
        status = contentJSON['status'],
        clinicID = contentJSON['clinicID']

        insertQuery = """
                        INSERT INTO doctors (doctorID,doctorName,doctorEmail,doctorPassword,doctorType,
                                            doctorICNumber,doctorContact,yearOfExperience,status,clinicID)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
        try:
            cursor = cursor.execute(insertQuery,(doctorID,doctorName,doctorEmail,doctorPassword,doctorType,
                                            doctorICNumber,doctorContact,yearOfExperience,status,clinicID))
        except Exception as e:
            return {'error': e}
        conn.commit() #Commit Changes to db, like git commit

        return'Successful POST', 201
    


    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM doctors")
            return 'Successful DELETE', 200
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
    cursor.close()
    conn.close()

@app.route('/doctors/<string:clinicID>', methods=['GET'])
def doctorsClinic(clinicID):
    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        #Add Error Handling
        cursor.execute("SELECT * FROM doctors where clinicID = %s",clinicID)

        doctors = [
            dict(
                doctorID = row['doctorID'],
                doctorName = row['doctorName'],
                doctorType = row['doctorType'],
                doctorICNumber = row['doctorICNumber'],
                doctorContact = row['doctorContact'],
                yearOfExperience = row['yearOfExperience'],
                status = row['status'],
                clinicID = row['clinicID']
            )
            for row in cursor.fetchall()
        ]
        if doctors is not None:
            return jsonify(doctors),200

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
                doctorType = row['doctorType'],
                doctorICNumber = row['doctorICNumber'],
                doctorContact = row['doctorContact'],
                yearOfExperience = row['yearOfExperience'],
                status = row['status'],
                clinicID = row['clinicID']
            )
            for row in cursor.fetchall()
        ]
        if doctor is not None:
            return jsonify(doctor),200
    if request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM doctors WHERE doctorID = %s;",id)
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
        cursor.execute("SELECT * FROM appointments ORDER BY appointmentDate, startTime")

        appointments = [
            dict(
                appointmentID = row['appointmentID'],
                doctorID  = row['doctorID'],
                patientID = row['patientID'],
                appointmentStatus = row['appointmentStatus'],
                startTime = str(row['startTime']),
                appointmentDate = row['appointmentDate'],
                visitReasons= row['visitReasons'],
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
        appointmentDate = contentJSON['appointmentDate']
        visitReasons= contentJSON['visitReasons']

        insertQuery = """
                        INSERT INTO appointments (appointmentID,doctorID,patientID,appointmentStatus,startTime,
                                            appointmentDate,visitReasons)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """
        cursor = cursor.execute(insertQuery,(appointmentID,doctorID,patientID,appointmentStatus,startTime,
                                            appointmentDate,visitReasons))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201

    if request.method == 'DELETE':  
        try:
            cursor.execute("DELETE FROM appointments")
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
                patientID = row['patientID'],
                appointmentStatus = row['appointmentStatus'],
                startTime = str(row['startTime']),
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


@app.route('/appointments/<string:aid>/assign/<string:did>',methods=['PATCH'])
def appointmentDoctorAssign(aid,did):

    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'PATCH':
        try:
            cursor.execute("UPDATE appointments SET doctorID = %s where appointmentID = %s",(did,aid))
        except pymysql.MySQLError as e:
            return 'Error : ',e
    
        conn.commit()
        
        return 'Successful PATCH', 200  

    
@app.route('/appointments/week',methods=['GET'])
def appointmentsWeek():
    dateToday = datetime.now().date() - timedelta(days= datetime.now().date().weekday())
    dateEnd = dateToday + timedelta(days=4)
    #print(dateToday)
    #print(dateEnd)
    conn = dbConnect()  
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM appointments where appointmentDate BETWEEN %s AND %s ORDER BY appointmentDate, startTime"
                        ,(dateToday,dateEnd))
        appointment = [
            dict(
                appointmentID = row['appointmentID'],
                doctorID  = row['doctorID'],
                patientID = row['patientID'],
                appointmentStatus = row['appointmentStatus'],
                startTime = str(row['startTime']),
                appointmentDate = row['appointmentDate'],
                visitReasons= row['visitReasons']
            )
            for row in cursor.fetchall()
        ]
        if appointment is not None:
            return jsonify(appointment),200

@app.route('/appointments/week/<string:doctorID>',methods=['GET'])
def appointmentsWeekID(doctorID):
    dateToday = datetime.now().date() - timedelta(days= datetime.now().date().weekday())
    dateEnd = dateToday + timedelta(days=4)
    conn = dbConnect()  
    cursor = conn.cursor()


    if request.method == 'GET':
        cursor.execute("""SELECT * FROM appointments where doctorID = %s AND
                       appointmentDate BETWEEN %s AND %s """,(doctorID,dateToday,dateEnd))
        appointment = [
            dict(
                appointmentID = row['appointmentID'],
                doctorID  = row['doctorID'],
                patientID = row['patientID'],
                appointmentStatus = row['appointmentStatus'],
                startTime = str(row['startTime']),
                appointmentDate = row['appointmentDate'],
                visitReasons= row['visitReasons']
            )
            for row in cursor.fetchall()
        ]
        if appointment is not None:
            return jsonify(appointment),200
    
@app.route('/appointments/<string:id>/find',methods=['GET'])
def appointmentsFind(id):
    conn = dbConnect()  
    cursor = conn.cursor()

    response = requests.get(f"http://127.0.0.1:5000/appointments/{id}")
    appointment = response.json()[0]
    date = datetime.strptime(appointment['appointmentDate'],'%a, %d %b %Y %H:%M:%S %Z')

    if request.method == 'GET':
        cursor.execute("""SELECT doctorID
                          FROM doctors
                          WHERE doctorID NOT IN (
                            SELECT doctorID
                            FROM appointments
                            WHERE appointmentDate = %s AND startTime = %s
                          );
                        """,(date,appointment['startTime']))
        appointment = [
            dict(
                doctorID  = row['doctorID']
            )
            for row in cursor.fetchall()
        ]
        if appointment is not None:
            return jsonify(appointment),200    

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
    
@app.route('/prescriptionDetails/<string:id>',methods=['GET','DELETE'])
def prescriptionDetailsID(id):

    conn = dbConnect()  
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM prescriptionsDetails where prescriptionID = %s",id)
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
            cursor.execute("DELETE FROM prescriptionsDetails WHERE prescriptionID = %s",id)
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

@app.route('/doctors/idgen')
def getLastDoctorID():
    conn = dbConnect()  
    cursor = conn.cursor()
    
    #Add Error Handling
    cursor.execute("SELECT COUNT(*) FROM doctors")
    counter = cursor.fetchall()
    id = str(counter[0]['COUNT(*)'])
    id = f'D{id.zfill(3)}'
    
    cursor.close()
    conn.close()

    if id is not None:
            return id,200


@app.route('/patients/idgen')
def getLastPatientID():
    conn = dbConnect()  
    cursor = conn.cursor()
    
    #Add Error Handling
    cursor.execute("SELECT COUNT(*) FROM patients")
    counter = cursor.fetchall()
    id = str(counter[0]['COUNT(*)'])
    id = f'P{id.zfill(3)}'
    
    cursor.close()
    conn.close()

    if id is not None:
            return id,200
    

@app.route('/clinics/idgen')
def getLastClinicID():
    conn = dbConnect()  
    cursor = conn.cursor()
    
    #Add Error Handling
    cursor.execute("SELECT COUNT(*) FROM clinics")
    counter = cursor.fetchall()
    id = str(counter[0]['COUNT(*)'])
    id = f'C{id.zfill(3)}'
    
    cursor.close()
    conn.close()

    if id is not None:
            return id,200
   
@app.route('/appointments/idgen')
def getLastAppointmentsID():
    conn = dbConnect()  
    cursor = conn.cursor()
    
    #Add Error Handling
    cursor.execute("SELECT COUNT(*) FROM appointments")
    counter = cursor.fetchall()
    id = str(counter[0]['COUNT(*)'])
    id = f'A{id.zfill(3)}'
    
    cursor.close()
    conn.close()

    if id is not None:
            return id,200
   


if __name__ == "__main__":
    app.run(debug=True)