import sys, csv
from scipy.cluster.vq import whiten, vq, kmeans
import numpy
from readable import call_readability
from calculate_feature_vector import calculate_feature_vector


def evaluate_input(input):
    vectors = []
    filenames = []
    text = []
    for line in input:
        line = eval(line)
        vectors.append(line[0])
        filenames.append(line[1])
        text.append(line[2])
        
    return vectors, filenames, text


def write_clusters_to_csv(centroids_list):
    cluster_ids = [number for number in range(len(centroids_list))]
    centroids_list = centroids_list.tolist()
    centroids_list = [map(lambda x: round(x, 3), item) for item in centroids_list ]
    ids_and_vectors = zip(cluster_ids, centroids_list)
    f = open('seed_data/clusters.csv', 'wb')
    writer=csv.writer(f, delimiter="|")
    for item in ids_and_vectors:
        writer.writerow(item)

def write_domains_to_csv(urls_list):
    f = open('seed_data/blog_info.csv', 'wb')
    writer=csv.writer(f, delimiter = "\n")
    writer.writerow(urls_list)
    
def write_posts_to_csv(posts_list):
    f = open('seed_data/posts.csv', 'wb')
    writer=csv.writer(f, delimiter = "|")
    writer.writerows(posts_list)

def save_post_tuples_to_csv(post_tuple_list):
    with open('saved_post_tuples.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter = "|")
        writer.writerows(post_tuple_list)

def main(): 
    post_tuple_list = []
    for post_dictionary in call_readability():
        post_tuple = calculate_feature_vector(post_dictionary)
        post_tuple_list.append(post_tuple)
    save_post_tuples_to_csv(post_tuple_list)
    feature_vectors, urls, excerpts, titles, domains = zip(*(post_tuple_list))

    write_domains_to_csv(domains)

    std_dev = numpy.std(feature_vectors, axis=0) + 0.001
    whitened = feature_vectors/std_dev
    centroids = kmeans(whitened, 50) #adjust number of clusters for precision
    write_clusters_to_csv(centroids[0])

    clustered_results = vq(whitened, centroids[0])
    # titles = [title.encode("utf8") for title in titles]
    # excerpts = [excerpt.encode("utf8") for excerpt in excerpts]

    post_data = zip(clustered_results[0], urls, feature_vectors, titles, excerpts, domains)
    write_posts_to_csv(post_data)


main()