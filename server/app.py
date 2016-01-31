# caution: this module was written by a Python novice learning on the fly
# you should not assume this is "good" or idiomatic Python.
# Hackathons are fun.

from flask import Flask, Blueprint, render_template, abort, request, jsonify
from flask.ext.login import LoginManager, login_required
import logging
import json
from user import User
import base64
import db.user

app = Flask(__name__)

# setting up auth ... this should be interesting
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.request_loader
def load_user_from_request(request):
	api_key = request.headers.get('Authorization')
	if api_key:
		api_key = api_key.replace('Basic ', '', 1)
		try:
			raw = base64.b64decode(api_key)
			parts = raw.decode("utf-8").split( ":" )
			userName = parts[ 0 ]
			password = parts[ 1 ]
			record = db.user.getUser(userName, password)
			if record:
				userType = "tutor" if record[2] else "student"
				return User(record[1], record[0], userType)
		except TypeError:
			logging.exception('')
			pass

	# finally, return if user is unauthorized
	return None

@login_manager.user_loader
def load_user(user_id):
	record = db.user.getUserById(user_id)
	userType = "tutor" if record[2] else "student"
	return User(record[1], record[0], userType)

@app.route('/')
def root():
	return app.send_static_file('index.html')

# load other blueprints into app
from resource.registration import registration
app.register_blueprint(registration)

from resource.student import student
app.register_blueprint(student)

if __name__ == "__main__":
	app.run(host="0.0.0.0")