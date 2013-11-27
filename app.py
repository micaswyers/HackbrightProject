from flask import Flask, render_template
from flask import request
import json, parse, model
from utilities import normalize
from random import choice
from scipy.spatial.distance import euclidean
app = Flask(__name__) #What does this do? 

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/butts", methods=["GET"]) 
def butts():
    input_text = request.args.get("input_text")
    unicode_clean_text = normalize(input_text)

    #calculates a feature vector for sample text 
    feature_vector = parse.calculate_feature_vector(unicode_clean_text)

    #retrieves standard deviation of all post feature vectors in database
    std_dev = model.calculate_std_dev()

    #divide feature vector by standard deviation to whiten 
    whitened_feature_vector = feature_vector/std_dev

    #retrieves centroid feature vectors from the memcache/database
    cluster_objects = model.get_cluster_centroids()
    cluster_centroids = [ cluster.centroid_values for cluster in cluster_objects]

    #calculates geometric distance between sample feature vector and each cluster's centroid
    distance_to_centroids = []
    for centroid in cluster_centroids:
        distance = euclidean(centroid, whitened_feature_vector)
        distance_to_centroids.append(distance)
    
    #finds shortest distance (i.e., distance to nearest centroid)
    shortest_distance = min(distance_to_centroids)

    #Finds index/id of nearest centroid
    cluster_id = distance_to_centroids.index(shortest_distance)

    #retrieves all posts clustered around this centroid from the database, selects one at random
    post_objects = model.get_posts_by_cluster_id(cluster_id)
    random_post_object = choice(post_objects)

    return json.dumps([{'text': random_post_object.text, 'id': random_post_object.id, 'cluster': random_post_object.cluster_id, 'sample_feature_vector': feature_vector, 'post_feature_vector': random_post_object.feature_vector}])


if __name__ == '__main__': #And this, what does this do? 
    app.run(debug=True)