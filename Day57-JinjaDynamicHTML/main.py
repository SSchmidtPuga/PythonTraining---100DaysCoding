from flask import Flask, render_template
import datetime
import requests
app= Flask(__name__)

@app.route("/")
def home():
    current_year  = datetime.datetime.now()
    current_year =  current_year.year
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response = response.text
    return render_template("dynamic.html", name = name , api = response)


@app.route("/blog")
def blog():
    blog_url = "https://www.npoint.io/docs/5cfeb6ab233e4bdc9e78"
    response2  = requests.get(url=blog_url)
    all_post = response2.json()
    return render_template("blog.html", api = all_post)






if __name__ == "__main__":
    app.run(debug=True)