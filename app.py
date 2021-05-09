from flask_wtf.csrf import CSRFProtect
from flask import Flask, session, redirect, url_for, render_template
from flask_session import Session
from flask.json import jsonify
import json
import redis


app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
app.secret_key = b"""I_.5qLr#ya2L'F4bvaasdf1Q8zxec]"""

# Configure Redis for storing the session data on the server-side
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://redis:6379')

# Create and initialize the Flask-Session object AFTER `app` has been configured
server_session = Session(app)

pps_students = [
    {"id": 1, "firstname": "Miguel", "lastname": "Moreno"},
    {"id": 2, "firstname": "Felipe", "lastname": "López"},
    {"id": 3, "firstname": "Antonio", "lastname": "Zamora"},
    {"id": 4, "firstname": "Enrique", "lastname": "Arias"},
    {"id": 5, "firstname": "Alberto", "lastname": "Pardo"}
]

@app.route("/")
def students():
    if "students" not in session:
        session["students"] = pps_students.copy()
    return render_template("students.html", students=session["students"])

@app.route("/ayuda")
def help():
    return render_template("help.html")

@app.route("/borrar/<student_id>", methods=['POST'])
def delete(student_id):
    mystudents = session["students"]
    for student in mystudents:
        if student["id"] == int(student_id):
            mystudents.remove(student)
            break
    session["students"] = mystudents
    return redirect(url_for('students'))
    

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for('students'))


if __name__ == "__main__":
    app.run(port=80, debug=False, host="0.0.0.0", threaded=True)
