from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    __tablename__ = 'Customer'

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(64), nullable=True, unique=True)
    para1 = db.Column(db.String(120), nullable=True)
    para2 = db.Column(db.String(128))
    para3 = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    __tablename__ = 'Template'

    def __repr__(self):
        return '<Template {}>'.format(self.title)


    # #one to many
    # class Person(db.Model):
    #     id = db.Column(db.Integer, primary_key= True)
    #     name = db.Column(db.string(50), nullable=False)
    #     addresses = db.relationships('Adress',backref='person', lazy=True)
    #
    # class Address(db.Model):
    #     id = db.Column(db.Integer,primary_key = True)
    #     email = db.Column(db.String(120), nullable= False)
    #     person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False )


