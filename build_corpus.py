import csv
import sys
from scipy.cluster.vq import vq, kmeans
import numpy
from utilities import call_readability
from calculate_feature_vector import calculate_feature_vector

csv.field_size_limit(sys.maxsize)

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

def open_post_dictionaries_from_csv(filename):
    post_dictionary_list = []
    with open(filename, 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter="\n")
        for row in reader:
            row[0] = eval(row[0])
            post_dictionary_list.append(row[0])
    return post_dictionary_list

def write_clusters_to_csv(centroids_list):
    cluster_ids = [number for number in range(len(centroids_list))]
    centroids_list = centroids_list.tolist()
    centroids_list = [map(lambda x: round(x, 3), item) for item in centroids_list ]
    ids_and_vectors = zip(cluster_ids, centroids_list)
    with open('seed_data/clusters.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter="|")
        writer.writerows(ids_and_vectors)

def write_domains_to_csv(urls_list):
    with open('seed_data/blog_info.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter="\n")
        writer.writerow(urls_list)
    
def write_posts_to_csv(posts_list):
    with open('seed_data/posts.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter="|")
        writer.writerows(posts_list)

def main():
    #comment out if running kmeans from post_dictionaries.csv & don't need to hit Readability API
    # call_readability() 
    post_tuple_list = []
    for post_dictionary in open_post_dictionaries_from_csv('post_dictionaries.csv'):
        post_tuple = calculate_feature_vector(post_dictionary)
        post_tuple_list.append(post_tuple)
    feature_vectors, urls, titles, excerpts, domains = zip(*(post_tuple_list))

    #performs k-means clustering on feature vectors from all blog posts
    std_dev = numpy.std(feature_vectors, axis=0) + 0.001
    whitened = feature_vectors/std_dev
    centroids = kmeans(whitened, 100) #can adjust number of clusters for precision
    clustered_results = vq(whitened, centroids[0])
    post_data = zip(clustered_results[0], feature_vectors, urls, titles, excerpts, domains)

    #writes csv files to be used for seeding datatables
    write_clusters_to_csv(centroids[0])
    write_domains_to_csv(domains)
    write_posts_to_csv(post_data)

if __name__ == "__main__":
    main()