from flask import render_template, request, Flask, session
import random
import pandas as pd
import re
import string
import pickle 


# get data
characters_dict = pickle.load(open("quotes.pickle", "rb"))

character_names = ['Obi-Wan', 'Vader', 'Luke', 'C-3PO', 'Han', 'Padme', 'Yoda', 'Anakin', 'Leia']

app = Flask(__name__)

# a simple page that says hello
@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        character = request.form['character']
        output = output_sentence(character)
        if character != None:
            return render_template('template.html', character=character, output=output)
    return render_template("template.html")

def output_sentence(character):
    character_list = characters_dict[character]
    topic_list = random.choice(character_list)
    quote = random.choice(topic_list)
    return quote


app.run(debug=True)



