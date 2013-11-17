"""
takes in an array of feature vectors
normalizes(whitens) feature vectors to account for disparate lengths
clusters into k groups 
returns centroids of k-groups & groupings
"""

import sys
from numpy import array
from scipy.cluster.vq import whiten, vq, kmeans, kmeans2

# def get_vectors(input = sys.stdin):
#     vectors = []
#     for line in input:
#         vectors.append(array(input))

#     return vectors

def evaluate_input(input):
    vectors = []
    filenames = []
    for line in input:
        line = eval(line)
        vectors.append(line[0])
        filenames.append(line[1])
    return vectors, filenames

def main(input): 
    vectors, filenames = evaluate_input(input)
    whitened = whiten(obs=vectors)
    # if using kmeans :
    results = kmeans(whitened,12)
    print "Centroids: ", results[0]
    clustered_results = vq(whitened, results[0])
    print "Groupings: ", zip(clustered_results[0], filenames)

    #  # if using kmeans2 :
    # results2 = kmeans2(whitened, 3) 
    # print "KMEANS2: ", results2[1] 

if len(sys.argv) > 1:
    for pathname in sys.argv[1:]:
        pathname = open(pathname)
        main(pathname)
        pathname.close()
else:
    main(sys.stdin)
