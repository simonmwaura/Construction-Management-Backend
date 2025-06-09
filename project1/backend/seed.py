from faker import Faker
from models import db,Client,Supplier,Personnel,Project,Certification,Equipment,Material,Financial
from app import app

faker=Faker()

print("<<--START SEEDING-->>")
def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        client1 = Client(name ='Michael',email="Michael23@gmail.com",phone_number='+254712345678',national_identity_number='102030408')
        db.session.add(client1)
        db.session.commit()

seed_data()
print("<<--SEEDING COMPLETED!->>")