from newspaper import Article
import heapq
import newspaper
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time

# Retrieve data as article1 using newspaper library
def guardian_url_list():
    req = requests.get("https://www.theguardian.com/uk")
    req.status_code

    frontpage = req.content
    s = BeautifulSoup(frontpage, 'html5lib')
    frontpage_articles = s.find_all('h3', class_='fc-item__title')
    
    url_list = []

    for n in range(len(frontpage_articles)):  
        if "live" in frontpage_articles[n].find('a')['href']:  
            continue
        
        url = frontpage_articles[n].find('a')['href']
        url_list.append(url)
        
    return url_list

def dailymail_url_list():
    req = requests.get("https://www.dailymail.co.uk")
    req.status_code

    frontpage = req.content
    s = BeautifulSoup(frontpage, 'html5lib')
    frontpage_articles = s.find_all('h2', class_='linkro-darkred')
    
    url_list = []
    for n in range(len(frontpage_articles)):  
        url = "https://www.dailymail.co.uk" + frontpage_articles[n].find('a')['href']
        url_list.append(url)
        
    return url_list

def retrieve_text_single(url1):
    article1 = Article(url1)
    return article1

# After retrieving, make an empty dictionary in order to find out what is top 10 most frequently used words, and make histogram


def analysis_top10_single(url1):
    article1 = retrieve_text_single(url1)
    histogram_art1 = dict()
    # download article1 and parse it so we can read the file
    article1.download()
 
    article1.parse()
    # pulling content out of article 1 as a text version like string
    text = article1.text

    # referred from stack overflow
    # cleaning up the text file, removing conjunctions like 'and' 'but' 'if' and pronouns
    text = ''.join([x for x in text if x in string.ascii_letters + '\'- '])
    # pulling only nouns out of the text, then make a list --> noun list
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tags if (
        pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
# Simple Histogram for loop / Making word frequency dictionary (histogram_art1)
    for word in nouns:
        if word not in histogram_art1:
            histogram_art1[word] = 1
        else:
            histogram_art1[word] += 1
    # heapq --> Pulling Top 10 most frequently used words from dictionary
    top10_1 = heapq.nlargest(10, histogram_art1, key=histogram_art1.get)
    return top10_1

# It pulls out the related articles from a specific website using a pre-specified keyword


def pull_related(keyword, source):
    related_papers = []
    # bring all the articles from the source
    for url in source:
        top10_1 = analysis_top10_single(url)
        top10_1 = [x.strip().lower() for x in top10_1]
        print(top10_1)
        # If keyword matches top10_1, it will be appended in the related_papers list
        if keyword in top10_1:
            related_papers.append(url)
    return related_papers


# Pulling the links of sources related to keyword
def sentiment_analysis(keyword):
    
    guardian_urls = guardian_url_list()
    dailymail_urls = dailymail_url_list()
    
    articles_1 = pull_related(keyword, guardian_urls)
    articles_2 = pull_related(keyword, dailymail_urls)
    articles_list = [articles_1, articles_2]

    scores = [[], []]
    i = 0
    for articles in articles_list:
        for url in articles:
            # retrieving data
            try:
                response = requests.get(url)
            except requests.ConnectionError as exception:
                continue
            article = retrieve_text_single(url)
            article.download()
            article.parse()
            text = article.text
            # cleaning up the text file, removing conjunctions like 'and' 'but' 'if' and pronouns
            text = ''.join(
                [x for x in text if x in string.ascii_letters + '\'- '])
            score = SentimentIntensityAnalyzer().polarity_scores(text)
            scores[i].append(score)
        # it means that the article 1 is done and the score is saved into the list, and move on to the article 2 in the article list
        # finished traversing through source 1 because the inner for loop is completed, so we increment the place to save by 1
        i += 1
    avg = []

    for source in scores:
        neg, neu, pos, compound = 0, 0, 0, 0
        # for scores in ny or fox, we have four different variables neg, neu, pos, compound
        for s in source:
            neg += s["neg"]
            neu += s["neu"]
            pos += s["pos"]
            compound += s["compound"]
        # averaging the sentiment scores in each source
        avg.append([neg/len(source), neu/len(source), pos/len(source), compound/len(source)])
        print(len(articles_1), len(articles_2))

    return avg

print(sentiment_analysis("covid"))