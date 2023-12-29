from flask import Flask, render_template, url_for, send_from_directory
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

import os

REPO_NAME = "inkvent"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))


def parent_dir(path):
    """Return the parent of a directory."""
    return os.path.abspath(os.path.join(path, os.pardir))


PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite"]
FLATPAGES_ROOT = os.path.join(APP_DIR, "articles")
FLATPAGES_EXTENSION = ".md"

pages = FlatPages(app)
freezer = Freezer(app)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/index/")
def get_all_articles():
    articles = [article for article in pages]
    # Sort pages by date
    # sorted_articles = sorted(articles, reverse=True, key=lambda page: page.meta["date"])
    return render_template("index.html", all_articles=articles)


# @app.route("/article/<int:index>/")
# def show_article(index):
#     requested_article = pages.get_or_404(str(index))
#     return render_template("article.html", article=requested_article)


if __name__ == "__main__":
    freezer.freeze()
