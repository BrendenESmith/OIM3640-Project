import praw
from textblob import TextBlob
from personal import client_id, client_secret, password
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username="dingdingding3",
                     password=password,
                     user_agent="user_agent")

community = reddit.subreddit("learnpython").hot(limit=10)
for submission in community:
    print(f'{submission.title} by:{submission.author}      \ntotal comments: {submission.num_comments}\nurl: {submission.url}\n')

# sub = 'learnpython'
# submissions = reddit.subreddit(sub).top('day', limit=5)
# top5 = [(submission.title, submission.selftext) for submission in submissions]