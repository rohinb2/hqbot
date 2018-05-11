import io
import os
from choose_option import *

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#from googleapiclient.discovery import build
import webbrowser

from secrets import *
from choose_option import *

import operator

NUM_ANSWERS = 3

# Instantiates a client
client = vision.ImageAnnotatorClient()

def search(filename):
    # The name of the image file to annotate
    file_path = os.path.join(
        os.path.dirname(__file__), "imgs/" + filename)
        #"imgs/"+filename)
        # 'hqimgs/imageedit_6_8142551098.jpg'

    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    texts = response.text_annotations


    lines = texts[0].description.split("\n")
    lines = lines[::-1]
    del lines[0]
    answers = []
    question = ""

    for i in range(0,len(lines)):
        if i >= NUM_ANSWERS:
            question = lines[i] + " " + question
        else:
            answers.append(lines[i])
    print(question)
    print(answers)

    choose_option(question, answers)
