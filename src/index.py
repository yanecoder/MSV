from flask import Blueprint, render_template, request
from .models import Row
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")