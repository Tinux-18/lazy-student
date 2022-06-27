from json import load
from pprint import pprint

from bson import ObjectId
from pymongo import MongoClient

with open('secrets.json', 'r') as secrets_json:
    secrets = load(secrets_json)
    database_pass = secrets["database_pass"]
    database_user = secrets["database_user"]

# Database initialisation

client = MongoClient(
    f"mongodb+srv://{database_user}:{database_pass}@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")

db = client.time_tracking

target_student_name = "Samuel Cochran"
target_course_id = ObjectId("62b707d4e700f67ac1e2eff7")

#Find out minutes logged

minutes = db.timelog.aggregate(
    [
    {'$match': {'name': target_student_name, 'course_id': target_course_id}},
       {
          "$group":
             {
                 "_id": {
             "name": "$name",
             "course_id": "$course_id"
            },
                 "averageTime":
                    {
                       "$avg":
                          {
                             "$dateDiff":
                                {
                                    "startDate": "$login",
                                    "endDate": "$logout",
                                    "unit": "minute"
                                }
                           }
                    }
             }
       },
        {
            "$lookup":
                {
                    "from": "courses",
                    "localField": "_id.course_id",
                    "foreignField": "_id",
                    "as": "course"
                }
        },
{
    "$unwind": "$course"
},
{
        "$project": {
          "_id": 1,
          "name": 1,
          "averageHours": {
                      "$divide": [ "$averageTime", 60 ]
                   },
          "course.title": 1,
          "course.duration": 1,
          "progress": {"$divide": [
                        {"$multiply": [
                            {"$divide": [
                                "$averageTime",
                                60]
                            },
                            100]
                        },
                        "$course.duration"]}
        }
      }
    ]
)

for x in minutes:
    print(x)