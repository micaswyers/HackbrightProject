import model
import csv

def load_blogs(session):
    with open('seed_data/blog_info.csv') as csvfile:
        blog_info = csv.reader(csvfile)
        for row in blog_info:
            try:
                blog = model.Blog(url=row[0])
                session.add(blog)
                session.commit()
            except:
                session.rollback()
                continue

def load_posts(session):
    with open('seed_data/posts.csv') as csvfile:
        cluster_info = csv.reader(csvfile, delimiter='|')
        for row in cluster_info:
            try:
                parent_cluster = row[0]
                feature_vector = eval(row[1])
                url = row[2]
                title = row[3]
                excerpt = row[4]
                blog = session.query(model.Blog).filter_by(url=row[5]).first()
                post = model.Post(cluster_id=parent_cluster, blog_id=blog.id, url=url, excerpt=excerpt, title=title, feature_vector=feature_vector)
                session.add(post)
                session.commit()
            except:
                session.rollback()
                continue

def load_clusters(session):
    with open('seed_data/clusters.csv') as csvfile:
        ids_and_vectors = csv.reader(csvfile, delimiter = "|")
        for row in ids_and_vectors:
            cluster = model.Cluster(id=row[0], centroid_values=eval(row[1]))
            session.add(cluster)
        session.commit()

def main(session):
    load_clusters(s)
    load_blogs(s)
    load_posts(s)

if __name__ == "__main__":
    # model.create_db()
    s = model.connect()
    model.create_tables()
    main(s)