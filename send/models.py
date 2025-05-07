from db import db

class Row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)