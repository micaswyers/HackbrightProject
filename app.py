from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
import json
import parse
from scipy.spatial.distance import euclidean
app = Flask(__name__) #What does this do? 
# app.config.from_pyfile(config.py)
db = SQLAlchemy(app) 

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts", methods=["GET"]) 
def butts():
    input_text = request.args.get("input_text")
    words, exclamation_count = parse.make_wordcount_dict(input_text)
    I_count = parse.count_i(words)
    total_words = 0
    average_sentence_length = parse.find_average_sentence_length(input_text)

    for word in words:
        total_words += words[word]
    scores = [total_words, I_count, exclamation_count, average_sentence_length] 
    scores = [x+0.001 for x in scores] #prevents divide-by-0 errors
    


    return json.dumps([{'I_count': I_count, 'total_words': total_words, 'exclamation_count': 'exclamation_count', 'average_sentence_length': average_sentence_length}])


if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)