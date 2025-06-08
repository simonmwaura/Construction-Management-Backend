from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer , primary_key = True )
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100) , nullable = False)
    phone_number = db.Column(db.String(13) , nullable = False)
    national_identity_number = db.Column(db.String(9) , nullable =False)


class Suppliers(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100) , nullable = False)
    email = db.Column(db.String(100) , nullable = False)
    phone_number = db.Column(db.String(13) , nullable = False)
    status = db.Column(db.Enum('Active','Inactive','Pending','Suspended') , nullable=False )
    remaining_amount = db.Column(db.Float , nullable=False)
    
class Personnel(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    national_identity_number = db.Column(db.String(9),nullable = False) 
    personnel_type = db.Column (db.Enum('Professional','Skilled','Unskilled') , nullable= False )
    wages = db.Column(db.Float , nullable = False)
    role = db.Column (db.Enum('Project Manager','Architect','Structural Engineer','Quantity Surveyor','Mechanical Engineer','Electrical Engineer','Site Supervisor','Mason','Plumber','Electrician','Carpenter','Welder', 'Painter','Roofer','Laborer') , nullable = False)
    code = db.Column(db.String(6),nullable= False)
class Projects(db.Model):
    pass
class Certification(db.Model):
    pass
class Equipment(db.Model):
    pass
class Materials(db.Model):
    pass
class Financials(db.Model):
    pass