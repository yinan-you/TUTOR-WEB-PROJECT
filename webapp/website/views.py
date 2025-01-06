from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') # whenever we go to / route, we will run this. This is the homepage
def home():
    return render_template("home2.html")