from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

test_font = Blueprint('test_font', __name__)

@test_font.route('/test-font')
def test_font():
    from flask import send_file
    return send_file('static/fonts/Rubik-Medium.ttf')