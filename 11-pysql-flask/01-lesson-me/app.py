
from flask import Flask, render_template, request
from database import get_cities
from mysql.connector import Error

app = Flask(__name__)
app.url_map.strict_slashes = False

#endpoints

@app.route("/")
def index():
    return render_template("index.html",
    heading = "I am the JinjaNinja")

@app.route("/about")
def about():
    header_me = "About me"
    author_name = "Steinar Martinussen"
    return render_template("about.html", header_about = header_me, author = author_name)


@app.route("/cities")
def cities():

    code = request.args.get("country", "NOR").strip().upper()
    if (len(code) != 3) or not code.isascii() or not code.isalpha():
        return "Invalid code", 400
    try:
        rows = get_cities(code)
    except Error:
        app.logger.exception(
            "Database query failed"
        )
        return "Database unavailable", 503
    return render_template("cities.html", code=code, rows=rows)