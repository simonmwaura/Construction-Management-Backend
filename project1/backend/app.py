from flask import Flask,request,jsonify
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///HousingDevelpment.db"

from models import db,Client,Supplier,Personnel,Project,Certification,Equipment,Material,Financial
migrate = Migrate(app,db)
db.init_app(app)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)