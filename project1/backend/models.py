from flask_sqlalchemy import SQLAlchemy
from datetime import date 
db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer , primary_key = True )
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100) , nullable = False , unique=True)
    phone_number = db.Column(db.String(13) , nullable = False , unique=True)
    national_identity_number = db.Column(db.String(9) , nullable =False, unique=True)

    projects = db.relationship('Project',backref='client',lazy=True)
    financials = db.relationship('Financial',backref='client',lazy=True)

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100) , nullable = False)
    email = db.Column(db.String(100) , nullable = False,unique=True)
    phone_number = db.Column(db.String(13) , nullable = False , unique=True) 
    status = db.Column(db.Enum('Active','Inactive','Pending','Suspended') , nullable=False , default='Active')
    remaining_amount = db.Column(db.Float , nullable=False , default=0.00)

    equipment = db.relationship('Equipment' ,backref='supplier',lazy=True)
    materials = db.relationship('Material' , backref='supplier' ,lazy=True)
    financials = db.relationship('Financial',backref ='supplier',lazy=True)
    
class Personnel(db.Model):
    __tablename__ = 'personnel'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    national_identity_number = db.Column(db.String(9),nullable = False,unique=True) 
    personnel_type = db.Column (db.Enum('Professional','Skilled','Unskilled') , nullable = False )
    wages = db.Column(db.Float,nullable = False)
    role = db.Column (db.Enum('Project Manager','Architect','Structural Engineer','Quantity Surveyor','Mechanical Engineer','Electrical Engineer','Site Supervisor','Mason','Plumber','Electrician','Carpenter','Welder', 'Painter','Roofer','Laborer') , nullable = False)
    code = db.Column(db.String(6),nullable= False,unique=True)

    projects = db.relationship('Project', backref='personnel', lazy=True)
    certifications = db.relationship('Certification', backref='personnel', lazy=True)
    financials = db.relationship('Financial',backref='personnel',lazy=True)


class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer , db.ForeignKey('client.id') , nullable = False)
    personnel_id = db.Column(db.Integer , db.ForeignKey('personnel.id') , nullable = False)
    name = db.Column(db.String(50),nullable = False , unique=True)
    budget = db.Column(db.Float, nullable = False)
    status = db.Column(db.Enum('Pending','In progress','Completed','On hold','Cancelled') , nullable = False, default='Pending')
    start_date = db.Column(db.Date, nullable =False)
    end_date = db.Column(db.Date, nullable = False)

    financials = db.relationship('Financial', backref = 'project' ,lazy=True)

class Certification(db.Model):
    __tablename__ = 'certification'   
    id = db.Column(db.Integer , primary_key = True )
    personnel_id  = db.Column(db.Integer ,db.ForeignKey('personnel.id') ,nullable=False)
    number = db.Column(db.String(50) , nullable = False , unique=True)
    name = db.Column(db.String(50) , nullable = False)
    expiry_date = db.Column(db.Date , nullable = False)
    status = db.Column(db.Enum('Active','Expired','Revoked','Pending'),default='Active' , nullable = False)


class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer , primary_key = True)
    supplier_id = db.Column(db.Integer , db.ForeignKey('supplier.id') , nullable=False)
    name = db.Column(db.String(50) , nullable=False)
    quantity = db.Column(db.Integer , nullable=False)
    code = db.Column(db.String(50) , nullable =False , unique=True)
    date_bought = db.Column(db.Date , nullable =False)
    status = db.Column(db.Enum('Active','In Repair','Retired'),default='Active',nullable=False)
    
class Material(db.Model):
    __tablename__='material'
    id = db.Column(db.Integer , primary_key=True)
    supplier_id = db.Column(db.Integer,db.ForeignKey('supplier.id'),nullable=False)
    name = db.Column(db.String(50) , nullable=False)
    quantity = db.Column(db.Integer , nullable = False)
    price = db.Column(db.Float , nullable = False)
    status = db.Column(db.Enum('Available','Not Available') ,default ='Available',nullable=False)

class Financial(db.Model):
    __tablename__ = 'financial'
    id = db.Column(db.Integer , primary_key = True)
    personnel_id = db.Column(db.Integer , db.ForeignKey('personnel.id') , nullable=True)
    project_id = db.Column(db.Integer , db.ForeignKey('project.id') , nullable=True)
    client_id = db.Column(db.Integer , db.ForeignKey('client.id') , nullable=True)
    supplier_id = db.Column(db.Integer , db.ForeignKey('supplier.id'),nullable=True)
    financial_type = db.Column(db.Enum('Personnel Wages','Supplier Payments','Client Payments'),nullable=False)
    amount = db.Column(db.Float,nullable=False)
    description = db.Column(db.Text, nullable=True)
    transaction_date = db.Column(db.Date , nullable=False ,default=(date.today))