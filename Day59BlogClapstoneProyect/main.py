from flask import Flask,render_template,request
app = Flask(__name__)
import requests

response = requests.get(url="https://api.npoint.io/e75e0e49fccb076f6e84").json()

title= []
subtitle= []
author=[]
dates = []
body = []
image_url = []


for n in range(len(response)):
    title.append(response[n]['title'])
    subtitle.append(response[n]['subtitle'])
    author.append(response[n]['author'])
    dates.append(response[n]['date'])
    body.append((response[n]["body"]))
    image_url.append(response[n]["image"])


range = range(len(title))

@app.route("/")
def main():
    return render_template("index.html",  title=title,subtitle=subtitle,author=author,dates=dates, range= range)

@app.route("/index.html")
def main_2():
    return render_template("index.html", title=title,subtitle=subtitle,author=author,dates=dates, range= range)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post.html/<int:n>")
def post(n):
    title_post =  title[n]
    subtitle_post= subtitle[n]
    author_post = author[n]
    date_post= dates[n]
    body_post = body[n]
    image_post = image_url[n]
    return render_template("post.html", title_post =title_post  , subtitle_post=subtitle_post, author_post=author_post,date_post= date_post,body_post=body_post, image_post=image_post )


@app.route("/post.html/contact.html")
def post_contact():
    return render_template("contact.html")

@app.route("/post.html/about.html")
def post_aboout():
    return render_template("about.html")

@app.route("/post.html/index.html")
def post_index():
    return render_template("index.html", title=title,subtitle=subtitle,author=author,dates=dates, range= range )

@app.route("/contact",  methods=["POST"] )
def contact_form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(name)
        print(email)
        print(phone)
        print(message)
    return "<h1>Successfully sent your message</h1>"


if __name__== "__main__":
    app.run(debug=True)