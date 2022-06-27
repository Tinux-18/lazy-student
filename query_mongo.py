from json import load
from bson import ObjectId
from pymongo import MongoClient

with open("secrets.json", "r") as secrets_json:
    secrets = load(secrets_json)
    database_pass = secrets["database_pass"]
    database_user = secrets["database_user"]

# Database initialisation

client = MongoClient(
    f"mongodb+srv://{database_user}:{database_pass}@cluster0.4jo8n.mongodb.net/?retryWrites=true&w=majority")

db = client.time_tracking


def get_progress(student_name, course_id):
    course_obj_id = ObjectId(course_id)
    return db.timelog.aggregate(
        [
            {'$match': {'name': student_name, 'course_id': course_obj_id}},
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
                        "$divide": ["$averageTime", 60]
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


def get_courses():
    items = []
    cursor = db.courses.find({}, {"_id": 0, "title": 1})
    for i in cursor:
        items.append(i["title"])
    return items


def get_students():
    items = []
    cursor = db.timelog.find({}, {"_id": 0, "name": 1})
    for i in cursor:
        if i["name"] not in items:
            items.append(i["name"])
    return items
