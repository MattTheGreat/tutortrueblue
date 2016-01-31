from flask.ext.login import UserMixin 

class User(UserMixin):
    def __init__(self, name, id, type="student"):
        self.id = id
        self.name = name
        self.type = type

    def get_id(self):
        return self.id

    @property
    def is_student(self):
        return self.type == "student"

    @property
    def is_tutor(self):
    	return self.type == "tutor"

    def get_auth_token(self):
        return make_secure_token(self.name, key='deterministic')
