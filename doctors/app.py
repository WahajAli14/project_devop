from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://localhost:27017/doctors')

collections= client['doctor']
doctors = [
  { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
  { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():

  return jsonify(list(doctors.find({},{"_id":0})))

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
  id = int(id) - 1
  doctor= list(doctors.find_one({'id':id}, {"_id":0}))
  if doctor:
    return jsonify(doctor)
  else:
    return jsonify({"errror message": "doctor not found"
    }),404
  # return jsonify({"id": doctors[id]['id'], "firstName": doctors[id]['firstName'], "lastName": doctors[id]['lastName'], "speciality": doctors[id]['speciality']})

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)