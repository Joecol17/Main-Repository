from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Toka_fitness_HTML.html')  

if __name__ == '__main__':
    app.run(debug=True)
