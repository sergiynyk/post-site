from flask import Flask, render_template, request
from sqlwg import BlogDB
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vjrrvrheugjvhrdhsuvfunrvfnvnisdijf43u833h3w'
db = BlogDB("baza.db")
PATH = os.path.dirname(__file__) +os.sep


@app.route("/")
def index():
    categories = db.get_all_categories()
    posts = db.get_all_posts()
    print(posts)
    return render_template("index.html", title = "АШГЦД№П?еш2пишгпи2гашдишгпйушда", posts = posts, categories = categories)

@app.route("/post/<post_id>")
def post(post_id):
    categories = db.get_all_categories()
    post = db.get_post(int(post_id))
    return render_template("post.html", title = "ПОсти", post = post, categories = categories)

@app.route("/category/<category_id>")
def posts_by_category(category_id):
    categories = db.get_all_categories()
    posts = db.get_posts_by_category(int(category_id))
    return render_template("category_post.html", title = "ПОсти", posts = posts, categories = categories)

@app.route("/newpost",methods=["POST", "GET"])
def new_post():
    categories = db.get_all_categories()
    if request.method == "POST":
        image = request.files['image']
        image.save(PATH + 'static/img/' + image.filename)
        db.create_post(request.form['title'], request.form['text'], request.form["category"], image.filename)
    return render_template("add_post.html", categories = categories)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)