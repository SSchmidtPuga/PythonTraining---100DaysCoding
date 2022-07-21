import csv

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL



class TableForm(FlaskForm):
    cafe_name = StringField(label = "Cafe Name",)
    Location = StringField(label = " Cafe Location in Google Maps (Url)", validators=[ DataRequired(), URL()])
    Open_time = StringField(label = "Opening Time ",)
    Close_time = StringField(label = "Closing Time",)
    Coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    Wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    Power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    Submit = SubmitField(label = "Add ")

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/coffe")
def coffe():
    with open('cafe-data.csv', newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter = ',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('coffe.html', cafes=list_of_rows)



@app.route("/add", methods = [ "GET", "POST"])
def add():
    form = TableForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe_name},"
                           f"{form.Location},"
                           f"{form.Open_time},"
                           f"{form.Close_time},"
                           f"{form.Coffee_rating},"
                           f"{form.Wifi_rating},"
                           f"{form.Power_rating}")
            return render_template("coffe.html")

    return render_template("add.html", form =form )

if (__name__) == ("__main__"):
    app.run(host="localhost", port=5000, debug=True)
