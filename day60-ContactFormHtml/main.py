
from flask import Flask,render_template

app=Flask(__name__,template_folder='template')
from flask import request


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods= ["POST"])
def recieve_data():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template('login.html',username=username , password=password)

if __name__=="__main__":
    app.run(debug=True)