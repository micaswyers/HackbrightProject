"""
takes in an array(list?) of features for each blog post
normalizes(whitens) features to account for disparate lengths
clusters into k groups 
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
    code_book = kmeans(whitened, 3) #returns tuple (codebook, distortion)
    clustered_results = vq(whitened, code_book[0])
    print clustered_results

# # This code prints out the clustering results to the CL
#     cluster_list = map(None, clustered_results[0])
#     counter = 1
#     for centroid in cluster_list:
#         print "Post #%d belongs in Cluster #%d" % (counter, centroid)
#         counter += 1

if len(sys.argv) > 1:
    for pathname in sys.argv[1:]:
        pathname = open(pathname)
        main(pathname)
        pathname.close()
else:
    main(sys.stdin)
