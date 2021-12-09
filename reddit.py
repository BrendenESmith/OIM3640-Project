import praw
from textblob import TextBlob
from private import client_id, client_secret, password
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
from praw.models import MoreComments
from pprint import pprint
reddit_api = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username="dingdingding3",
                     password=password,
                     user_agent="user_agent")
def reddit_posts(sub, num_of_posts):
    """
    This function takes a user-entered topic and how many reddit posts they want to analyze. It returns the average compound score of the submissions from the sentiment analysis and the submission title, number of comments, submission author, submission url, and 5 comments. 
    """
    commentsArray = []
    community = reddit_api.subreddit(sub).hot(limit= int(num_of_posts))
    for submission in community:
        print(f'Title:{submission.title} \nby:{submission.author}\nupvotes: {submission.score}\ntotal comments: {submission.num_comments}\nurl: {submission.url}\n')
        for first_comment in submission.comments:
            if isinstance(first_comment, MoreComments):
                continue
            commentsArray.append(first_comment.body)
        pprint(commentsArray[:5])
        SIA = sia()
        results = []   
        for i in commentsArray:
            r_score = SIA.polarity_scores(i)
            results.append(r_score)
        pprint(r_score,width=100)
        r_compound = []
        for key, value in r_score.items():
            if key == "compound":
                r_compound.append(value)
        print(r_compound)

# result = SentimentIntensityAnalyzer()
# def nltk_sentiment(review, sub_entries_nltk):
#     result1 = result.polarity_scores(review)
#     if not result1

        



def main():
    topic = input("Please enter the subreddit you'd wish to search: ")
    num_of_posts = input("Please enter the number of submissions you would like to see: ")
    reddit_posts(topic, num_of_posts)
    # reddit_sentiment(commentsArray)

# def post_thread(f_comment,o_comment,sub_entries_textblob,sub_entries_nltk):
#     if len(f_comment.replies)==0:
#         o_comment = 0
#         return
#     else: 
#         for 

if __name__ == '__main__':
    main()


# mywords = ["Covid-19"]
# community = reddit.subreddit("all")
# for i in community.stream.comments():
#     answers = i.body
#     if any(keyword in answers for keyword in mywords):
#         print(answers)