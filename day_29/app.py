import os

from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime

from insert_data import students_collection

app = Flask(__name__)

# MongoDB URI and client setup
MONGODB_URI = 'mongodb+srv://kishanvaghasiya:kishan.123@30daysofpython.r5ful.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']  # Accessing the database
@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    try:
        students = list(db.students.find({}, {'_id': 0}))  # Fetch all students, exclude '_id'
        return Response(dumps(students), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    try:
        student = db.students.find_one({'_id': ObjectId(id)})  # Find one student by id
        if student:
            return Response(dumps(student), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Student not found'}), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), mimetype='application/json')


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    try:
        data = request.get_json()  # Get JSON data from request
        name = data.get('name')
        country = data.get('country')
        city = data.get('city')
        skills = data.get('skills', [])
        bio = data.get('bio')
        birthyear = data.get('birthyear')
        created_at = datetime.now()

        student = {
            'name': name,
            'country': country,
            'city': city,
            'birthyear': birthyear,
            'skills': skills,
            'bio': bio,
            'created_at': created_at
        }

        db.students.insert_one(student)
        return Response(json.dumps({'message': 'Student created successfully'}), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.get_json()
        result = db.students.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.matched_count:
            return Response(json.dumps({'message': 'Student updated successfully'}), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Student not found'}), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    try:
        result = students_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count:
            return Response(json.dumps({'message': 'Student deleted successfully'}), mimetype='application/json')
        else:
            return Response(json.dumps({'error': 'Student not found'}), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
