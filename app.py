from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #usado por flash

#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:admin@localhost/peliflixDB'
app.config["SQLALCHEMY_DATABASE_URI"] =  DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(contacts)


