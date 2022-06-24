from json import load

from pymongo import MongoClient
from faker import Faker
fake = Faker()

print(fake.random.randint(1,18))

with open('secrets.json', 'r') as secrets:
    database_pass = load(secrets)["database_pass"]

# Ingest data

with open('data/courses.json', 'r') as secrets:
    courses = load(secrets)["data"]

# Database initialisation

client = MongoClient(
    f"mongodb+srv://lazystudent:{database_pass}@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")

db = client.time_tracking  # defining the database

# Insert local data into database
