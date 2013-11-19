from flask import Flask, render_template
from flask import request
import json
import parse
app = Flask(__name__) #What does this do?  

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts", methods=["GET"]) #this is a resource, request things with AJAX
def butts():
    input_text = request.args.get("input_text")
    words, exclamation_count = parse.make_wordcount_dict(input_text)
    print words, exclamation_count
    # return json.dumps([{'hello': 'hello'}])
    return json.dumps([{'word_count': words,'exclamation_count': exclamation_count}])


if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)