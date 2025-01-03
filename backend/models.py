from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    emails = db.Column(db.Text)  # Store as JSON string if multiple
    phone_numbers = db.Column(db.Text)
    comments = db.Column(db.Text)
    communication_periodicity = db.Column(db.String(50))
