import csv
from flask import request
from app import app, db
from app.models import Customer, Template
from flask_mail import Mail
from flask_mail import Message
from io import TextIOWrapper
from sqlalchemy.exc import IntegrityError

app.config['MAIL_SERVER']='localhost' #running on this
app.config['MAIL_PORT'] = 2525 #port number
mail = Mail(app)
#
class customException1(Exception):
    status_code = 400 #Bad Request response status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error

@app.errorhandler(customException1)
def handle_error(error):
    return 'The customer Exists, kindly add a new customer' #Exception handling message

class customException2(Exception):
    status_code = 400 #Bad Request response status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error

@app.errorhandler(customException2)
def handle_error(error):
    return 'The Template exist, kindly add a different template' #Exception handling message

@app.route('/user', methods=['PUT','POST','GET','DELETE']) #importing with JSON
def http_method():
    first_name = request.json.get('first_name')
    email = request.json.get('email')
    if request.method == 'PUT':
        first_name = request.json.get('first_name')
        new_email = request.json.get('email')
        print(first_name)
        admin = Customer.query.filter_by(first_name=first_name).first()
        # print(admin)
        admin.email = new_email
        db.session.commit()
        return 'updated email id is '+ new_email

    elif request.method == 'GET':
        user = Customer.query.filter_by(first_name=first_name,email=email)
        user = user.first()
        s={}
        user = Customer.query.all()
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
        Customer.query.filter_by(first_name=first_name,email=email).delete()
        db.session.commit()
        return 'success deletion with first_name{} '.format(first_name)

    elif request.method == 'POST':
        user= Customer(first_name=first_name,email=email)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            raise customException1
        return 'Successfully added {}\'s data'.format(first_name)

@app.route('/customers', methods=['GET'])
def customer_all():
    users=Customer.query.filter_by().all()
    temp_list=list()
    for user in users:
        temp_list.append(user.first_name+" "+user.last_name+" "+user.email)
    return str(temp_list)

@app.route('/customer/<id>', methods=['GET'])
def customer_search(id):
    users=Customer.query.filter_by(id=id).first()
    return {"first_name":users.first_name,"last_name":users.last_name,"id":users.id,"email":users.email,"gender":users.gender}

@app.route('/user/CSV', methods=['POST'])
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
        user= Customer(id=id,first_name=first_name,last_name=last_name,gender=gender,email=email,age=age,address=address,state=state,zipcode=zipcode,phoneNumber=phoneNumber,registerationDate=registerationDate)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            raise customException1
    return 'Created new user'

@app.route('/template', methods=['PUT','POST','GET','DELETE'])
def template():
    id = request.json.get('id')
    title = request.json.get('title')
    para1 = request.json.get('para1')
    para2 = request.json.get('para2')
    para3 = request.json.get('para3')
    if request.method == 'PUT':
        new_title = request.json.get('title')
        new_para1 = request.json.get('para1')
        new_para2 = request.json.get('para2')
        new_para3 = request.json.get('para3')
        admin = Template.query.filter_by(id=id).first()
        admin.Title = new_title
        admin.para1 = new_para1
        admin.para2 = new_para2
        admin.para3 = new_para3
        db.session.add(admin)
        db.session.commit()
        return 'updated template'
    #Get Method

    elif request.method == 'GET':
         template= Template.query.filter_by(id=id).first()
         return "<h1><center>{}</center></h1> \
               <p>{}</p> \
               <p>{}</p> \
               <p>{}</p>".format(template.Title , template.para1 , template.para2, template.para3)

    #Delete Method
    elif request.method == 'DELETE':
        template=Template.query.filter_by(Title=title, para1=para1, para2=para2, para3=para3)
        db.session.delete(template.first())
        db.session.commit()
        return 'successful deletion of template'
    #Post Method
    elif request.method == 'POST':
        template = Template(Title=title, para1=para1, para2=para2, para3=para3)
        try:
            db.session.add(template)
            db.session.commit()
        except IntegrityError:
            raise customException2
        return 'Created template'


@app.route("/mail",methods=['POST'])
def send_mail():
    if request.method == 'POST' :
       for email in request.json["recipients"]:
           msg = Message(sender = 'test1@gmail.com', recipients = [email])
           msg.html =  "<h1>\
	                        <center><b>Thank you</b></center>\
                        </h1>\
                        <p>Hi</p>\
                        <p>Thank you for being part of our family. Hope you will have a \
                       <br> nice experience with us.</p>\
	                    <p>For any queries visit our website<br> \
                       Thank you<br>HU2k20.com</p>"
           msg.subject = "Test Email"
           mail.send(msg)
    return "Email Sent"

@app.route("/dmail",methods=['POST'])
def send_dmail():
    if request.method == 'POST' :
       for email in request.json["recipients"]:
           msg = Message(sender = 'test1@gmail.com', recipients = [email])
           temp_user=Customer.query.filter_by(email=email).first()
           print(temp_user)
           print("AFDRgeragaskfgseufygweliyEGIUAYGFLEUGY")
           msg.html = "<h1>\
	                        <center><b>New Years Sales</b></center>\
                        </h1>\
                        <p>Hi {} {},<br><br>Wish you a very happy new year. As you have done shopping worth 7000<br> \
                      this year, we have surprise for you.\
                      <br><br>\
                      Below is a coupon for  this  new year sale to bring more joy to in the<br> \
                      coming year.	</p> \
                      <br><br>\
                        <p><center>Coupon Code \
                      <br><br>\
                      <h1><b>MMCDD2020<b></h1></center></p>\
                        <p>For any queries visit our website \
                      <br><br> \
                      Thank you<br> \
                      HU2k20.com</p>".format(temp_user.first_name,temp_user.last_name)
           msg.subject = "Test Email"
           mail.send(msg)
    return "Email Sent"

@app.route('/selective', methods=['GET'])
def selective():
    if request.method == 'GET' :
        users=Customer.query.all()
        temp_dict={}
        i=0
        for user in users:
            print(user.first_name)
            temp_dict[i]={"first_name": user.first_name, "last_name": user.last_name, "id": user.id, "email": user.email,"gender": user.gender}
            i+=1
        return  temp_dict


