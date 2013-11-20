from flask import Flask, render_template
from flask import request
import json, parse, model
from utilies import normalize
from random import choice
from scipy.spatial.distance import euclidean
app = Flask(__name__) #What does this do? 

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts", methods=["GET"]) 
def butts():
    input_text = request.args.get("input_text")
    clean_text = normalize(input_text)

    #calculates feature vector for sample text input by user
    words, exclamation_count = parse.make_wordcount_dict(clean_text)
    I_count = parse.count_i(words)
    total_words = 0
    average_sentence_length = parse.find_average_sentence_length(input_text)

    for word in words:
        total_words += words[word]
    scores = [total_words, I_count, exclamation_count, average_sentence_length] 
    scores = [x+0.001 for x in scores] #prevents divide-by-0 errors
    print "SAMPLE TEXT FEATURE VECTOR ", scores

    #retrieves feature vectors from centroids (centers of each cluster) from the database
    cluster_objects = model.get_cluster_centroids()
    print "CLUSTERS: ", [cluster.id for cluster in cluster_objects]

    cluster_centroids = [ cluster.centroid_values for cluster in cluster_objects]
    print "CENTROID VALUES: ", cluster_centroids

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
    cluster_id = distance_to_centroids.index(shortest_distance)
    print "INDEX/ID OF CLOSEST CENTROID: ", cluster_id

    #retrieve all posts clustered around this centroid from db
    posts = model.get_posts_by_cluster_id(cluster_id)
    random_post = choice(posts)


    return json.dumps([{'I_count': I_count, 'total_words': total_words, 'exclamation_count': exclamation_count, 'average_sentence_length': average_sentence_length, 'post': random_post}])


if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)