from app import db
from models import Company, CommunicationMethod

db.create_all()

# Add default communication methods
default_methods = [
    {"name": "LinkedIn Post", "description": "Post on LinkedIn", "sequence": 1, "mandatory": True},
    {"name": "LinkedIn Message", "description": "Send LinkedIn message", "sequence": 2, "mandatory": True},
    {"name": "Email", "description": "Send an email", "sequence": 3, "mandatory": True},
    {"name": "Phone Call", "description": "Call the company", "sequence": 4, "mandatory": True},
    {"name": "Other", "description": "Other communication", "sequence": 5, "mandatory": False}
]

for method in default_methods:
    m = CommunicationMethod(**method)
    db.session.add(m)

db.session.commit()
