from _curses import window

from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/456e2b2881d8810340f0")
data = response.json()
list = []
for post in data:
    list.append((post))
    print(list)
    print(list[ 0]["id"])

app = Flask(__name__)




@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/456e2b2881d8810340f0")
    data = response.json()
    return render_template("index.html", data = data)

@app.route('/post/<num>')
def read(num):
    global body_text, title, subtitle
    response = requests.get(url="https://api.npoint.io/456e2b2881d8810340f0")
    data = response.json()
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == num:
            requested_post = blog_post
        return render_template("post.html", post = blog_post, )

if __name__ == "__main__":
    app.run(debug=True)
