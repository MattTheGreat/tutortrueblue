import pymysql
import bcrypt
import logging

db = pymysql.connect( host="localhost", user="md2z", passwd="trueblue", db="md2z", port=3306 )

# creates a new user record with a salted, bcrypt hashed password
def createUser(campusId, name, type, password):
	try:
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(password.encode("utf-8"),salt)
		cursor = db.cursor()
		flag = 0 if type=="student" else 1
		cursor.execute("""INSERT INTO USERS (CampusId, Name, UserType, PasswordHash, Salt) VALUES (%s,%s,%s,%s,%s)""",
			(campusId, name, flag, hashed, salt))
		db.commit()
	except Exception:
		logging.exception('')

# returns a tuple with the campusId, name and userType if the credentials are valid
def getUser(campusId, password):
	try:
		cursor = db.cursor()
		cursor.execute("""SELECT Salt, PasswordHash, Name, UserType FROM USERS WHERE CampusId=%s""",
			(campusId,))
		row = cursor.fetchone()
		salt = row[0];
		correct = row[1].encode("utf-8");
		hashed = bcrypt.hashpw(password.encode("utf-8"),salt.encode("utf-8"))
		valid = hashed == correct;
		if valid:
			return (campusId, row[2], row[3])
		else:
			return None
	except Exception:
		logging.exception('')

# returns a tuple with the campusId, name and userType
def getUserById(campusId):
	try:
		cursor = db.cursor()
		cursor.execute("""SELECT Name, UserType FROM USERS WHERE CampusId=%s""",
			(campusId,))
		row = cursor.fetchone()
		if valid:
			return (campusId, row[0], row[1])
		else:
			return None
	except Exception:
		logging.exception('')

# not presently in use - returns a boolean indicating whether the credentials passed are valid
def checkCredentials(campusId, password):
	try:
		cursor = db.cursor()
		cursor.execute("""SELECT Salt, PasswordHash FROM USERS WHERE CampusId=%s""",
			(campusId,))
		row = cursor.fetchone()
		salt = row[0];
		correct = row[1].encode("utf-8");
		hashed = bcrypt.hashpw(password.encode("utf-8"),salt.encode("utf-8"))
		valid = hashed == correct;
		return valid
	except Exception:
		logging.exception('')
