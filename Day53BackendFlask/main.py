from flask import Flask
import random
app = Flask(__name__)
print(__name__)





random_number = random.randint(0,9)
@app.route('/')
def hello_word():
    return '<h1 style ="text-align:center">Guess a number between 0 and 9</h1>' \
           '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route("/<int:number>")
def greet(number):
    if number > random_number:
        return '<h1 style ="text-align:center">Guess a number between 0 and 9</h1>' \
               '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'
    elif number < random_number:
        return '<h1 style ="text-align:center">Guess a number between 0 and 9</h1>' \
               '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'
    else:
        return '<h1 style ="text-align:center">Guess a number between 0 and 9</h1>' \
               '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


if __name__ == "__main__":
    app.run(debug=True)



