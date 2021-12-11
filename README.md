# OIM3640-Project
OIM3640 Project - Alex Jang, Joyce Lee, Brenden Smith

In order for this project to run independently, a user will have to install the following libraries:

* tweepy
* nltk
    * download "vader_lexicon"
    * import "SentimentIntensityAnalyzer
* statistics
* pprint
    * import pprint
* json
* praw
    * from praw.models, import "MoreComments"
* textblob
    * import "TextBlob"
* flask
    * import Flask, render_template, request

Additionally, users will have to obtain API credentials from Twitter and Reddit to access the data from their servers

NOTE: In this repository are Python files of "news.py" and "gd.py." These are code that scrapes stories from The Guardian and The Daily Mail and seeks nouns in the article that match a desired key word before running sentiment analysis. While we planned on including this in our project, the code is very intensive and took too long to run (upwards of 10-15 minutes)

Visit our [Google Site](https://sites.google.com/babson.edu/newsevaluator/home) to learn more about our project.
