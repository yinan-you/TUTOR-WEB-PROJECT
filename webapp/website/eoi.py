from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

eoi = Blueprint('eoi', __name__)


@eoi.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
         
        if len(email) < 4:
            flash('Email must be at least 4 characters long.', category='error')
        elif len(first_name) < 2:
            flash('First name must be at least 2 characters long.', category='error')
        else:
            # Add user to database logic here
            new_user = User(email=email, first_name=first_name)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            flash('Successfully signed up!', category='success') 
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")