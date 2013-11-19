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
    #Writes a CSV file with the cluster & blog [filename] that each post belongs to
    f = open('seed_data/groupings.csv', 'wb')
    writer=csv.writer(f, delimiter = "|")
    for item in groupings_list:
        writer.writerow(item)

def write_centroids_to_csv(centroids_list):
    cluster_ids = [number for number in range(len(centroids_list))]
    centroids_list = centroids_list.tolist()
    centroids_list = [map(lambda x: round(x, 3), item) for item in centroids_list ]
    ids_and_vectors = zip(cluster_ids, centroids_list)
    f = open('seed_data/centroids.csv', 'wb')
    writer=csv.writer(f, delimiter="|")
    for item in ids_and_vectors:
        writer.writerow(item)



def main(input): 
    vectors, filenames = evaluate_input(input)
    whitened = whiten(obs=vectors)

    centroids = kmeans(whitened,12)
    write_centroids_to_csv(centroids[0])

    clustered_results = vq(whitened, centroids[0])
    cluster_and_filename = zip(clustered_results[0], filenames)
    write_groupings_to_csv(cluster_and_filename)



if len(sys.argv) > 1:
    for pathname in sys.argv[1:]:
        pathname = open(pathname)
        main(pathname)
        pathname.close()
else:
    main(sys.stdin)
