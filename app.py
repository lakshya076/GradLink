import sys
from flask import Flask, render_template, redirect, request, url_for, flash, session
from pymongo.mongo_client import MongoClient
from pymongo import errors
from utility.encryption import sha256

uri = "mongodb+srv://lakshyasaxena076:IX4voLrdMVuY9ELo@cluster0.sy08f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["gradlink"]
user_col = db["users"]
acad_col = db["acad"]

user_data = {}
acad_data = {}
username = ""

app = Flask(__name__)
app.secret_key = "ok"


@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_retrieval = user_col.find_one({"_id": session['user_id']})
    acad_retrieval = acad_col.find_one({"_id": session['user_id']})
    return render_template("index.html", user_data=user_retrieval, acad_data=acad_retrieval)


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_retrieval = user_col.find_one({"_id": session['user_id']})
    acad_retrieval = acad_col.find_one({"_id": session['user_id']})
    return render_template("index.html", user_data=user_retrieval, acad_data=acad_retrieval)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        print("Already logged in. Redirecting to home.")
        return redirect(url_for('home'))

    global user_data, username

    if request.method == 'POST':
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        dob = request.form.get('dob')

        real_pass = sha256(password)

        user_data = {"_id": username, "email": email, "fullname": fullname, "password": real_pass, "phone": phone,
                     "gender": gender, "dob": dob}

        return redirect(url_for('register_two'))

    return render_template('register.html')


@app.route('/register_two', methods=['GET', 'POST'])
def register_two():
    if 'user_id' in session:
        print("Already logged in. Redirecting to home.")
        return redirect(url_for('home'))

    return render_template("register_two.html")


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'user_id' in session:
        print("Already logged in. Redirecting to home.")
        return redirect(url_for('home'))
    global acad_data

    if request.method == 'POST':
        grad_year = request.form.get('grad_year')
        degree = request.form.get('degree')
        major = request.form.get('major')

        acad_data = {"_id": username, "grad_year": grad_year, "degree": degree, "major": major}

        try:
            user_col.insert_one(user_data)
            acad_col.insert_one(acad_data)
            print("Insertion successful")
            session['user_id'] = username
            return redirect(url_for('home'))
        except errors.DuplicateKeyError:
            print("DuplicationError. Try Again")
            flash("Duplicate mail or username. Try Again", "error")
            return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        print("Already logged in. Redirecting to home.")
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = user_col.find_one({'email': email})
        print(user)

        if not user:
            flash('Email not found!', 'error')
        elif not (user['password'] == sha256(password)):
            flash('Incorrect password!', 'error')
        else:
            flash('Login successful!', 'success')
            session['user_id'] = user['_id']
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    print("Logged out successfully")
    render_template("register.html")
    render_template("register_two.html")
    render_template("login.html")
    return redirect(url_for('login'))


@app.route('/donation')
def donation():
    return render_template('donation.html')


@app.route('/alumni')
def alumni():
    return render_template("alumni.html")

@app.route('/networking')
def networking():
    return render_template("networking.html")

@app.route('/events')
def events():
    return render_template("events.html")

if __name__ == '__main__':
    print("Trying to connect to the database.")
    try:
        client.admin.command('ping')
        print("Database connected successfully.")
    except Exception as e:
        print(e)
        sys.exit(1)
    app.run()
