import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    full_name = Column(String(250), nullable=False)
    followers_count = Column(String(250), nullable=False)
    following_count = Column(String(250), nullable=False)
    

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    image_url = Column(String(250), nullable=False)
    likes_count = Column(Integer, nullable=False)
    coments_count = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comnemt_id = Column(String(250), primary_key=True)
    post_id = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('post.id'))
    person = relationship(Post)

class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    like_id = Column(String(250), primary_key=True)
    post_id = Column(String(250), nullable=False)
    comment_id = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('post.id'))
    person = relationship(Post)  
      

class Follow(Base):
    __tablename__ = 'follow'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follow_id = Column(String(250), primary_key=True)
    follower_id = Column(String(250), nullable=True)
    following_id = Column(String(250), nullable=True)
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)      
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
