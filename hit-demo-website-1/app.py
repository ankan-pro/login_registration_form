from flask import Flask,render_template,request
from dbhelper import DB

app = Flask(__name__)
dbo =DB()

logged_in = 0

@app.route('/')
def index():
    global logged_in
    if logged_in == 1:
        return 'Not Allowed'
    return render_template('login_form.html')

@app.route('/register')
def register():
    return render_template('register_form.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    global logged_in
    email = request.form.get('user-ka-email')
    password = request.form.get('user-ka-password')

    data = dbo.search(email,password)

    if len(data) ==0:
        return 'Incorrect email/password'
    else:
        logged_in = 1
        return render_template('profile.html',data=data)

@app.route('/reg_validation',methods=['POST'])
def reg_validation():
    # receive data from html
    name = request.form.get('user-ka-name')
    email = request.form.get('user-ka-email')
    password = request.form.get('user-ka-password')
    gender = request.form.get('user-ka-gender')
    city = request.form.get('user-ka-city')

    result = dbo.insert(name,email,password,gender,city)

    if result == 1:
        return 'Reg succesful'
    else:
        return 'Reg failed'

@app.route('/logout')
def logout():
    global logged_in
    logged_in = 0
    return render_template('login_form.html')

app.run(debug=True)