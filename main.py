from flask import Flask, request
from flask_cors import CORS
from json import dumps
from query_mongo import get_progress, get_students, get_courses

# Building Flask

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_lists():
    return dumps({"courses": get_courses(), "students": get_students()})

@app.route('/get-progress')
def get_student_progress():
    progress = get_progress(request.args.get("student"), request.args.get("course_id"))._CommandCursor__data[0]
    print(progress)
    return dumps({"student": request.args.get("student"), "course": progress["course"]["title"], "progress": f'{progress["progress"]} %'})
