from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/home')
def red_home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        dob = request.form.get('dob')

        # Process or store the data as needed
        return f"Registration successful for {username}!"

    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')

    # Process the data (e.g., print it or store it)
    return f"Received name: {name} and email: {email}"

if __name__ == '__main__':
    app.run()
