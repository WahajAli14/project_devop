import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
CORS(app)
mongo_uri = os.environ.get('MONGO_URI')
client = MongoClient(mongo_uri)
db= client['doctor']
collections= db['doctor']
# doctors = [
#   { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
#   { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
# ]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
  doctor=list(collections.find({},{'_id': 0}))
  return jsonify(doctor)

# @app.route('/doctor/<id>', methods=["GET"])
# def getDoctor(id):
#   id = int(id) - 1
#   doctor= collections.find_one({'id':id}, {"_id":0})
#   if doctor:
#     return jsonify(doctor)
#   else:
#     return jsonify({"errror message": "doctor not found"
#     }),404
#   # return jsonify({"id": doctors[id]['id'], "firstName": doctors[id]['firstName'], "lastName": doctors[id]['lastName'], "speciality": doctors[id]['speciality']})
@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
  doctor = collections.find_one({'id': id}, {'_id': 0})  # Find appointment by ID
  if doctor:
      return jsonify(doctor)
  else:
      return jsonify({"message": "Doctor not found"}), 404

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)