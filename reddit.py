import praw
from textblob import TextBlob
from private import client_id, client_secret, password
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
from praw.models import MoreComments
from pprint import pprint
import statistics
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
        print(f'\n--------------------------------\nTitle: {submission.title}\n--------------------------------\nby: {submission.author}\nupvotes: {submission.score}\ntotal comments: {submission.num_comments}\n\n{submission.selftext}\n\nurl: {submission.url}\n')
        for first_comment in submission.comments:
            if isinstance(first_comment, MoreComments):
                continue
                # pprint(first_comment.body)
            commentsArray.append(first_comment.body)
    pprint(commentsArray[:3])
    SIA = sia()
    compound_results = []   
    for i in commentsArray:
        r_score = SIA.polarity_scores(i)
        # print(r_score)
        # Identifying the compound score in each comment
        compound_score = r_score["compound"]
        # Making a list of all the compound scores
        compound_results.append(compound_score)
    # print(compound_results)
    # Averaging the compound score list to find the average compound score across the comments
    avg_comp_score = statistics.mean(compound_results)
    print(avg_comp_score)
    print (f'average compound score: {avg_comp_score}')
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