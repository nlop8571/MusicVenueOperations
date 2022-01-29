# populate_purchase_order.py
# France Cheong
# 22/01/2019

# ########
# Packages
# ########
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Required for date ordered, date required
from datetime import date

# ###########################################
# Import your classes defined in other files
# ###########################################
# From file xxx.py import class Xxxx
from schema import Organizer
from schema import Event

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

    session.add_all([
        
        # Organizer 1
        Organizer(organizer_id = 1001, 
                  firstname = 'Larry', 
                  lastname = 'David',
                  phonenuber = '0449281737',
                  emailaddress = 'backflipking26@hotmail.com',
            
                event = [  #An organizer can have many events
         Event(
                        event_id = 1, 
                        venue = 'Grace Darling',
                        date = date(2019, 1, 25),
                        times = times(8),
                        capacity = 300
                    

         Event(
                        event_id = 2, 
                        venue = 'Section 8',
                        date = date(2019, 1, 30),
                        times = times(9),
                        capacity = 200
                        organizer_id = 1002
                        artists_id = 201


                    ] # end borrow data for table
            ), # end Organizer 1
         
       ]) # End of list to insert and closing bracket for add_all()

    # Commit the transactions
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
        populate()
