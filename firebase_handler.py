import firebase_admin
from firebase_admin import credentials, db

def init_firebase():
    cred = credentials.Certificate("/home/k00288477/CalmSpace/calmspace-firebase.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://calmspace-e334d-default-rtdb.europe-west1.firebasedatabase.app/"
    })

def push_readings(readings):
    try:
        ref = db.reference("/readings")
        ref.push({
            "temperature": readings["temperature"],
            "humidity": readings["humidity"],
            "noise": readings["noise"],
            "timestamp": {".sv": "timestamp"}
        })
        print("Readings pushed to Firebase")
    except Exception as e:
        print(f"Firebase error: {e}")
