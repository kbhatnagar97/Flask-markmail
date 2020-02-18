from flask import request
from app import app, db
from app.models import User
    # Student, Adress, ContactInfo, Page, Tag, Person

@app.route('/user', methods=['PUT','POST','GET','DELETE'])

def http_method():
    username = request.json.get('username')
    email = request.json.get('email')
    if request.method == 'PUT':
        username = request.json.get('username')
        new_email = request.json.get('email')
        admin = User.query.filter_by(username=username).first()
        admin.email = new_email
        db.session.commit()
        return 'updated email id is '+ new_email

    elif request.method == 'GET':
        s={}
        user = User.query.all()
        print(user)
        i=0
        for use in user:
            s[i]={
                username:use.username,
                email:use.email
            }
            i+=1
        return s

    elif request.method == 'DELETE':
        User.query.filter_by(username=username,email=email).delete()
        db.session.commit()
        return 'success deletion with username{}'.format(username)

    elif request.method == 'POST':
        user= User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        return 'Created new user with email {}'.format(email)





@app.route('/')
def hello():
    return '<h1><center><b>Thank you</b></center></h1>' \
           '<p>Hi</p>' \
           '<p>Thank you for being part of our family. Hope you will have a <br>nice experience with us.</p>' \
           '<p>For any queries visit our website.</p>' \
           'Thank you<br>HU2k20.com'
