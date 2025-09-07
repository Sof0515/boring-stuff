from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, world!</h1> <a href="/picture">boring stuff</a>'

@app.route("/welcome")
def welcom():
    return '<h1>hi welcome to  my website!</h1>'

@app.route("/picture")
def hi():
    return '<h1>stich!</h1><img src="https://upload.wikimedia.org/wikipedia/en/d/d2/Stitch_%28Lilo_%26_Stitch%29.svg">'
app.run(debug=True)
