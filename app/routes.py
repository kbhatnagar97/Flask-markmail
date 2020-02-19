import csv
from flask import request
from app import app, db
from app.models import User, Template
from flask_mail import Mail
from flask_mail import Message
from io import TextIOWrapper
from sqlalchemy.exc import IntegrityError
# Student, Adress, ContactInfo, Page, Tag, Person

app.config['MAIL_SERVER']='localhost' #running on this
app.config['MAIL_PORT'] = 2525 #port number
mail = Mail(app)
#
class customException(Exception):
    status_code = 400 #Bad Request response status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error

@app.errorhandler(customException)
def handel_error(error):
    return 'CUSTOM EXCEPTION HANDLED' #Exception handling message

@app.route('/user', methods=['PUT','POST','GET','DELETE'])
def http_method():
    first_name = request.json.get('first_name')
    email = request.json.get('email')
    if request.method == 'PUT':
        first_name = request.json.get('first_name')
        new_email = request.json.get('email')
        print(first_name)
        admin = User.query.filter_by(first_name=first_name).first()
        # print(admin)
        admin.email = new_email
        db.session.commit()
        return 'updated email id is '+ new_email

    elif request.method == 'GET':
        user = User.query.filter_by(first_name=first_name,email=email)
        user = user.first()
        s={}
        user = User.query.all()
        print(user)
        i=0
        for use in user:
            s[i]={
                "first_name":use.first_name,
                "email":use.email
            }
            i+=1
        return s

    elif request.method == 'DELETE':
        User.query.filter_by(first_name=first_name,email=email).delete()
        db.session.commit()
        return 'success deletion with first_name{} '.format(first_name)

    elif request.method == 'POST':
        user= User(first_name=first_name,email=email)
        db.session.add(user)
        db.session.commit()
        return 'Successfully added {}\'s data'.format(first_name)


@app.route('/user/CSV', methods=[   'POST'])
def customer():
    csv_file = request.files['files'] #gets input in bytes
    csv_file = TextIOWrapper(csv_file, encoding='utf-8') #converts to string
    csv_dict = csv.DictReader(csv_file) #converts bytes into ordered dictionary
    for row in csv_dict: #row is the iterrator
        id = row['id']
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
        # print(row)
        user= User(id=id,first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registerationDate=registerationDate)
        try:
            print(user)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            raise customException
    return 'Created new user'
#
#
#
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

