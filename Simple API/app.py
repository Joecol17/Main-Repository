from flask import Flask

app = Flask("__name__")

@app.route('/')
def index():
    return  "Hello, World!"

@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
