from app import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     __tablename__ = 'Customer'
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    gender = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True)
    age = db.Column(db.String(120), index=True)
    address = db.Column(db.String(120), index=True)
    state = db.Column(db.String(120), index=True)
    zipcode = db.Column(db.String(120), index=True)
    phoneNumber = db.Column(db.String(120), index=True)
    registerationDate = db.Column(db.String(120), index=True)
    __tablename__ = 'Customer'

    def __repr__(self):
        return '<User {}>'.format(self.first_name)

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(64), nullable=True, unique=True)
    para1 = db.Column(db.String(120), nullable=True)
    para2 = db.Column(db.String(128))
    para3 = db.Column(db.String(128))
    __tablename__ = 'Template'

    def __repr__(self):
        return '<Template {}>'.format(self.Title)



