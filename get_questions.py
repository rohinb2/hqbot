#http://www.quizwise.com/
import json
import urllib2
from bs4 import BeautifulSoup as soup

def get_json(link):

    questions = []

    html = urllib2.urlopen(link)
    text = soup(html, "html5lib")
    for question_block in text.find_all("div", {"class":"questionBlock"}):
        for div in question_block.find_all("div", {"class": "question"}):
            question = div.p.text.strip()
        options = []
        for div in question_block.find_all("div", {"class":"answer"}):
            for div_answer in div.find_all("div", {"class":"answerText"}):
                options.append(div_answer.text.strip())
        for div in question_block.find_all("div", attrs={"color":"rgb(0, 136, 0)"}):
            print div.text
        dict = {}
        dict["question"] = question
        dict["options"] = options
        dict["answer"] = ""
        questions.append(dict)
    print json.dumps(questions, sort_keys=True, indent=4, separators=(',', ': '))


get_json("http://www.quizwise.com/general-knowledge-quiz/2017-09-21")
