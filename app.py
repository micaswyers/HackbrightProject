from flask import Flask, render_template
from flask import request
import json, parse, model
from utilies import normalize
from scipy.spatial.distance import euclidean
app = Flask(__name__) #What does this do? 

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts", methods=["GET"]) 
def butts():
    #calculates feature vector for sample text input by user
    input_text = request.args.get("input_text")
    clean_text = normalize(input_text)

    # input_text.replace(u"\u2019", "'").decode("utf8")
    words, exclamation_count = parse.make_wordcount_dict(clean_text)
    I_count = parse.count_i(words)
    total_words = 0
    average_sentence_length = parse.find_average_sentence_length(input_text)

    for word in words:
        total_words += words[word]
    scores = [total_words, I_count, exclamation_count, average_sentence_length] 
    scores = [x+0.001 for x in scores] #prevents divide-by-0 errors
    print "Sample text feature vector: ", scores

    #retrieves feature vectors from centroids (centers of each cluster) from the database
    cluster_centroids = model.get_cluster_centroids()

    #calculates geometric distance between sample feature vector and each cluster centroid
    distance_to_centroids = []
    for centroid in cluster_centroids:
        distance = euclidean(centroid, scores)
        distance_to_centroids.append(distance)
    print "DISTANCES: ", distance_to_centroids
    
    #find shortest distance (i.e., distance to nearest centroid)
    shortest_distance = min(distance_to_centroids)
    print "SHORTEST DISTANCE: ", shortest_distance

    #Finds index/id of nearest centroid
    print "INDEX/ID OF CLOSEST CENTROID: ", distance_to_centroids.index(shortest_distance)

    #retrieve all posts clustered around this centroid from db
    model.get_posts_by_cluster_id(shortest_distance)
    

    return json.dumps([{'I_count': I_count, 'total_words': total_words, 'exclamation_count': exclamation_count, 'average_sentence_length': average_sentence_length,'waiting': 'Hold on, working on it! GEEZ!!!!!! \n Pretend there is text here from a blog you want to read.'}])


if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)