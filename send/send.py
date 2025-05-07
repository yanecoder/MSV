from flask import Blueprint, render_template, request
from models import Row
from db import db

send = Blueprint('send', __name__)

@send.route('/send', methods=["POST"])
def send_msg():
    data = request.get_json()
    msg = data.get("text")
    row = Row(text=msg)
    db.session.add(row)
    db.session.commit()
    return render_template("send.html")

    
    