from flask import Blueprint, render_template, request
from db import db
from models import Row

get = Blueprint('get', __name__)

@get.route("/get", methods=["GET"])
def load_msg():
    id = request.args.get("id")
    msg = db.session.query(Row).filter(Row.id == id).first()
    return render_template("get.html", id=id, message=msg.text)
