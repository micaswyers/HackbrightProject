import model
import csv


def load_blogs(session):
    with open('blog_info.csv') as csvfile:
        blog_info = csv.reader(csvfile)
        for row in blog_info:
            blog = model.Blog(filename=row[0])
            session.add(blog)
        session.commit()

def load_posts(session):
    #check blogs table for filename, add corresponding blog.id to blog_id
    with open('groupings.csv') as csvfile:
        cluster_info = csv.reader(csvfile, delimiter='|')
        for row in cluster_info:
            parent_cluster = row[0]
            blog= session.query(model.Blog).filter_by(filename=row[1]).first()
            post = model.Post(cluster=parent_cluster, blog_id=blog.id)
            session.add(post)
        session.commit()

def load_clusters(session):
    pass

def main(session):
    #Call each of the load_* functions with the session as the argument
    #load_blog(s)
    load_posts(s)


if __name__ == "__main__":
    s = model.connect()
    main(s)