from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    return render_template('index.html')

@contacts.route("/new", methods=['POST'])
def add():
    fullname = request.form['contact-name']
    email = request.form['contact-email']
    message = request.form['contact-message']
    response = ''    
    new_contact = Contact(fullname, email, message, response)
    db.session.add(new_contact)
    db.session.commit()

    flash("Hemos recibido su mensaje")
    return redirect('/')

@contacts.route("/manage-contacts")
def manage():
    contacts = Contact.query.all();
    return render_template('manage-contacts.html', contacts=contacts)

@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts.manage'))

@contacts.route("/update/<id>", methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        contact = Contact.query.get(id)
        responseText = request.form['contact-response']
        contact.response = responseText

        db.session.commit()
        return redirect(url_for('contacts.manage'))
    
    return render_template('update-contact.html', contact=contact)
