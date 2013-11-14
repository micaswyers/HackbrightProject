from flask import Flask, render_template
import json
app = Flask(__name__) #What does this do?  

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts") #this is a resource, request things with AJAX
def butts():
    return json.dumps([{'title': 'MicaPie','post': 'Here is some text from a blog. Just use your pretend skills.'}])




if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)