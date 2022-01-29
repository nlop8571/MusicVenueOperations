# schema.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship 

# Get a base class from which all mapped classes should inherit
Base = declarative_base()

# organizer class

class Organizer(Base): 
    # private protection related assignment for its name
    __tablename__ = 'organizer'

    organizer_id = Column(Integer, primary_key=True) # primary key
    firstname = Column(String(255), nullable=False) # non null
    lastname = Column(String(255), nullable=False) # non null
    phonenumber = Column(String(255), nullable=False, unique=True) # non null, unique
    emailaddress = Column(String(255), nullable=False, unique=True) # non null, unique
    

# Artists class
class Artists(Base):
    __tablename__ = 'artists' 

    artists_id = Column(Integer, primary_key=True) # primary key
    artistsname = Column(String(255), nullable=False) # non null
    
   

# Event class
class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True) #primary key
    venue = Column(String(255), nullable=False, unique=True) #non null
    date = Column(String(255), nullable=False, unique=True) #non null
    times = Column(String(255), nullable=False, unique=True) # non null
    capacity = Column(String(255), nullable=False, unique=False)


