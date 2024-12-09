from flask import Blueprint

eoi = Blueprint('eoi', __name__)


@eoi.route('/sign-up')
def sign_up():
    return "<p>Sign Up<p>"