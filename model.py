from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, backref, sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

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
    global ENGINE
    global Session

    ENGINE = create_engine("postgres://Mica@/postgres")
    connection = ENGINE.connect() 
    connection.execute("commit")
    connection.execute("DROP DATABASE IF EXISTS recommendations")
    connection.execute("commit")
    connection.execute("CREATE DATABASE recommendations")
    connection.close()

def create_tables():
    global ENGINE
    global Session

    ENGINE = create_engine("postgresql://Mica@localhost/recommendations", echo=True)
    Base.metadata.create_all(ENGINE)

def connect():
    global ENGINE
    global Session
    
    ENGINE = create_engine("postgresql://Mica@localhost/recommendations", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

