import sys, csv
from scipy.cluster.vq import whiten, vq, kmeans

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

def write_posts_to_csv(posts_list):
    f = open('seed_data/posts.csv', 'wb')
    writer=csv.writer(f, delimiter = "|")
    for item in posts_list:
        item = (item[0], item[1], item[2], item[3].encode('utf8'))
        writer.writerow(item)

def write_clusters_to_csv(centroids_list):
    cluster_ids = [number for number in range(len(centroids_list))]
    centroids_list = centroids_list.tolist()
    centroids_list = [map(lambda x: round(x, 3), item) for item in centroids_list ]
    ids_and_vectors = zip(cluster_ids, centroids_list)
    f = open('seed_data/clusters.csv', 'wb')
    writer=csv.writer(f, delimiter="|")
    for item in ids_and_vectors:
        writer.writerow(item)

def main(input): 
    vectors, filenames, text = evaluate_input(input)
    whitened = whiten(obs=vectors)

    centroids = kmeans(whitened,15)
    write_clusters_to_csv(centroids[0])

    clustered_results = vq(whitened, centroids[0])
    clusters_filenames_vectors_texts = zip(clustered_results[0], filenames, vectors, text)
    write_posts_to_csv(clusters_filenames_vectors_texts)

if len(sys.argv) > 1:
    for pathname in sys.argv[1:]:
        pathname = open(pathname)
        main(pathname)
        pathname.close()
else:
    main(sys.stdin)
