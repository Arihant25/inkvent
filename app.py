from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Connect to DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "articles.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Create DB
class Article(db.Model):
    """Database table containing all articles."""

    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000))
    subtitle = db.Column(db.String(10000))
    date = db.Column(db.String(10000))
    body = db.Column(db.Text)
    author = db.Column(db.String(10000))
    img_url = db.Column(db.String(10000))
    song_url = db.Column(db.String(10000))


@app.route("/")
def get_all_articles():
    articles = db.session.query(Article).all()
    return render_template("index.html", all_articles=articles)


@app.route("/article/<int:index>")
def show_article(index):
    requested_article = db.session.query(Article).get(index)
    return render_template("article.html", article=requested_article)


@app.route("/about")
def about():
    return render_template("about.html")
