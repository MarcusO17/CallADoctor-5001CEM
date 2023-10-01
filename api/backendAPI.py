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

@app.route('/patients',methods=['GET','POST'])
def patients():
    conn = dbConnect()
    cursor = conn.cursor()
    if request.method == 'GET':
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

        patientID = request.form['patientID']
        patientName = request.form['patientName']
        address = request.form['address']
        dateOfBirth = request.form['dateOfBirth'] # YYYY-MM-DD
        bloodType = request.form['bloodType']
        race = request.form['race']

        insertQuery = """
                        INSERT INTO patients (patientID,patientName,address,
                                            dateOfBirth,bloodType,race)
                        VALUES (%s,%s,%s,%s,%s,%s)
                      """
        cursor = cursor.execute(insertQuery,(patientID,patientName,address,dateOfBirth,
                                             bloodType,race))
        conn.commit()
        return'Successful POST', 200
    

        


if __name__ == "__main__":
    app.run()