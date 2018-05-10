import re
from math import *
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def unigram_query_prob(query, document):

    #naive bayes, assuming p{query) and p(document) are uniform and bag-of-words model
    words = {}
    num_words = 0
    for word in document.split():
        word = re.sub('\W+', '', word)
        if word not in words:
            words[word] = 0
        words[word] += 1
        num_words += 1

    #count = 0
    total_probability = 1
    for query_word in query.split():
        query_word = re.sub('\W+', '', query_word)

        if query_word not in stop_words:
            total_probability *= ((words[query_word])/ float(num_words)) if query_word in words else 0
        #count += words[query_word] if query_word in words else 0

    #return count / float(len(query.split()))

    return total_probability
