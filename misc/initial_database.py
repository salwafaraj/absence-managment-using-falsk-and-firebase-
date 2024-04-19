import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://system-for-student-attendance-default-rtdb.firebaseio.com/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "004223": {  # id of student which is a key
        "id": "004223",
        "name": "Allali Ghali",
        "password": "004223ghali",
        "dob": "1997-08-02",
        "address": "Khouribga",
        "phone": "2348657951",
        "email": "ghali@gmail.com",
        "major": "Data Science",
        "starting_year": 2020,
        "standing": "IID1",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },

"004228": {  # id of student which is a key
        "id": "004228",
        "name": "Allaoui Aya",
        "password": "004223aya",
        "dob": "1997-08-02",
        "address": "Khouribga",
        "phone": "2348657951",
        "email": "aya@gmail.com",
        "major": "Data Science",
        "starting_year": 2020,
        "standing": "IID1",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },

}


for key, value in data.items():
    ref.child(key).set(value)
