from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(500), unique=False, nullable=False)
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250), unique=False, nullable=False)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

class Ratingform(FlaskForm):
    rating = StringField(label= 'Starts out of 10', validators= [DataRequired(), Length(0,20, message= "Please give your review. from 0 to 10")])
    Review = StringField(label = 'Your Review', validators= [DataRequired(), Length(4,50, message= "Please update the review")])
    ranking = StringField(label = 'Give a ranking from 1 to 100', validators= [DataRequired(), Length(0,50, message= "Give a ranking from 1 to 100")])
    submit = SubmitField(label="Submit")

class Addmovie(FlaskForm):
    name = StringField(label = ' What do ypu wanna add?')
    submit = SubmitField(label="Search")



# db.create_all()


@app.route("/", )
def home():
    Movie1 = db.session.query(Movie).all()
    return render_template("index.html", movies = Movie1)



@app.route('/edit/<int:id>', methods = ["GET", "POST"])
def edit(id):
    form = Ratingform()
    Movie_id = id
    Movie_film = Movie.query.get(Movie_id)
    if form.validate_on_submit():
        Movie_film.rating = float(form.rating.data)
        Movie_film.review = form.Review.data
        Movie_film.ranking = int(form.ranking.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form = form)

@app.route("/delete/<id>")
def delete(id):
    movie_id = id
    Movie_film = Movie.query.get(movie_id)
    db.session.delete(Movie_film)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods ={"GET", "POST"})
def add():
    movies = Addmovie()
    if movies.validate_on_submit():
        api_key = "a513e9fb4dbde60cd47b4d6d50007989"
        query = movies.name.data
        response = requests.get(url=f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&page=1&include_adult=false&query={query}').json()
        response = response["results"]
        return render_template("select.html", movie_title=response )
    return render_template("add.html", movie = movies )


@app.route("/find/<int:id>")
def find_movie(id):
    api_key = "a513e9fb4dbde60cd47b4d6d50007989"
    image_url= "https://image.tmdb.org/t/p/w500"
    movie_id = id
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US").json()
    new_movie_1 = Movie(title = response["title"],
                        year= response["release_date"],
                        description = response["overview"],
                        img_url= f"{image_url}{response['poster_path']}",
                        review = "")
    db.session.add(new_movie_1)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
