import datetime
from flask import Flask

app = Flask(__name__)


studentsDb = [
    {"id": 1, "name": "John", "age": 20},
    {"id": 2, "name": "Jane", "age": 22},
    {"id": 3, "name": "Joe", "age": 21}
]

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the Python Web Server! - today's date " +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route("/students", methods=["GET"])
def get_students():
    return {"students": studentsDb}

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for student in studentsDb:
        if student["id"] == id:
            return student
    return {"error": "Student not found"}

if (__name__ == "__main__"):
    app.run()