import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics
import pprint


def tweet_sentiments(topic, num_of_tweets):
    """This function takes a user-entered topic and how many tweets they'd like to analyze. It returns and average
    compound score of the tweets from the sentiment analysis and a dictionary of the Twitter user names and tweets
    in question."""
    # Keys and secrets
    TOKEN = '1049810324365430786-L0iaMkrCz1uNxygUycZFdFhExC4ULT'
    TOKEN_SECRET = 'vmoBdQ9Q96LEif5hIxyOVao3KQgO4ZSROs9bMbnprthK1'
    CONSUMER_KEY = 'mZ5gp1MWCi0aEmecoUxvWUEO3'
    CONSUMER_SECRET = 'YhwtTjvEe1zPnlUSlCWOVFRJsWXE8jgo4ek4pHaHJPqPHpRsst'

    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKObVAEAAAAASmYKqe7QJEqJpHRcDgvGSmKnSqI%3DQsdD34IKqTbqfmjcnTuzrqTzZbkzoF8VsropQqjGj0BoqEEPYh"

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(TOKEN,TOKEN_SECRET)

    api = tweepy.API(auth)

    # for tweet in api.search_tweets(q="Dune", lang="en", count = 5):
    #     print(f"{tweet.user.name}: {tweet.text}")

    tweet_counter = 0
    tweet_list_compounds = []
    user_key = []
    tweet_value  = []
    tweet_dict = dict()
    for tweet in api.search_tweets(q = topic, result_type = "popular", count = 100):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
        overall_compound = score["compound"]
        if overall_compound != 0.0:
            user_key.append(tweet.user.screen_name)
            tweet_value.append(tweet.text)
            # print(f"{tweet.screen_name}: {tweet.text}")
            compound = score["compound"]
            tweet_list_compounds.append(compound)
            tweet_counter += 1
            if tweet_counter >= num_of_tweets:
                break
    
    tweet_dict = {user_key[i]: tweet_value[i] for i in range(len(user_key))}           
    avg_compound_score = statistics.mean(tweet_list_compounds)
    return round(avg_compound_score, 4), tweet_dict




def main():
    """
    Collects info from other function
    """
    topic = input("Please enter the topic you'd wish to search: ")
    num_of_tweets = int(input("Please enter how many tweets you'd like to collect: "))

    (tweet_sentiments(topic, num_of_tweets))

    function_acquisition = tweet_sentiments(topic, num_of_tweets)
    avg_compound_score = function_acquisition[0]
    tweet_dict = function_acquisition[1]
    if num_of_tweets > 1:
        print(f"Average compound score of tweets: {avg_compound_score}")
    if num_of_tweets == 1:
        print(f"Compound score of tweet: {avg_compound_score}")

    for tweets in tweet_dict:
            print(f"{tweets}: {tweet_dict[tweets]}")
    
if __name__ == '__main__':
    main()

