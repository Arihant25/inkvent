# Inkvent

This is a blog written by Arihant and ira about random stuff.

How to run locally and add new articles:

**Prerequisites**: You need [Python](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads) installed.

1. Clone the repo

    ```
    git clone https://github.com/Arihant25/inkvent.git
    cd inkvent
    ```
2. Create and activate a virtual environment

    ```
    python -m venv venv
    .\venv\Scripts\activate
2. Install the required packages

    `pip install -r requirements.txt`

4. Add new articles to the `\projects\pages` folder following the format given in the `page_template.md` file
5. Run the `app.py` file

    `python projects/app.py`

    The static files for the GitHub pages are generated in the root folder of the project.

6. Commit and push the changes to the repo

    ```
    git add .
    git commit -m "Commit message"
    git push
    ```