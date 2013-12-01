from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
import memcache
from numpy import std
import numpy

ENGINE = create_engine("postgres://Mica@/postgres", echo=True)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

MC = memcache.Client(['127.0.0.1:11211'], debug=1)

#Begin class declarations
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key = True)
    url = Column(String(64), unique=True)
    posts = relationship("Post", backref=backref("blog", order_by=id)) #um what does this do?

class Post(Base):
    __tablename__ = "posts" 

    id = Column(Integer, primary_key = True)
    title = Column(Text)
    cluster_id = Column(Integer, ForeignKey('clusters.id'))
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    feature_vector = Column(ARRAY(Float), nullable=False)
    excerpt = Column(Text)
    url = Column(Text)

class Cluster(Base):
    __tablename__ = "clusters"

    id = Column(Integer, primary_key = True)
    centroid_values = Column(ARRAY(Float), nullable=True)

#End class declarations

def calculate_std_dev():
    std_dev = MC.get('std_dev')
    if not std_dev:
        print 'STD_DEV NOT IN MEMCACHE'
        feature_vectors = get_all_feature_vectors()
        std_dev = std(feature_vectors, axis=0)
        MC.set('std_dev', std_dev.tolist())
    std_dev = numpy.array(std_dev)
    return std_dev
    
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
    centroids = MC.get('centroids')
    if not centroids:
        print 'CENTROIDS NOT IN MEMCACHE'
        centroids = session.query(Cluster).all()
        MC.set('centroids', centroids)
    return centroids

def get_posts_by_cluster_id(cluster_id):
    post_objects = session.query(Post).filter_by(cluster_id = cluster_id).all()
    return post_objects

def get_all_feature_vectors():
    post_objects = session.query(Post).all()
    feature_vectors = []
    for post_object in post_objects:
        feature_vectors.append(post_object.feature_vector)
    return feature_vectors


