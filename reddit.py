import praw
from praw import reddit
from textblob import TextBlob
from private import client_id, client_secret, password
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
from praw.models import MoreComments
from pprint import pprint
import statistics

                    
def reddit_sentiments(sub, num_of_posts):
    """
    This function takes a user-entered topic and how many reddit posts they want to analyze. It returns the average compound score of the submissions from the sentiment analysis and the submission title, number of comments, submission author, submission url, and 5 comments. 
    """
    reddit_api = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username="dingdingding3",
                     password=password,
                     user_agent="user_agent")
    commentsArray = []
    reddit_dict = {}
    community = reddit_api.subreddit(sub).hot(limit= int(num_of_posts))
    for submission in community:
        rkey = (f'\n--------------------------------\nTitle: {submission.title}\n--------------------------------\nby: {submission.author}\nupvotes: {submission.score}\ntotal comments: {submission.num_comments}\n\n{submission.selftext}\n\nurl: {submission.url}\n')
        submission.comments.replace_more(limit=0)
        # Turns each submission into a dictionary key with None as value
        # print(reddit_dict)
        # Prints out comment from one submission    
        counter = 0
        
        for first_lvl_comment in submission.comments:
            commentsArray.append(first_lvl_comment.body)
            counter += 1
            if counter > 3:
                break
            pprint(first_lvl_comment.body)            
            reddit_dict[rkey]=first_lvl_comment.body

        print(reddit_dict)


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
    print(f'Average Compound Score: {avg_comp_score}')
    return (round(avg_comp_score, 4), reddit_dict)
    


def main():
    topic = input("Please enter the subreddit you'd wish to search: ")
    num_of_posts = input("Please enter the number of submissions you would like to see: ")
    reddit_sentiments(topic, num_of_posts)



if __name__ == '__main__':
    main()

