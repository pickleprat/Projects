from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json 

app = Flask(__name__)

with open('config.json', 'r') as json_file:
    json_obj = json.load(json_file)['params']


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/medicaldb'

db = SQLAlchemy(app)

class Complaints(db.Model):

    complaintID = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    allergy = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    emailID = db.Column(db.String(100), nullable=False)
    pillName = db.Column(db.String(100), nullable=False) 
    registerDate = db.Column(db.DateTime, default = datetime.now())

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = int(request.form.get('age'))
        pillName = request.form.get('pillname')
        allergy = request.form.get('side-effect')
        description = request.form.get('description')
        entry = Complaints(name=name, emailID=email, allergy=allergy, description=description, age=age, pillName=pillName)
        db.session.add(entry)
        db.session.commit()

    return render_template('home.html', bitch=0)

if __name__ == '__main__':
    app.run(debug=True)


