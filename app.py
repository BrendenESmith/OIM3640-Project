"""
Flask application for Online Media Website Scraper. Provided a topic, returns articles/potss from 
"""

from flask import Flask, render_template, request

from twitter import tweet_sentiments

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        ttopic = str(request.form["twitter_topic"])
        tnumber = int(request.form["twitter_post_num"])
        tresult = tweet_sentiments(ttopic,tnumber)
        if tresult:
            return render_template("result.html", ttopic = ttopic, tnumber = tnumber, tresult = tresult)
        else:
            return render_template("error.html", error=True)
    return render_template("homepage.html", error=None)

if __name__ == "__main__":
    app.run(debug=True)