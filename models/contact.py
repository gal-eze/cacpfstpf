from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(500))
    response = db.Column(db.String(500))

    def __init__(self, fullname, email, message, response):
        self.fullname = fullname
        self.email = email
        self.message = message
        self.response = response