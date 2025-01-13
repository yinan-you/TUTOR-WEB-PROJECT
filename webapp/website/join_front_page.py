from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
import re

join_front_page = Blueprint('join_front_page', __name__)


@join_front_page.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email1 = request.form.get('email1')  # retrieve the email from html
        print("THIS IS THE EMAIL SUBMITTED: ", email1)  # debugging

        existing_user = User.query.filter_by(email=email1).first()
        # Check if email is valid format using regex (optional if HTML5 already validates)
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email1):
            flash('Invalid email format.', category='error')

        # Check if the email already exists in the database
        
        elif existing_user:
            flash('Email already registered.', category='error')
        
        # If email is unique, add new user to the database
        else: 
            try:
                new_user = User(email=email1, first_name="placeholder")
                db.session.add(new_user)
                db.session.commit()
                flash('Successfully signed up!', category='success')
            except Exception as e:
                db.session.rollback()  # Ensure the transaction is rolled back in case of error
                flash('An error occurred. Please try again later.', category='error')
                print(f"Error: {e}")
    return redirect(url_for('join_front_page.sign_up'))

