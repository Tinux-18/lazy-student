from datetime import timedelta
from json import load
from random import choice
from pymongo import MongoClient
from faker import Faker

with open('../secrets.json', 'r') as secrets_json:
    secrets = load(secrets_json)
    database_pass = secrets["database_pass"]
    database_user = secrets["database_user"]

# Data ingestion

with open('data/courses.json', 'r') as secrets:
    courses = load(secrets)["data"]

# Database initialisation

client = MongoClient(
    f"mongodb+srv://{database_user}:{database_pass}@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")

db = client.time_tracking

# Insert courses into database

# for i in courses:
#     course = {
#                 "title": i["item"],
#                 "duration": Faker().random.randint(8,28)
#                 }
#     result = db.courses.insert_one(course)
#     print(f"Course '{course['title']}' created with id {result.inserted_id}")

# Insert students into database

# Get course ids

course_ids = []
for course in db.courses.find({"duration": {"$gt":0}}, "_id"):
    course_ids.append(course["_id"])

for _ in range(20):
    name = Faker().name()
    logs = []
    for _ in range(5):
        login_datetime = Faker().date_time_this_month()
        logout_datetime = login_datetime + timedelta(seconds=Faker().random.randint(60, 3600))
        logs.append({'name': name, 'login': login_datetime, 'logout': logout_datetime, 'course_id': choice(course_ids)})
    result = db.timelog.insert_many(logs)
    print(f"Student '{logs[0]['name']}' created with id {result}")
