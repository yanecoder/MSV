from flask import Blueprint, render_template, request
from .models import Row
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/send', methods=["POST"])
def send_msg():
    data = request.get_json()
    msg = data.get("text")
    row = Row(text=msg)
    db.session.add(row)
    db.session.commit()
    return render_template("send.html")

@main.route("/get", methods=["GET"])
def load_msg():
    id = request.args.get("id")
    msg = db.session.query(Row).filter(Row.id == id).first()
    return render_template("get.html", id=id, message=msg.text)