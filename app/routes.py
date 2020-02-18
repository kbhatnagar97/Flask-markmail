from flask import request
from app import app, db
from app.models import User, Template
    # Student, Adress, ContactInfo, Page, Tag, Person

@app.route('/user', methods=['PUT','POST','GET','DELETE'])

def http_method():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    gender = request.json.get('gender')
    email = request.json.get('email')
    age = request.json.get('age')
    address = request.json.get('address')
    state = request.json.get('state')
    zipcode = request.json.get('zipcode')
    phoneNumber = request.json.get('phoneNumber')
    registrationDate = request.json.get('registrationDate')
    if request.method == 'PUT':
        # new_first_name = request.json.get('first_name')
        # new_last_name = request.json.get('last_name')
        # new_gender = request.json.get('gender')
        # new_email = request.json.get('email')
        # new_age = request.json.get('age')
        # new_address= request.json.get('address')
        # new_state = request.json.get('state')
        # new_zipcode = request.json.get('zipcode')
        # new_phoneNumber = request.json.get('phoneNumber')
        # new_registrationDate = request.json.get('registrationDate')
        admin = User.query.filter_by(first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registrationDate=registrationDate).first()
        admin.email = email
        admin.first_name = first_name
        admin.last_name = last_name
        admin.gender = gender
        admin.age = age
        admin.address = address
        admin.state = state
        admin.zipcode = zipcode
        admin.phoneNumber = phoneNumber
        admin.registrationDate = registrationDate
        db.session.commit()
        return 'updated email id is '+ new_email

    elif request.method == 'GET':
        s={}
        user = User.query.all()
        print(user)
        i=0
        for use in user:
            s[i]={
                "first_name" : use.first_name,
                "last_name" : use.last_name,
                "gender" : use.gender,
                "email" : use.email,
                "age" : use.age,
                "address" : use.address,
                "state" : use.state,
                "zipcode" : use.zipcode,
                "phoneNumber" : use.phoneNumber,
                "registrationDate" : use.registrationDate
            }
            i+=1
        return s

    elif request.method == 'DELETE':
        User.query.filter_by(first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registrationDate=registrationDate).delete()
        db.session.commit()
        return 'success deletion with username'

    elif request.method == 'POST':
        user= User(first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registrationDate=registrationDate)
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
