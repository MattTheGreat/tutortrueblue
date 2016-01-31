from flask import Flask, request, jsonify, abort, Blueprint, render_template
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)
import logging
import json

from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

import db.user

registration = Blueprint( "registration", __name__ )

@registration.route("/register", methods=['POST'])
def create_user():
	print( request.json )
	db.user.createUser( request.json[ "campusId" ], request.json[ "name" ], request.json[ "type" ], request.json[ "password" ] )
	return "ok"