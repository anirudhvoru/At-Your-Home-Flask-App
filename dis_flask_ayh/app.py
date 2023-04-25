from flask import Flask, render_template, request
import sqlite3
import hashlib

app = Flask(__name__)
salt = 'm6yYM*fDc8E^gbeJiKWgyioSj@ZtGx#km!^#@e$kHWzZ$Bd$$fK63Py6EA695U2g@gfx2BgCKfMQp6Kh7SnGQJoL2uE7EYe8wRqpuv7xc!z@ajrhYEWSUGJbv@qJHiT'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/sign-in')
def signin():
    return render_template('sign-in.html')


@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')


# db apis

# Route to add a new record (INSERT) customer data to the database
@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        # try:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        try:
            contact = int(request.form['contact'])
        except Exception as e:
            msg = str(e)
            return render_template('sign-up-error.html', msg=msg)
        password = request.form['password']
        # Connect to SQLite3 database and execute the INSERT
        try:
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            # Check the user is already there or not
            cur.execute(
                "SELECT COUNT(*) FROM users WHERE email=? OR contact=?", (email, contact))
            result = cur.fetchone()
            if result[0] > 0:
                msg = 'The email or phone number already exists.'
                conn.close()
            else:
                hashed_pwd = hashlib.sha256(password.encode(
                    'utf-8') + salt.encode('utf-8')).hexdigest()
                cur.execute("INSERT INTO users (first_name, last_name, email, contact, password) VALUES (?,?,?,?,?)",
                            (first_name, last_name, email, contact, hashed_pwd))
                conn.commit()
                conn.close()
                # msg = "Thank you for signing up!"
                return render_template('sign-up-thank-you.html')
        except Exception as e:
            msg = "Got this Error : " + "e"

        return render_template('sign-up-error.html', msg=msg)


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            hashed_pwd = hashlib.sha256(password.encode(
                'utf-8') + salt.encode('utf-8')).hexdigest()
            cur.execute(
                "SELECT * FROM users WHERE email=? AND password=?", (email, hashed_pwd))
            result = cur.fetchone()
            print('result', result)
            if result:
                msg = 'Login Succesful!!'
                print("msg", msg)
                return render_template('sign-in-thank-you.html')
            else:
                # msg = 'Password is incorrect.'
                return render_template('sign-in-error.html')
        except Exception as e:
            # msg = "Internal Server Error : " + str(e)
            return render_template('sign-in-error.html')
        

if __name__ == '__main__':
    app.run(debug=True)
