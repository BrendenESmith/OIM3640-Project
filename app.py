"""
Flask application for Online Media Website Scraper. Provided a topic, returns articles/potss from 
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)