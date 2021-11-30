import praw
from textblob import TextBlob
from private import client_id, client_secret, password
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username="dingdingding3",
                     password=password,
                     user_agent="user_agent")

community = reddit.subreddit("learnpython").hot(limit=5)
for submission in community:
    print(f'{submission.title} by:{submission.author}      \ntotal comments: {submission.num_comments}\nurl: {submission.url}\n')

# def post_thread(f_comment,o_comment,sub_entries_textblob,sub_entries_nltk):
#     if len(f_comment.replies)==0:
#         o_comment = 0
#         return
#     else: 
#         for 
