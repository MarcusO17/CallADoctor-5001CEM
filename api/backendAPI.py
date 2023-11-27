from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
from datetime import datetime, timedelta
from src.model import geoHelper
import bcrypt
import io
import os
import requests
import pymysql
import pandas as pd 


app = Flask(__name__)

def hashPassword(password):
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashedPassword

def configure():
    """Loads Secrets
    """
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
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
    
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
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
          
@app.route('/patients',methods=['GET','POST','DELETE'])
def patients():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()

        if request.method == 'GET':
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
                    lat = row['lat'],
                    lon = row['lon']
                )
                for row in cursor.fetchall()
            ]
            if patients is not None:
                return jsonify(patients),200

        if request.method == 'POST':
            contentJSON = request.get_json()

            patientID = requests.get('http://127.0.0.1:5000/patients/idgen').text
            patientName = contentJSON['patientName']
            patientEmail = contentJSON['patientEmail']
            patientPassword = hashPassword(contentJSON['patientPassword'])
            patientICNumber = contentJSON['patientICNumber']
            address = contentJSON['address']
            dateOfBirth = contentJSON['dateOfBirth'] # YYYY-MM-DD
            bloodType = contentJSON['bloodType']
            race = contentJSON['race']
            try:
                lat,lon = geoHelper.geocode(address=address)
            except Exception as e:
                lat,lon = None,None
    
            insertQuery = """
                            INSERT INTO patients (patientID,patientName,address,patientEmail,patientPassword,
                                                patientICNumber,dateOfBirth,bloodType,race,lat,lon)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            cursor = cursor.execute(insertQuery,(patientID,patientName,address,patientEmail,patientPassword,
                                                patientICNumber,dateOfBirth,bloodType,race,lat,lon))
            conn.commit() #Commit Changes to db, like git commit
            return'Successful POST', 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
   
@app.route('/patients/<string:id>',methods=['GET','DELETE'])
def patientID(id):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
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
                    lat = row['lat'],
                    lon = row['lon']
                )
                for row in cursor.fetchall()
            ]
            if patients is not None:
                return jsonify(patient),200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
          
@app.route('/patient/geocode/address',methods=['PATCH'])
def reGeocode():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                newDetailsEditJSON = request.get_json()
                address = newDetailsEditJSON['address']
                patientID = newDetailsEditJSON['patientID']
                try:
                    lat,lon = geoHelper.geocode(address=address)
                except Exception as e:
                    lat,lon = None,None

                cursor.execute("UPDATE patients SET address = %s, lat= %s, lon= %s where patientID = %s",(address,lat,lon,patientID))
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()   
        
@app.route('/clinics',methods=['GET','POST'])  
def clinics():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
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
                    lat = row['lat'],
                    lon = row['lon']
                )
                for row in cursor.fetchall()
            ]
            if clinics is not None:
                return jsonify(clinics),200
           
    if request.method == 'POST':
        contentJSON = request.get_json()

        clinicID = requests.get('http://127.0.0.1:5000/clinics/idgen').text
        clinicName = contentJSON['clinicName']
        clinicEmail = contentJSON['clinicEmail']
        clinicPassword = hashPassword(contentJSON['clinicPassword'])
        clinicContact = contentJSON['clinicContact']
        address = contentJSON['address']
        governmentApproved = 0
        lat,lon = geoHelper.geocode(address=address)
   

        insertQuery = """
                        INSERT INTO clinics (clinicID,clinicName,address,clinicEmail,clinicPassword,
                                            clinicContact,governmentApproved,lat,lon)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(clinicID,clinicName,address,clinicEmail,clinicPassword,
                                            clinicContact,governmentApproved,lat,lon))
        print('Success')  
        conn.commit() #Commit Changes to db, like git commit
        
        return f'Successful POST : {clinicID}',201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
    

@app.route('/clinics/<string:id>',methods=['GET','DELETE'])
def clinicID(id):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
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
                    lat = row['lat'],
                    lon = row['lon']
                )
                for row in cursor.fetchall()
            ]
            if clinics is not None:
                return jsonify(clinic),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()

@app.route('/clinics/unapproved',methods=['GET'])  
def clinicsUnapproved():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'GET':
            #Add Error Handling
            cursor.execute("SELECT * FROM clinics where governmentApproved = 'Pending'")
        
            clinics = [
                dict(
                    clinicID = row['clinicID'],
                    clinicName = row['clinicName'],
                    clinicContact = row['clinicContact'],
                    address = row['address'],
                    governmentApproved = row['governmentApproved'],
                    lat = row['lat'],
                    lon = row['lon']
                )
                for row in cursor.fetchall()
            ]
            if clinics is not None:
                return jsonify(clinics),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
        

@app.route('/clinics/approve/<string:clinicID>',methods=['PATCH'])
def clinicApprove(clinicID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE clinics SET governmentApproved = 'Approved' where clinicID = %s",clinicID)
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()      

@app.route('/clinics/cancel/<string:clinicID>',methods=['DELETE'])
def clinicCancel(clinicID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500

        cursor = conn.cursor()
        if request.method == 'DELETE':
            try:
                cursor.execute("DELETE FROM clinics where clinicID = %s",clinicID)
            except pymysql.MySQLError as e:
                return 'Error : ',e

            conn.commit()
            
            return 'Successful DELETE', 200    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()      
      
@app.route('/doctors', methods=['GET','POST'])
def doctors():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
    
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
            doctorName = contentJSON['doctorName']
            doctorPassword = hashPassword(contentJSON['doctorPassword'])
            doctorICNumber = contentJSON['doctorICNumber']
            doctorContact = contentJSON['doctorContact']
            doctorType = contentJSON['doctorType']
            yearOfExperience = contentJSON['yearOfExperience']
            doctorEmail = contentJSON['doctorEmail']
            status = "Unassigned"
            clinicID = None

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

            return f'Successful POST : {doctorID}',201
          
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
    finally:
        if conn is not None:
            conn.close()      




@app.route('/doctors/clinics/<string:clinicID>', methods=['GET'])
def doctorsClinic(clinicID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()    

@app.route('/doctors/<string:doctorID>',methods=['GET'])
def doctorsID(doctorID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()

        if request.method == 'GET':

            cursor.execute("SELECT * FROM doctors where doctorID = %s;",doctorID)
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
            
      
    

@app.route('/doctors/unassigned', methods=['GET'])
def doctorsUnassigned():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()

        if request.method == 'GET':
            #Add Error Handling
            cursor.execute("SELECT * FROM doctors where status = 'Unassigned'")

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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
            
        
@app.route('/doctors/<string:clinicID>/assign/<string:doctorID>',methods=['PATCH'])
def doctorClinicAssign(clinicID,doctorID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE doctors SET clinicID = %s, status = 'Active' where doctorID = %s",
                            (clinicID,doctorID))
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/doctors/unassign/<string:doctorID>',methods=['PATCH'])
def doctorClinicUnAssign(doctorID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500

        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE doctors SET clinicID = %s, status = 'Unassigned' where doctorID = %s",
                            (None,doctorID))
            except pymysql.MySQLError as e:
                return 'Error : ',e
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/doctors/pastpatients/<string:doctorID>',methods=['GET'])
def doctorPastPatients(doctorID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()

        if request.method == 'GET':
            #Add Error Handling
            cursor.execute("""SELECT * FROM patients where patientID in 
                        (SELECT patientID FROM appointments where doctorID = %s)""",doctorID)
        
            patients = [
                dict(
                    patientID = row['patientID'],
                    patientName = row['patientName'],
                    address = row['address'],
                    dateOfBirth = row['dateOfBirth'],
                    patientICNumber = row['patientICNumber'],
                    bloodType = row['bloodType'],
                    race = row['race'],  
                    lat = row['lat'],
                    lon= row['lon'],  
                )
                for row in cursor.fetchall()
            ]
            if patients is not None:
                return jsonify(patients),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
        


@app.route('/appointments', methods=['GET','POST','DELETE'])
def appointments():
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'GET':
            #Add Error Handling
            cursor.execute("SELECT * FROM appointments ORDER BY appointmentDate, startTime")

            appointments = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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

            appointmentID = requests.get('http://127.0.0.1:5000/appointments/idgen').text
            doctorID  = ""
            clinicID = contentJSON['clinicID']
            patientID = contentJSON['patientID']
            appointmentStatus = "Pending"
            startTime = contentJSON['startTime']
            appointmentDate = contentJSON['appointmentDate']
            visitReasons= contentJSON['visitReasons']

            insertQuery = """
                            INSERT INTO appointments (appointmentID,clinicID,doctorID,patientID,appointmentStatus,startTime,
                                                appointmentDate,visitReasons)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                        """
            cursor = cursor.execute(insertQuery,(appointmentID,clinicID,doctorID,patientID,appointmentStatus,startTime,
                                                appointmentDate,visitReasons))
            conn.commit() #Commit Changes to db, like git commit
            return'Successful POST', 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
        

@app.route('/appointments/<string:id>',methods=['GET','DELETE'])
def appointmentID(id):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM appointments where appointmentID = %s",id)
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  


@app.route('/appointments/past/<string:patientID>',methods=['GET'])
def appointmentPatientID(patientID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM appointments where patientID = %s", patientID)
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/appointments/toDate',methods=['GET'])
def appointmentToDate():
    todayDate =datetime.today().date()
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM appointments where appointmentDate <= %s ", todayDate)
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  




@app.route('/appointments/<string:aid>/assign/<string:did>',methods=['PATCH'])
def appointmentDoctorAssign(aid,did):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE appointments SET doctorID = %s, appointmentStatus = 'Approved' where appointmentID = %s",(did,aid))
            except pymysql.MySQLError as e:
                return 'Error : ',e
              
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  




@app.route('/appointments/<string:aid>/deny',methods=['PATCH'])
def appointmentDeny(aid):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE appointments SET appointmentStatus = 'Cancelled' where appointmentID = %s",aid)
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/appointments/<string:aid>/approve',methods=['PATCH'])
def appointmentApprove(aid):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE appointments SET appointmentStatus = 'Approved' where appointmentID = %s",aid)
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/appointments/<string:aid>/complete',methods=['PATCH'])
def appointmentComplete(aid):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE appointments SET appointmentStatus = 'Completed' where appointmentID = %s",aid)
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/appointments/week',methods=['GET'])
def appointmentsWeek():
    dateToday = datetime.now().date() - timedelta(days= datetime.now().date().weekday())
    dateEnd = dateToday + timedelta(days=6)
    print(dateToday)
    print(dateEnd)
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()

        if request.method == 'GET':
            cursor.execute("SELECT * FROM appointments where appointmentDate BETWEEN %s AND %s ORDER BY appointmentDate, startTime"
                            ,(dateToday,dateEnd))
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
        

@app.route('/appointments/upcoming/doctor/<string:doctorID>',methods=['GET'])
def appointmentsDoctorUpcoming(doctorID):
    dateToday = datetime.now().date() - timedelta(days= datetime.now().date().weekday())
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("""SELECT * FROM appointments where appointmentDate >= %s AND 
                        doctorID = %s ORDER BY appointmentDate, startTime LIMIT 3"""
                            ,(dateToday,doctorID))
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  


@app.route('/appointments/upcoming/patient/<string:patientID>',methods=['GET'])
def appointmentsPatientUpcoming(patientID):
    dateToday = datetime.now().date() - timedelta(days= datetime.now().date().weekday())
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("""SELECT * FROM appointments where appointmentDate >= %s AND 
                        patientID = %s ORDER BY appointmentDate, startTime LIMIT 3"""
                            ,(dateToday,patientID))
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  


@app.route('/appointments/<string:clinicID>/pending',methods=['GET'])
def appointmentsPending(clinicID):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM appointments where appointmentStatus = %s AND clinicID = %s ORDER BY appointmentDate, startTime"
                            ,('Pending',clinicID))
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/appointments/week/<string:doctorID>',methods=['GET'])
def appointmentsWeekID(doctorID):
    dateToday = datetime.now().date() - timedelta(days= datetime.now().date().weekday())
    dateEnd = dateToday + timedelta(days=6)
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()

        if request.method == 'GET':
            cursor.execute("""SELECT * FROM appointments where doctorID = %s AND
                        appointmentDate BETWEEN %s AND %s """,(doctorID,dateToday,dateEnd))
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/appointments/today/<string:clinicID>',methods=['GET'])
def appointmentsClinicWeek(clinicID):
    dateToday = datetime.now().date()
    print(dateToday)
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()

        if request.method == 'GET':
            cursor.execute("""SELECT * FROM appointments where clinicID = %s AND
                        appointmentDate = %s""",(clinicID,dateToday))
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
            
            
@app.route('/appointments/doctor/<string:doctorID>',methods=['GET'])
def appointmentsByDoctor(doctorID):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM appointments where doctorID = %s ",doctorID)
            appointment = [
                dict(
                    appointmentID = row['appointmentID'],
                    doctorID  = row['doctorID'],
                    clinicID = row['clinicID'],
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
            
        
@app.route('/appointments/<string:id>/find/<string:clinicID>',methods=['GET'])
def appointmentsFind(id,clinicID):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
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
                            ) AND clinicID = %s
                            """,(date,appointment['startTime'],clinicID))
            appointment = [
                dict(
                    doctorID  = row['doctorID']
                )
                for row in cursor.fetchall()
            ]
            if appointment is not None:
                return jsonify(appointment),200    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()

@app.route('/prescriptions', methods=['GET','POST','DELETE'])
def prescriptions():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
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

            prescriptionID = contentJSON['prescriptionID']
            appointmentID  = contentJSON['appointmentID']
            expiryDate = contentJSON['expiryDate']

            insertQuery = """
                            INSERT INTO prescriptions (prescriptionID,appointmentID,expiryDate
                                                )
                            VALUES (%s,%s,%s)
                        """
            cursor = cursor.execute(insertQuery,(prescriptionID,appointmentID,expiryDate
                                                ))
            conn.commit() #Commit Changes to db, like git commit
            return'Successful POST', 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()



@app.route('/prescriptions/<string:id>',methods=['GET','DELETE'])
def prescriptionID(id):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()

    
@app.route('/prescriptions/appointments/<string:id>',methods=['GET','DELETE'])
def prescriptionAppointmentID(id):

    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM prescriptions where appointmentID = %s",id)
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
        
@app.route('/prescriptions/patients/<string:id>',methods=['GET','DELETE'])
def prescriptionPatientID(id):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("""SELECT * FROM prescriptions where appointmentID in (SELECT 
                        appointmentID FROM appointments where patientID = %s)""",id)
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()

    
@app.route('/prescriptionDetails/<string:id>',methods=['GET','DELETE'])
def prescriptionDetailsID(id):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM prescription_details where prescriptionID = %s",id)
            prescription = [
                dict(
                    medicationName = row['medicationName'],
                    pillsPerDay  = row['pillsPerDay'],
                    food = row['food'],
                    dosage = row['dosage']
                )
                for row in cursor.fetchall()
            ]
            if prescription is not None:
                return jsonify(prescription),200
        if request.method == 'DELETE':
            try:
                cursor.execute("DELETE FROM prescription_details WHERE prescriptionID = %s",id)
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            return 'Successful DELETE', 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()

    
@app.route('/prescriptionDetails', methods=['POST'])
def prescriptionDetails():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'POST':
            contentJSON = request.get_json()

            prescriptionID =contentJSON['prescriptionID']
            appointmentID =  contentJSON['appointmentID']
            medicationName = contentJSON['medicationName']
            pillsPerDay = contentJSON['pillsPerDay']
            food = contentJSON['food']
            dosage = contentJSON['dosage']

            insertQuery = """
                            INSERT INTO prescription_details (prescriptionID,appointmentID,medicationName
                                                            ,pillsPerDay,food,dosage)
                            VALUES (%s,%s,%s,%s,%s,%s)
                        """
            cursor = cursor.execute(insertQuery,(prescriptionID,appointmentID,medicationName
                                                ,pillsPerDay,food,dosage))
            conn.commit() #Commit Changes to db, like git commit
            return'Successful POST', 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()
    
@app.route('/requests',methods=['GET','POST'])
def allRequests():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM requests")

            reqs = [
                dict(
                    requestsID = row['requestsID'],
                    requestsType = row['requestsType'],
                    clientID  = row['clientID'],
                    approvalStatus = row['approvalStatus'],
                    dateSubmitted = row['dateSubmitted'],
                    requestReason = row['requestReason'],
                    appointmentID = row['appointmentID']
                )
                for row in cursor.fetchall()
            ]

            if reqs is not None:
                return jsonify(reqs),200
            
        if request.method == 'POST':
            
            contentJSON = request.get_json()
            reqsID =  requests.get('http://127.0.0.1:5000/requests/idgen').text
            reqsType = contentJSON['requestsType']
            clientID = contentJSON['clientID']
            approvalStatus = 'Pending'
            dateSubmitted = datetime.now().date() 
            requestReason = contentJSON['requestReason']
            appointmentID = contentJSON['appointmentID']

            insertQuery = """
                            INSERT INTO requests (requestsID,requestsType,clientID,approvalStatus,
                                                dateSubmitted,requestReason,appointmentID)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                        """

            cursor = cursor.execute(insertQuery,(reqsID,reqsType,clientID,approvalStatus,
                                                dateSubmitted,requestReason,appointmentID)
                                                )
            conn.commit() #Commit Changes to db, like git commit
            return'Successful POST', 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()    
    


@app.route('/requests/<string:clinicID>',methods=['GET'])
def requestsByClinic(clinicID):
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM requests where appointmentID in(SELECT appointmentID from clinics where clinicID = %s)",clinicID)
            requests = [
                dict(
                    requestsID = row['requestsID'],
                    requestsType = row['requestsType'],
                    clientID  = row['clientID'],
                    approvalStatus = row['approvalStatus'],
                    dateSubmitted = row['dateSubmitted'],
                    requestReason = row['requestReason'],
                    appointmentID = row['appointmentID']
                )
                for row in cursor.fetchall()
            ]
            if requests  is not None:
                return jsonify(requests),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()    
    
@app.route('/requests/cancel/<string:requestsID>',methods=['PATCH'])
def requestsCancel(requestsID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE requests SET requestsID = %s, approvalStatus = 'Rejected' where requestsID = %s",
                            (None,requestsID))
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/requests/approve/<string:requestsID>',methods=['PATCH'])
def requestsApprove(requestsID):
    try:
        conn = dbConnect()
        if conn is None:
            return jsonify({'Error': 'Failed to connect to the database'}), 500
        
        cursor = conn.cursor()
        if request.method == 'PATCH':
            try:
                cursor.execute("UPDATE requests SET requestsID = %s, approvalStatus = 'Approved' where requestsID = %s",
                            (None,requestsID))
            except pymysql.MySQLError as e:
                return 'Error : ',e
        
            conn.commit()
            
            return 'Successful PATCH', 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/graph/users', methods=['GET'])
def generateGraph():
    appointments = requests.get(f"http://127.0.0.1:5000/appointments/toDate").json()
    df = pd.DataFrame(columns=['dates', 'count'])
    dateFormat = "%a, %d %b %Y %H:%M:%S %Z"
    df['dates'] = [datetime.strptime(dates['appointmentDate'], dateFormat)
                   .strftime("%d-%m-%Y") for dates in appointments]

    uniqueDates = df['dates'].value_counts().reset_index()

    return uniqueDates.to_json()


@app.route('/users/auth')
def userAuthentication():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
            
        cursor = conn.cursor()
    
        contentJSON = request.get_json()

        cursor.execute('SELECT ID,role,password from users where email = %s',(email))

        try:
            sessionInfo = cursor.fetchone()
            storedHashPass = sessionInfo['password'].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'),storedHashPass):
                validInfo = {'ID': sessionInfo['ID'], 'role': sessionInfo['role']}
                return jsonify(validInfo), 200
        except:
            sessionInfo = None;


    except Exception as e:
       return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/doctors/idgen')
def getLastDoctorID():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
          
        cursor = conn.cursor()
        #Add Error Handling
        cursor.execute("SELECT COUNT(*) FROM doctors")
        counter = cursor.fetchall()
        id = counter[0]['COUNT(*)']
        if id == 0:
            id = f'D{str(id).zfill(3)}'
        else:
            cursor.execute("SELECT MAX(doctorID) FROM doctors")
            id  = cursor.fetchone()['MAX(doctorID)']

            print(id)
            id = str(int(id.strip('D'))+1)
            id = f'D{id.zfill(3)}'

        if id is not None:
                return id,200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  


@app.route('/patients/idgen')
def getLastPatientID():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
          
        cursor = conn.cursor()
        #Add Error Handling
        cursor.execute("SELECT COUNT(*) FROM patients")
        counter = cursor.fetchall()
        id = counter[0]['COUNT(*)']
        if id == 0:

            id = f'P{str(id).zfill(3)}'
        else:
            cursor.execute("SELECT MAX(patientID) FROM patients")
            id  = cursor.fetchone()['MAX(patientID)']
            id = str(int(id.strip('P'))+1)
            id = f'P{id.zfill(3)}'

        if id is not None:
                return id,200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  


@app.route('/clinics/idgen')
def getLastClinicID():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
          
        cursor = conn.cursor()
        #Add Error Handling
        cursor.execute("SELECT COUNT(*) FROM clinics")
        counter = cursor.fetchall()
        id = counter[0]['COUNT(*)']
        if id == 0:
            id = f'C{str(id).zfill(3)}'
        else:
            cursor.execute("SELECT MAX(clinicID) FROM clinics")
            id  = cursor.fetchone()['MAX(clinicID)']

            id = str(int(id.strip('C'))+1)
            id = f'C{id.zfill(3)}'

        if id is not None:
                return id,200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  
   
@app.route('/appointments/idgen')
def getLastAppointmentsID():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
          
        cursor = conn.cursor()
        #Add Error Handling
        cursor.execute("SELECT COUNT(*) FROM appointments")
        counter = cursor.fetchall()
        id = counter[0]['COUNT(*)']
        print(id)
        if id == 0:
            id = f'A{str(id).zfill(3)}'
        else:
            cursor.execute("SELECT MAX(appointmentID) FROM appointments")
            id  = cursor.fetchone()['MAX(appointmentID)']
            print(id)

            id = str(int(id.strip('A'))+1)
            id = f'A{id.zfill(3)}'

        if id is not None:
                return id,200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/prescriptions/idgen')
def getLastPrescriptionID():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
          
        cursor = conn.cursor()
        #Add Error Handling
        cursor.execute("SELECT COUNT(*) FROM prescriptions")
        counter = cursor.fetchall()
        id = counter[0]['COUNT(*)']
        if id == 0:
            id = f'PR{str(id).zfill(3)}'
        else:
            cursor.execute("SELECT MAX(prescriptionID) FROM prescriptions")
            id  = cursor.fetchone()['MAX(prescriptionID)']

            id = str(int(id.strip('PR'))+1)
            id = f'PR{id.zfill(3)}'

        if id is not None:
                return id,200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn is not None:
            conn.close()  

@app.route('/requests/idgen')
def getLastRequestsID():
    try:
        conn = dbConnect()
        if conn is None:
             return jsonify({'Error': 'Failed to connect to the database'}), 500
          
        cursor = conn.cursor()
        #Add Error Handling
        cursor.execute("SELECT COUNT(*) FROM requests")
        counter = cursor.fetchall()
        id = counter[0]['COUNT(*)']
        if id == 0:
            id = f'REQ{str(id).zfill(3)}'
        else:
            cursor.execute("SELECT MAX(requestsID) FROM requests")
            id  = cursor.fetchone()['MAX(requestsID)']

            id = str(int(id.strip('REQ'))+1)
            id = f'REQ{id.zfill(3)}'

        if id is not None:
                return id,200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
      
    finally:
        if conn is not None:
            conn.close()  
   

@app.route('/clinics/image/upload/<string:id>', methods=['POST'])
def uploadClinicImage(id):
    conn = dbConnect()  
    cursor = conn.cursor()
   
    if request.method == 'POST':
        try:
            file = request.files['file']
            imgData = file.read()
            cursor.execute("UPDATE clinics SET verifiedDoc = %s WHERE clinicID = %s", (imgData, id))
            conn.commit()
            conn.close()
            return jsonify({"Message": "Image uploaded and processed successfully"})
        except:
            return jsonify({'Error':'Image Error'})

@app.route('/clinics/image/download/<string:id>', methods=['GET'])
def downloadClinicImage(id):
    conn = dbConnect()  
    cursor = conn.cursor()
   
    if request.method == 'GET':
        try:
            cursor.execute("SELECT verifiedDoc from clinics where clinicID = %s", id)
            imgData = cursor.fetchone()

            conn.commit()
            conn.close()

            return imgData['verifiedDoc']
        except:
            return jsonify({'Error':'Image Error'})
    

@app.route('/doctors/image/upload/<string:id>', methods=['POST'])
def uploadDoctorsImage(id):
    conn = dbConnect()  
    cursor = conn.cursor()
   
    if request.method == 'POST':
        try:
            file = request.files['file']
            imgData = file.read()
            cursor.execute("UPDATE doctors SET certifiedDoc = %s WHERE doctorID = %s", (imgData, id))
            conn.commit()
            conn.close()
            return jsonify({"Message": "Image uploaded and processed successfully"})
        except:
            return jsonify({'Error':'Image Error'})

@app.route('/doctors/image/download/<string:id>', methods=['GET'])
def downloadDoctorsImage(id):
    conn = dbConnect()  
    cursor = conn.cursor()
   
    if request.method == 'GET':
        try:
            cursor.execute("SELECT certifiedDoc from doctors where doctorID = %s", id)
            imgData = cursor.fetchone()

            conn.commit()
            conn.close()

            return imgData['certifiedDoc']
        except:
            return None, jsonify({'Error':'Image Error'})
    
    
if __name__ == "__main__":
    app.run(debug=True)