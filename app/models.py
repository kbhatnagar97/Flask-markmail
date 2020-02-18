from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    # __tablename__ = 'CustomerUser'

    def __repr__(self):
        return '<User {}>'.format(self.username)

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


