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
    pass

def load_clusters(sessoin):
    pass

def main(session):
    #Call each of the load_* functions with the session as the argument
    load_blogs(s)

if __name__ == "__main__":
    s = model.connect()
    main(s)