from flask import request
from app import app, db
from app.models import User, Template
from flask_mail import Mail
from flask_mail import Message
from io import TextIOWrapper
from sqlalchemy.exc import IntegrityError
import csv
    # Student, Adress, ContactInfo, Page, Tag, Person

app.config['MAIL_SERVER']='localhost' #running on this
app.config['MAIL_PORT'] = 2525 #port number
mail = Mail(app)

class customException(Exception):
    status_code = 400 #Bad Request response status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error

@app.errorhandler(customException)
def handel_error(error):
    return 'CUSTOM EXCEPTION HANDLED' #Exception handling message

@app.route('/user', methods=['PUT','POST','GET','DELETE'])
def customer():
    csv_file = request.files['files'] #gets input in bytes
    csv_file = TextIOWrapper(csv_file, encoding='utf-8') #converts to string
    csv_dict = csv.DictReader(csv_file) #converts bytes into ordered dictionary
    for row in csv_dict: #row is the iterrator
        first_name = row['first_name']
        last_name = row['last_name']
        gender = row['gender']
        email = row['email']
        age = row['age']
        address = row['address']
        state = row['state']
        zipcode = row['zipcode']
        phoneNumber = row['phoneNumber']
        registerationDate = row['registerationDate']
        #put method
        if request.method == 'PUT':
            admin = User.query.filter_by(first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registerationDate=registerationDate).first()
            admin.email = email #Assigning new email to variable admin
            admin.first_name = first_name #Assigning new first_name to variable admin
            admin.last_name = last_name #Assigning new second_name to variable admin
            admin.gender = gender #Assigning new gender to variable admin
            admin.age = age #Assigning new age to variable admin
            admin.address = address #Assigning new address to variable admin
            admin.state = state #Assigning new state to variable admin
            admin.zipcode = zipcode #Assigning new zipcode to variable admin
            admin.phoneNumber = phoneNumber #Assigning new phonenumber to variable admin
            admin.registrationDate = registerationDate #Assigning new registerationDate to variable admin
            db.session.commit()
            return 'updated all fields'
        #get Method
        elif request.method == 'GET':
            s={}
            user = User.query.all()
            i=0 #defining iterating variable
            for use in user: #iterating through all the atttributes of customer
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
                    "registerationDate" : use.registerationDate
                }
                i+=1
                return s
        #Delete Method
        elif request.method == 'DELETE':
            User.query.filter_by(first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registerationDate=registerationDate).delete()
            db.session.commit()
            return 'success deletion'
        #Post Method
        elif request.method == 'POST':
            user= User(first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registerationDate=registerationDate)
            try:
                db.session.add(user)
                db.session.commit()
            except IntegrityError:
                raise customException
        return 'Created new user'



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
    #Get Method
    elif request.method == 'GET':
        return "<h1><center>{}</center></h1> \
               <p>{}</p> \
               <p>{}</p> \
               <p>{}</p>".format(title , para1 , para2, para3)
    #Delete Method
    elif request.method == 'DELETE':
        template=Template.query.filter_by(Title=title, para1=para1, para2=para2, para3=para3)
        db.session.delete(template.first())
        db.session.commit()
        return 'successful deletion of template'
    #Post Method
    elif request.method == 'POST':
        template = Template(Title=title, para1=para1, para2=para2, para3=para3)
        db.session.add(template)
        db.session.commit()
        return 'Created template'

@app.route("/mail")
def send_mail():
   msg = Message(sender = 'test1@gmail.com', recipients = ['test2@gmail.com'])
   msg.body = "This is the email body"
   msg.subject = "Test Email"
   mail.send(msg)
   return "Email Sent"

