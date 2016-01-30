from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
import logging
import json
app = Flask(__name__)
students = []
def findByName( name ):
	for student in students:
		if student[ "name" ] == name : yield student
@app.route("/student", methods=['POST'])
def create_student():
	print( request.json )
	students.append( request.json )
	return "ok"
@app.route("/student", methods=['GET'])
def list_students():
	return json.dumps( students )
@app.route("/student/<name>", methods=['GET'])
def get_student( name ):
	try:
		student = [student for student in students if student[ "name" ] == name]
		if len(student) == 0:
			return ("No student found", 404)
		return json.dumps( student[0] )
	except:
		logging.exception('')
@app.route("/student/<name>", methods=['DELETE'])
def delete_student( name ):
	try:
		student = [student for student in students if student[ "name" ] == name]
		if len(student) == 0:
			return ("Can't remove student that didn't exist", 404)
		students.remove( student )
		return "Student removed successfully"
	except:
		logging.exception('')
if __name__ == "__main__":
    app.run()
