import praw
from personal import client_id, client_secret, password
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username="dingdingding3",
                     password=password,
                     user_agent="user_agent")
for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)

# sub = 'learnpython'
# submissions = reddit.subreddit(sub).top('day', limit=5)
# top5 = [(submission.title, submission.selftext) for submission in submissions]