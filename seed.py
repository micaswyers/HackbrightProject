import model
import csv

def load_blogs(session):
    with open('seed_data/blog_info.csv') as csvfile:
        blog_info = csv.reader(csvfile)
        for row in blog_info:
            blog = model.Blog(filename=row[0])
            session.add(blog)
        session.commit()

def load_posts(session):
    with open('seed_data/posts.csv') as csvfile:
        cluster_info = csv.reader(csvfile, delimiter='|')
        for row in cluster_info:
            parent_cluster = row[0]
            blog= session.query(model.Blog).filter_by(filename=row[1]).first()
            post = model.Post(cluster_id=parent_cluster, blog_id=blog.id, text=row[2])
            session.add(post)
        session.commit()

def load_clusters(session):
    with open('seed_data/clusters.csv') as csvfile:
        ids_and_vectors = csv.reader(csvfile, delimiter = "|")
        for row in ids_and_vectors:
            cluster = model.Cluster(id=row[0], centroid_values=eval(row[1]))
            session.add(cluster)
        session.commit()

def main(session):
    #Call each of the load_* functions with the session as the argument
    load_clusters(s)
    load_blogs(s)
    load_posts(s)


if __name__ == "__main__":
    model.create_db()
    model.create_tables()
    s = model.connect()
    main(s)