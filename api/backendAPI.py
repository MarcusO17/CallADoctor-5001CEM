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



@app.route('/users',methods=['GET','POST'])
def users():
    conn = dbConnect()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM users')
        users = [
            dict(
            userID = row['userID'],
            email = row['email'],
            password = row['password'],
            role = row['role']
            )
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users), 200
        
    
    if request.method == 'POST':
        contentJSON = request.get_json()

        userID = contentJSON['userID']
        email = contentJSON['email']
        password = contentJSON['password'] # YYYY-MM-DD
        role = contentJSON['role']
      
   
        insertQuery = """
                        INSERT INTO patients (userID,email,
                                           password,role)
                        VALUES (%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(userID,email,password,
                                             role))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    

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

        patientName = contentJSON['patientName']
        address = contentJSON['address']
        dateOfBirth = contentJSON['dateOfBirth'] # YYYY-MM-DD
        bloodType = contentJSON['bloodType']
        race = contentJSON['race']
   
        insertQuery = """
                        INSERT INTO patients (patientName,address,
                                            dateOfBirth,bloodType,race)
                        VALUES (%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(patientName,address,dateOfBirth,
                                             bloodType,race))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    
    if request.method == 'DELETE':
        try:
            cursor.execute("DROP TABLE patients")
        except pymysql.MySQLError as e:
            return 'Error : ',e
        return 'Successful DELETE', 200
    
  
@app.route('/patients/<int:id>',methods=['GET','DELETE'])
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

        clinicName = contentJSON['clinicName'],
        address = contentJSON['address'],
        governmentApproved = contentJSON['governmentApproved'],
   
        insertQuery = """
                        INSERT INTO clinics (clinicName,address,
                                            governmentApproved)
                        VALUES (%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(clinicName,address,
                                            governmentApproved))
        conn.commit() #Commit Changes to db, like git commit
        return'Successful POST', 201
    
    if request.method == 'DELETE':
        #cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute("DROP TABLE clinics")
        #cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        
        return 'Successful DELETE', 200
    
    
        
#DELETE PATIENT BY ID

if __name__ == "__main__":
    app.run()