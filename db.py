from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  


users = {
    "admin": "password123",
    "user1": "mypassword"
}

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
