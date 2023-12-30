import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

REPO_NAME = "inkvent"
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route("/index.html")
def index():
    return render_template("index.html", pages=pages)


@app.route("/<path:path>/index.html")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)


@app.route("/about.html")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    freezer.freeze()
    print(page)
    app.run(port=8000)
