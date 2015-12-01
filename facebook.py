import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
#this class creates the table for facebook posts.
#id, message, and updated time are the columns for the table because those are the parameters of facebook's "Post" class
class FacebookPost(Base):
    __tablename__ = 'facebookPosts'
    id  = Column(String(250), primary_key = True)
    message = Column(Text(), nullable = True)
    updated_time = Column(String(250), nullable = True)
 
 #this class creates the facebook comment table. 
class FacebookComment(Base):
    __tablename__ = 'facebookComments'
    id =  Column(String(250), primary_key = True)
    userfrom  = Column(String(250), nullable = True)
    message = Column(Text(), nullable = True)
    created_time = Column(String(250), nullable = True)
#this is the method called to run the above classes. This creates the database.
if __name__ == '__main__':
    engine = create_engine('mysql://username:password@localhost/databasename')
    Base.metadata.create_all(engine)
