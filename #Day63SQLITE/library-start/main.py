from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Book_name = db.Column(db.String(80), unique=True, nullable=True)
    Author = db.Column(db.String(80), unique=False, nullable=True)
    rating = db.Column(db.Integer, unique=True, nullable=True)

    def __repr__(self):
        return f'<Book {self.id}>


# db.create_all()
#


@app.route('/')
def home():
    data_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books, books_data= data_books)

all_books = []
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form["name"]
        author = request.form["author"]
        rating = request.form["rating"]
        new_book = Book(Book_name=book_name, Author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return render_template("add.html", msg_sent=True, msg=False)
    return render_template("add.html", msg=True)


@app.route("/edit/<int:id>",  methods=["GET", "POST"])
def ratings(id):
    new_id =id
    book_id = Book.query.get(new_id)
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        book_id.rating = new_rating
        print(new_rating)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("change_rating.html", book = book_id)

@app.route("/delete/<int:id>")
def delete(id):
    new_id =id
    book_id = Book.query.get(new_id)
    db.session.delete(book_id)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)
