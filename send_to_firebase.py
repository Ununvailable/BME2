import csv
import firebase_admin
from firebase_admin import credentials, db, auth
import datetime
import pytz

# set the timezone to Vietnam's timezone
vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')

# get the current datetime in Vietnam's timezone
current_time_vietnam = datetime.datetime.now(tz=vietnam_tz)

# format the datetime as a string
current_time_vietnam_str = current_time_vietnam.strftime("%Y-%m-%d")

# Initialize Firebase app
cred = credentials.Certificate('./bme2-b643c-firebase-adminsdk-z7fnn-4a2fc7720a.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://bme2-b643c-default-rtdb.asia-southeast1.firebasedatabase.app/'})

# get a reference to the Firebase Realtime Database
ref = db.reference(current_time_vietnam_str)

# open and read the CSV file
with open('angle_three_sensor.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # create a dictionary with the row data
        data = {
            'ang1': row['ang1'],
            'ang2': row['ang2'],
            'ang3': row['ang3'],
            'ang4': row['ang4'],
            'ang5': row['ang5']
            # add more columns as needed
        }
        # set the data in the Firebase Realtime Database
        ref.push().set(data)