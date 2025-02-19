import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    
    return "Welcome to the Python Web Server! - today's date " +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if (__name__ == "__main__"):
    app.run()