from flask import Blueprint, request, jsonify
from models import db, Company

company_bp = Blueprint('company', __name__)

@company_bp.route('/', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'location': c.location,
        'linkedin': c.linkedin,
        'emails': c.emails,
        'phone_numbers': c.phone_numbers,
        'comments': c.comments,
        'communication_periodicity': c.communication_periodicity
    } for c in companies])

@company_bp.route('/', methods=['POST'])
def add_company():
    data = request.json
    company = Company(
        name=data['name'],
        location=data['location'],
        linkedin=data['linkedin'],
        emails=data['emails'],
        phone_numbers=data['phone_numbers'],
        comments=data['comments'],
        communication_periodicity=data['communication_periodicity']
    )
    db.session.add(company)
    db.session.commit()
    return jsonify({'message': 'Company added successfully!'}), 201
