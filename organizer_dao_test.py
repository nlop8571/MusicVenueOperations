# product_dao_test_stubs.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from organizer_dao import OrganizerDAO

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

def get_db_session():

    engine = create_engine(DATABASE_URI, echo=False)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def test_create():

    session = get_db_session()

    organ = OrganizerDAO()

    data = {
        'firstname':"Larry",
        'lastname':"David",
        'phonenumber':"0449281737",
        'emailaddress':"backflipking26@hotmail.com",
    }

    result = organ.create(session, data)

    print(result)

    session.close()

def test_find_by_id():

    session = get_db_session()

    organ = OrganizerDAO()

    organizer_id = 1001

    result = organ.find_by_id(session, organizer_id)

    print(result)
    
    session.close()

def test_find_all():

    session = get_db_session()

    organ = OrganizerDAO()

    result = organ.find_all(session)

    print(result)

    session.close()   

def test_find_ids():

    session = get_db_session()

    organ = OrganizerDAO()

    result = organ.find_ids(session)

    print(result)

    session.close()

def test_update():

    session = get_db_session()

    organ = OrganizerDAO()

    organizer_id = 1001

    data = {}
    data['firstname'] = "Larry"
    data['lastname'] = "David"
    data['phonenumber'] = "0449281737"
    data['emailaddress'] = "backflipking26@hotmail.com"

    result = organ.update(session, organizer_id, data)

    print(result)

    session.close()  

def test_delete():

    session = get_db_session()
        
    organ = OrganizerDAO()

    organizer_id = 1001

    result = organ.delete(session, organizer_id)

    print(result)

    session.close()      

if __name__ == "__main__":

    print("\nTesting ...")

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_ids()

    test_update()

    test_delete()

    
