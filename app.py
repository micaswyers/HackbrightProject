from flask import Flask, render_template
from flask import request
import json
import parse
app = Flask(__name__) #What does this do?  

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts", methods=["GET"]) 
def butts():
    input_text = request.args.get("input_text")
    words, exclamation_count = parse.make_wordcount_dict(input_text)
    print words
    I_count = parse.count_i(words)
    return json.dumps([{'I_count': I_count}])


if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)