from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, backref, sessionmaker

ENGINE = None
Session = None

engine = create_engine("postgresql://Mica@localhost/recommendations")

Base = declarative_base()

#Begin class declarations
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key = True)
    filename = Column(String(64))
    posts = relationship("Post", backref=backref("blog", order_by=id))


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True)
    cluster = Column(Integer)
    text = Column(Text)
    blog_id = Column(Integer, ForeignKey('blogs.id'))

class Cluster(Base):
    __tablename__ = "clusters"

    id = Column(Integer, primary_key = True)
    vector = Column(ARRAY(Integer))
#End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()