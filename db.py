from flask import Flask, render_template, request, redirect, url_for, session
import os
import sqlite3 as SQLite3
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash


DB_PATH = Path("data.db")

def build_db():
    connection = SQLite3.connect(DB_PATH)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS credential_system ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL           
        );
    """)

    connection.commit()
    connection.close()

def prepopulate_db():
    connection = SQLite3.connect(DB_PATH)
    query = connection.execute("SELECT * FROM credential_system;")
    people = query.fetchall()
    if not people:
        connection.executemany(
           "INSERT INTO credential_system (username, password) VALUES (?, ?);",
            [("Admin", "password123")]
        )

    connection.commit()
    connection.close()

def get_db():
    connection = SQLite3.connect(DB_PATH)
    connection.row_factory = SQLite3.Row
    return connection


build_db()
prepopulate_db()



app = Flask(__name__)
app.secret_key = os.urandom(24)  

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()   
        cursor = db.cursor()
    
        



@app.route('/')
def home():
    return render_template('Toka_fitness_HTML.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('profile'))
        else:
            error = "Invalid username or password."

    return render_template('Toka_fitness_Login_page.html', error=error)


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome {session['user']} to your dashboard!"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/membership')
def membership():
    return render_template('Toka_fitness_Membership.html')

@app.route('/find-gym')
def find_gym():
    return render_template('Toka_fitness_Find_GYM.html')

@app.route('/profile') 
def profile(): 
    if 'user' not in session: 
        return redirect(url_for('login')) 
    return render_template('Toka_fitness_Profile.html')

@app.route('/')
def homepage():
    return render_template('Toka_fitness_HTML.html')


if __name__ == '__main__':
    app.run(debug=True)
