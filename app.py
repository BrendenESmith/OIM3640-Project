"""
Flask application for Online Media Website Scraper. Provided a topic, returns articles/potss from 
"""

from flask import Flask, render_template, request
from reddit import reddit_sentiments

from twitter import tweet_sentiments

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        ttopic = str(request.form["twitter_topic"])
        tnumber = int(request.form["twitter_post_num"])
        tresult = tweet_sentiments(ttopic,tnumber)
        rtopic = str(request.form["reddit_topic"])
        rnumber = int(request.form["reddit_post_num"])
        rresult = reddit_sentiments(rtopic,rnumber)
        if tresult and rresult:
            return render_template("result.html", ttopic = ttopic, tnumber = tnumber, tresult = tresult, rtopic = rtopic, rnumber = rnumber, rresult=rresult)
        else:
            return render_template("error.html", error=True)
    return render_template("homepage.html", error=None)

if __name__ == "__main__":
    app.run(debug=True)