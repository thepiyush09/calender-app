from flask import Flask
from flask_cors import CORS
from models import db
from routes.company_routes import company_bp

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register routes
app.register_blueprint(company_bp, url_prefix='/api/companies')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
