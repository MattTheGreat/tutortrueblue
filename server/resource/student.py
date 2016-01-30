from flask import Flask, request, jsonify, abort, Blueprint, render_template
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)
import logging
import json

from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

student = Blueprint( "student", __name__ )

students = []

def findByName( name ):
	for student in students:
		if student[ "name" ] == name : yield student

@student.route("/student", methods=['POST'])
def create_student():
	print( request.json )
	students.append( request.json )
	return "ok"

@student.route("/student", methods=['GET'])
@login_required
def list_students():
	return json.dumps( students )

@student.route("/student/<name>", methods=['GET'])
@login_required
def get_student( name ):
	try:
		student = [student for student in students if student[ "name" ] == name]
		if len(student) == 0:
			return ("No student found", 404)
		return json.dumps( student[0] )
	except:
		logging.exception('')

@student.route("/student/<name>", methods=['DELETE'])
@login_required
def delete_student( name ):
	try:
		student = [student for student in students if student[ "name" ] == name]
		if len(student) == 0:
			return ("Can't remove student that didn't exist", 404)
		students.remove( student )
		return "Student removed successfully"
	except:
		logging.exception('')

