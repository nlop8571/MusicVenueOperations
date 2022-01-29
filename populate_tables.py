# populate_tables.py
# France Cheong
# 22/01/2019

# ########
# Packages
# ########
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ###########################################
# Import your classes defined in other files
# ###########################################
# From file xxx.py import class Xxxx
from schema import Event
from schema import Artists


# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def populate():

    # Get a session
    session = get_db_session()


    # Insert a list [] of Events
    session.add_all([
         Event(venue = 'Grace Darling',
               date = '2019, 1, 25',
               times = '8:00',
               capacity = '300'),   

         Event(venue = 'Section 8',
               date = '2019, 1, 30',
               times = '9:00',
               capacity = '200'),
         ])


    # List of Artists
    session.add_all([
          Artists(artistsname = 'Tame Impala'),
            
          Artists(artistsname = 'Mac Demarco'),
          ])

    # Commit the transactions
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
        populate()
