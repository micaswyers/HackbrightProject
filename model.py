from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session

ENGINE = create_engine("postgres://Mica@/postgres", echo=True)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

#Begin class declarations
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key = True)
    filename = Column(String(64))
    posts = relationship("Post", backref=backref("blog", order_by=id)) #um what does this do?


class Post(Base):
    __tablename__ = "posts" 

    id = Column(Integer, primary_key = True)
    cluster_id = Column(Integer, ForeignKey('clusters.id'))
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    text = Column(Text)


class Cluster(Base):
    __tablename__ = "clusters"

    id = Column(Integer, primary_key = True)
    centroid_values = Column(ARRAY(Float), nullable=True)

#End class declarations
def create_db():
    connection = ENGINE.connect() 
    connection.execute("commit")
    connection.execute("DROP DATABASE IF EXISTS recommendations")
    connection.execute("commit")
    connection.execute("CREATE DATABASE recommendations")

def create_tables():
    Base.metadata.drop_all(ENGINE)
    Base.metadata.create_all(ENGINE)

def connect():
    
    ENGINE = create_engine("postgres://Mica@/postgres", echo=True)
    Session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

    return Session()

def get_cluster_centroids():
    clusters = session.query(Cluster).all()
    return [ cluster.centroid_values for cluster in clusters ]

def get_posts_by_cluster_id(cluster_id):
    posts = session.query(Post).filter_by(cluster_id = cluster_id).all()
    return [ post.text for post in posts]

