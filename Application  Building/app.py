import re
import os
from flask import Flask,request,render_template,redirect,url_for,flash,session
from flask_session import Session
from cloudant.client import Cloudant
from predicter import predicter

username="1f3effb3-8b3a-412f-b91c-7ef39a78789b-bluemix"
api_key= "PuMaRnoaIqUpFtJF0vEjQBFUzNSXLDbv7aYHGfvpP7qX"
client = Cloudant.iam(username,api_key,connect=True)
my_database = client.create_database("database-vijo")

app=Flask(__name__,static_folder="static",template_folder='templates')
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = 1800
app.config.update(SECRET_KEY=os.urandom(24))
app.config.from_object(__name__)
Session(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')


#registration page
@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/afterrreg/', methods=['POST'])
def afterreg():
    x = [x for x in request.form.values()]
    print(x)
    data = {
        '_id': x[1],
        'name' : x[0],
        'psw' : x[2]
    }
    print(data)

    query = {'_id': {'$eq': data['_id']}}
    docs = my_database.get_query_result(query)
    print(docs)

    print(len(docs.all()))

    if(len(docs.all())==0):
        url = my_database.create_document(data)
        print("Registration Successfull!!!")
        return render_template('register.html',pred="Registration Successfull!!!")
    else:
        print("helo")
        return render_template('register.html',pred="User already Registerd")


#login page
@app.route('/login/')
def login():
    return render_template('login.html')
@app.route('/afterlogin/', methods=['POST'])    
def afterlogin():
    user = request.form['_id']
    passw = request.form['psw']

    query = {'_id':{'$eq': user}}
    
    docs=my_database.get_query_result(query)
    print(docs)

    print(len(docs.all()))

    if(len(docs.all())==0):
        print("no user")
        return render_template('login.html',pred="The username is not found")
    else:
        print(docs[0][0]['_id'])
        if((user==docs[0][0]['_id']) and (passw==docs[0][0]['psw'])):
            return redirect(url_for('prediction'))
        else:
            print("no user1")
            return render_template('login.html',pred="Invalid password or username")
#log out
@app.route('/logout/')
def logout():
    return render_template('index.html')

@app.route('/prediction/')
def prediction():
    return render_template('prediction.html')

@app.route('/result/', methods=['POST'])
def result():
    f=request.files['image']
    basepath=os.path.dirname(__file__)
    filepath=os.path.join(basepath,f.filename)
    f.save(filepath)
    res=predicter.predict(filepath)
    return render_template('prediction.html',prediction=res)





if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)