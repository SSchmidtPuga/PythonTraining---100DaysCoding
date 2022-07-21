from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label= 'Email', validators= [DataRequired(), Email(), Length(4,20, message= "Please type a email")])
    password = PasswordField(label = 'Password', validators= [DataRequired(), Length(4,10, message= "Please type a password")])
    submit = SubmitField(label="Submit")

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        if login.email.data == "admin@email.com" and login.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form= login)




if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)