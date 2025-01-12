from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

join_front_page = Blueprint('join_front_page', __name__)


@join_front_page.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email1 = request.form.get('email1')
        print("THIS IS THE EMAIL SUBMITTED")
        print(email1)
        if len(email1) < 4:
            flash('Email must be at least 4 characters long.', category='error')
        else:
            # Add user to database logic here
            new_user = User(email=email1, first_name="placeholder")
            db.session.add(new_user)
            db.session.commit()
            print("user added to database")
            flash('Account created!', category='success')
            flash('Successfully signed up!', category='success') 
            return redirect(url_for('views.home'))
    return render_template("home.html")