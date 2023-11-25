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

createPatientTable = '''CREATE TABLE patients (
                     patientID VARCHAR(64) PRIMARY KEY,
                     patientName TEXT NOT NULL,
                     patientEmail TEXT NOT NULL,
                     patientPassword TEXT NOT NULL,
                     patientICNumber TEXT UNIQUE,
                     address TEXT NOT NULL,
                     lat FLOAT,
                     lon FLOAT,
                     dateOfBirth DATE NOT NULL,
                     bloodType TEXT,
                     race TEXT
                     )'''

createClinicTable = '''CREATE TABLE clinics (
                     clinicID VARCHAR(64) PRIMARY KEY,
                     clinicName TEXT NOT NULL,
                     clinicEmail  TEXT NOT NULL,
                     clinicPassword TEXT NOT NULL,
                     clinicContact TEXT NOT NULL,
                     verifiedDoc BLOB,
                     address TEXT NOT NULL,
                     lat FLOAT,
                     lon FLOAT,
                     governmentApproved TEXT NOT NULL
                     )
                    '''

createDoctorTable = '''CREATE TABLE doctors (
                     doctorID VARCHAR(64) PRIMARY KEY,
                     clinicID VARCHAR(64),
                     doctorEmail  TEXT NOT NULL,
                     doctorPassword TEXT NOT NULL,
                     doctorContact TEXT  NOT NULL,
                     doctorName TEXT NOT NULL,
                     doctorType TEXT NOT NULL,
                     doctorICNumber TEXT UNIQUE,
                     certifiedDoc BLOB,
                     yearOfExperience TEXT,
                     status TEXT NOT NULL,
                     FOREIGN KEY (clinicID) REFERENCES clinics(clinicID)
                     )'''


createAppointmentTable = '''CREATE TABLE appointments (
                     appointmentID VARCHAR(64) PRIMARY KEY,
                     doctorID VARCHAR(64),
                     clinicID VARCHAR(64),
                     patientID VARCHAR(64),
                     appointmentStatus TEXT NOT NULL,
                     startTime TIME NOT NULL,
                     endTime TIME NOT NULL,
                     appointmentDate DATE NOT NULL,
                     status TEXT NOT NULL,
                     visitReasons TEXT,
                     FOREIGN KEY (patientID) REFERENCES patients(patientID)
                     )'''

createPrescriptionTable = '''CREATE TABLE prescriptions (
                     prescriptionID VARCHAR(64) PRIMARY KEY,
                     appointmentID VARCHAR(64) NOT NULL,
                     expiryDate DATE NOT NULL,
                     FOREIGN KEY (appointmentID) REFERENCES appointments(appointmentID)
                     )'''

createPrescriptionDetailsTable = '''CREATE TABLE prescription_details (
                     prescriptionID VARCHAR(64) NOT NULL,
                     appointmentID VARCHAR(64) NOT NULL,
                     medicationName TEXT NOT NULL,
                     pillsPerDay INTEGER NOT NULL,
                     food TEXT,
                     dosage INT,
                     FOREIGN KEY (prescriptionID) REFERENCES prescriptions(prescriptionID),
                     FOREIGN KEY (appointmentID) REFERENCES appointments(appointmentID)
                     )'''

createAdminTable = '''CREATE TABLE admins (
                     adminID VARCHAR(64) NOT NULL,
                     adminEmail TEXT NOT NULL,
                     adminPassword TEXT NOT NULL)       
                    '''

createRequestsTable = '''CREATE TABLE requests (
                     requestsID VARCHAR(64) PRIMARY KEY,
                     requestsType TEXT NOT NULL,
                     clientID TEXT NOT NULL,
                     approvalStatus TEXT NOT NULL,
                     dateSubmitted DATE NOT NULL,
                     requestReason TEXT NOT NULL,
                     appointmentID TEXT NOT NULL
                     FOREIGN KEY (appointmentID) references appointments(appointmentID)
                     CONSTRAINT chk_approvalStatus CHECK (approvalStatus IN ('Pending', 'Approved', 'Rejected'))
                     )       
                    '''

#Table Creation


#cursor.execute(createPatientTable)
#cursor.execute(createClinicTable)
#cursor.execute(createDoctorTable)
#cursor.execute(createAppointmentTable)
#cursor.execute(createPrescriptionTable)
#cursor.execute(createPrescriptionDetailsTable)

#CreateView
userViewCreate = """ CREATE VIEW users AS 
                     SELECT patientID as ID, patientEmail as email, patientPassword as password, 'patient' as role FROM patients
                     UNION ALL
                     SELECT doctorID as ID, doctorEmail as email, doctorPassword as password, 'doctor' as role FROM doctors
                     UNION ALL
                     SELECT clinicID as ID, clinicEmail as email, clinicPassword as password, 'clinic' as role FROM clinics
                     UNION ALL
                     SELECT adminID as ID, adminEmail as email, adminPassword as password, 'admin' as role FROM admins
                """

#cursor.execute(userViewCreate)
cursor.close()
conn.close()
