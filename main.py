from json import load
from pprint import pprint

from pymongo import MongoClient

with open('secrets.json', 'r') as secrets_json:
    secrets = load(secrets_json)
    database_pass = secrets["database_pass"]
    database_user = secrets["database_user"]

# Database initialisation

client = MongoClient(
    f"mongodb+srv://{database_user}:{database_pass}@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")

db = client.time_tracking

#Find out minutes logged

minutes = db.timelog.aggregate(
    [
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
                                    "unit": "hour"
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
                    "as": "course_name"
                }
        },
{
    "$unwind": "$course_name"
},
{
        "$project": {
          "_id": 1,
          "name": 1,
          "averageTime": {
                      "$divide": [ "$averageTime", 60 ]
                   },
          "course_name.title": 1,
        "course_name.duration": 1,
        }
      }
    ]
)

for x in minutes:
    print(x)

# TODO filter by target student and course and return precentage