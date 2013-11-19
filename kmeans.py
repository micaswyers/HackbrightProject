"""
takes in an array of feature vectors
normalizes(whitens) feature vectors to account for disparate lengths
clusters into k groups 
returns centroids of k-groups & groupings
"""

import sys, csv
from numpy import array
from scipy.cluster.vq import whiten, vq, kmeans

def evaluate_input(input):
    vectors = []
    filenames = []
    for line in input:
        line = eval(line)
        vectors.append(line[0])
        filenames.append(line[1])
    return vectors, filenames

def write_groupings_to_csv(groupings_list):
    f = open('groupings.csv', 'wb')
    writer=csv.writer(f, delimiter = "|")
    for item in groupings_list:
        writer.writerow(item)

def main(input): 
    vectors, filenames = evaluate_input(input)
    whitened = whiten(obs=vectors)

    results = kmeans(whitened,12)
    print "Centroids: ", results[0]
    clustered_results = vq(whitened, results[0])
    cluster_and_filename = zip(clustered_results[0], filenames)
    write_groupings_to_csv(cluster_and_filename)
    # print "Groupings: ", zip(clustered_results[0], filenames)



if len(sys.argv) > 1:
    for pathname in sys.argv[1:]:
        pathname = open(pathname)
        main(pathname)
        pathname.close()
else:
    main(sys.stdin)
