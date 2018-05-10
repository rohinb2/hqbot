import unigram_query_prob
import re
import pprint
import urllib2
from bs4 import BeautifulSoup as soup
from secrets import *

from googleapiclient.discovery import build

def get_query_prob_pair_snippets(query, doc):
    query = query.lower()
    prob = unigram_query_prob.unigram_query_prob(query, doc)
    return (query, prob)

def get_query_prob_pair(query, doc):
    query = query.lower()
    prob = unigram_query_prob.unigram_query_prob(query, doc)
    return (query, prob)


def choose_option(question, options):

    cx_key = GOOGLE_CUSTOM_SEARCH_ID
    api_key = GOOGLE_API_KEY

    service = build("customsearch", "v1", developerKey=api_key)

    query_prob_pairs = []

    '''
    question = question.strip()
    res = service.cse().list( q=question, cx=cx_key).execute()
    document = ""
    for i in range(4):
        try:
            item = res["items"][i]
            link = item["link"]
            html = urllib2.urlopen(link)
            text = soup(html, "html5lib").text
            document += text.lower()
        except:
            continue

    for option in options:
        query_prob_pairs.append( get_query_prob_pair(option, document) )
    '''

    for option in options:
        and_question = "{} AND \"{}\"".format(question.strip(), option.strip())
        res = service.cse().list( q=and_question, cx=cx_key).execute()
        document = ""
        for i in range(4):
            try:
                item = res["items"][i]
                link = item["link"]
                html = urllib2.urlopen(link)
                text = soup(html, "html5lib").text
                document += text.lower()
            except:
                continue

        query_prob_pairs.append( get_query_prob_pair(option, document) )


    min_max_answer = (max(query_prob_pairs,key=lambda item:item[1]),
        min(query_prob_pairs,key=lambda item:item[1]))

    print(min_max_answer)
    return min_max_answer

if __name__ == '__main__':
    question = "What color is the sky?"
    options = ["red", "white", "blue"]
    choose_option(question, options)
