"""
takes in an array(list?) of features for each blog post
normalizes(whitens) features to account for disparate lengths
clusters into k groups 
"""

import sys
from scipy.cluster.vq import whiten, vq, kmeans, kmeans2

def get_vectors(input = sys.stdin):
    vectors = []
    for line in input:
        vectors.append(eval(line))
    return vectors

def main(input): 
    whitened = whiten(obs=get_vectors(input))
    clusters = kmeans(whitened, 2)
    print clusters

# main()
print "sys.argv: ", sys.argv
if len(sys.argv) > 1:
    for pathname in sys.argv[1:]:
        pathname = open(pathname)
        main(pathname)
        pathname.close()
else:
    main(sys.stdin)
