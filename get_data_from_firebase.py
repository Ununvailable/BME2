import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase app
cred = credentials.Certificate('./bme2-b643c-firebase-adminsdk-z7fnn-4a2fc7720a.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://bme2-b643c-default-rtdb.asia-southeast1.firebasedatabase.app/'})

ref = db.reference('/2023-03-13')
data = ref.get()
# data_dict = json.loads(json.dumps(data))
print(data)