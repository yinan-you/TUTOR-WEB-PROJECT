from flask import Blueprint, render_template, request, flash

eoi = Blueprint('eoi', __name__)


@eoi.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
         
        if len(email) < 4:
            flash('Email must be at least 4 characters long.', category='error')
        elif len(firstname) < 2:
            flash('First name must be at least 2 characters long.', category='error')
        else:
            # Add user to database logic here
            flash('Successfully signed up!', category='success') 
    return render_template("sign_up.html")