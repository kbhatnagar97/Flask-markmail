from flask import request
from app import app, db
from app.models import User, Template
    # Student, Adress, ContactInfo, Page, Tag, Person

@app.route('/user', methods=['PUT','POST','GET','DELETE'])

def http_method():
    username = request.json.get('username')
    email = request.json.get('email')
    if request.method == 'PUT':
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



@app.route('/template', methods=['PUT','POST','GET','DELETE'])

def template():
    title = request.json.get('title')
    para1 = request.json.get('para1')
    para2 = request.json.get('para2')
    para3 = request.json.get('para3')
    if request.method == 'PUT':
        new_title = request.json.get('title')
        new_para1 = request.json.get('para1')
        new_para2 = request.json.get('para2')
        new_para3 = request.json.get('para3')
        admin = Template.query.filter_by(Title=title, para1=para1, para2=para2, para3=para3)
        admin.title = new_title
        admin.para1 = new_para1
        admin.para2 = new_para2
        admin.para3 = new_para3
        db.session.commit()
        return 'updated template'

    elif request.method == 'GET':
        return "<h1><center>{}</center></h1> \
               <p>{}</p> \
               <p>{}</p> \
               <p>{}</p>".format(title , para1 , para2, para3)

    elif request.method == 'DELETE':
        template=Template.query.filter_by(Title=title, para1=para1, para2=para2, para3=para3)
        db.session.delete(template.first())
        db.session.commit()
        return 'successful deletion of template'

    elif request.method == 'POST':
        template = Template(Title=title, para1=para1, para2=para2, para3=para3)
        db.session.add(template)
        db.session.commit()
        return 'Created template'
