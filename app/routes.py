from app import app

# @app.route('/', methods = ['POST', 'GET', 'DELETE'])
# def http_method():
#     if request.method == 'POST':
#         return request.json.get('name')
#
#     if request.method == 'GET':
#         return 'success getting response'
#
#     if request.method == 'DELETE':
#         return 'success deletion'

@app.route('/')
def hello():
    return '<h1><center><b>Thank you</b></center></h1>' \
           '<p>Hi</p>' \
           '<p>Thank you for being part of our family. Hope you will have a <br>nice experience with us.</p>' \
           '<p>For any queries visit our website.</p>' \
           'Thank you<br>HU2k20.com'
