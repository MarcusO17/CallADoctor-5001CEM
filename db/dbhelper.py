import pymysql
from dotenv import load_dotenv
import os

#Loading Secrets (DB Credentials)
load_dotenv()

conn = pymysql.connect(
        host=os.getenv('SQL_hostname'),
        database=os.getenv('SQL_database_name'),
        user=os.getenv('SQL_username'),
        passwd=os.getenv('PWD'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )

cursor = conn.cursor()



def addAutoIncrement(table,value):
    return f"ALTER TABLE {table} AUTO_INCREMENT={value};"

#SQL Statements for Table Creation
createUserTable = '''CREATE TABLE users (
                     userID INTEGER PRIMARY KEY,
                     email TEXT NOT NULL,
                     password TEXT NOT NULL,
                     role TEXT NOT NULL
                )'''

createPatientTable = '''CREATE TABLE patients (
                     patientID INTEGER PRIMARY KEY AUTO_INCREMENT,
                     patientName TEXT NOT NULL,
                     address TEXT NOT NULL,
                     dateOfBirth DATE NOT NULL,
                     bloodType TEXT,
                     race TEXT
                     )'''

createClinicTable = '''CREATE TABLE clinics (
                     clinicID INTEGER PRIMARY KEY,
                     clinicName TEXT NOT NULL,
                     address TEXT NOT NULL,
                     governmentApproved BOOLEAN NOT NULL
                     )
                    '''

createDoctorTable = '''CREATE TABLE doctors (
                     doctorID INTEGER PRIMARY KEY,
                     clinicID INTEGER NOT NULL,
                     doctorName TEXT NOT NULL,
                     status TEXT NOT NULL,
                     FOREIGN KEY (clinicID) REFERENCES clinics(clinicID)
                     )'''

#Table Creation

#cursor.execute(createUserTable)
cursor.execute(createPatientTable)
#cursor.execute(createClinicTable)
#cursor.execute(createDoctorTable)

cursor.execute(addAutoIncrement('patients',1000))

conn.close()
