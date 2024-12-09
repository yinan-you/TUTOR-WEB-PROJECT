from flask import Blueprint, render_template

eoi = Blueprint('eoi', __name__)


@eoi.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")