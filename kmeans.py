"""
takes in an array of feature vectors
normalizes(whitens) feature vectors to account for disparate lengths
clusters into k groups 
returns centroids of k-groups & groupings
"""

import sys
from numpy import array
from scipy.cluster.vq import whiten, vq, kmeans, kmeans2

def get_vectors(input = sys.stdin):
    vectors = []
    for line in input:
        vectors.append(array(eval(line)))
    return vectors

def main(input): 
    whitened = whiten(obs=get_vectors(input))

    # if using kmeans :
    results = kmeans(whitened,12)
    print "Centroids: ", results[0]
    clustered_results = vq(whitened, results[0])
    print "Groupings: ", clustered_results[0]
    #turns array into a list:
    # list = map(None, clustered_results[0]) 
    # print list

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
