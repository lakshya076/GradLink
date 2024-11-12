import sys
from flask import Flask, render_template, redirect, request, url_for, flash
from pymongo.mongo_client import MongoClient
from pymongo import errors
from Utility.encryption import sha256

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


def insert_user(data: dict, collection):
    """
    Inserts a new user document into the collection.
    """

    try:
        collection.insert_one(data)
        print("Insertion successful")
    except errors.DuplicateKeyError:
        print("DuplicationError. Try Again")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
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
    return render_template("register_two.html")


@app.route('/submit', methods=['GET', 'POST'])
def submit():
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
            return redirect(url_for('home'))
        except errors.DuplicateKeyError:
            print("DuplicationError. Try Again")
            flash("Duplicate mail or username. Try Again", "error")
            return render_template('register.html')


if __name__ == '__main__':
    print("Trying to connect to the database.")
    try:
        client.admin.command('ping')
        print("Database connected successfully.")
    except Exception as e:
        print(e)
        sys.exit(1)
    app.run()
