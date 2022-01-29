# product_dao_stubs.py
# France Cheong
# 11/12/2018

# Import packages
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from schema import Organizer

class OrganizerDAO():

    def create(self, session, data):

        print("\nCreating a product ...")
        print(data)

        organizer = Organizer(firstname = data['firstname'],
                              lastname = data['lastname'],
                              phonenumber = data['phonenumber'],
                              emailaddress = data['emailaddress'],
                    )

        session.add(organizer)
        session.commit()

        result = {}
        result['message'] = 'Organizer added successfully!'
        inserted_organizer_id = organizer.organizer_id
        result['organizer_id'] = inserted_organizer_id
        return result

    def find_by_id(self, session, organizer_id):

        print("\nFinding organizer...")
        print(organizer_id)

        organ = session.query(Organizer).get(organizer_id)

        result = {}

        if not organ:
            result['message'] = "Organizer not found"
        else:
            d = {}
            d['organizer_id'] = organ.organizer_id
            d['firstname'] = organ.firstname
            d['lastname'] = organ.lastname
            d['phonenumber'] = organ.phonenumber
            d['emailaddress'] = organ.emailaddress
            

            result['organizer'] = d

        return result

    def find_all(self, session):

        print("\nFinding all organizers ...")

        result = {}

        rows = session.query(Organizer).all()

        if not rows:
            result['message'] = "No organizers found!"
        else:
            list_organ = []
            for x in rows:
                d = {}
                d['organizer_id'] = x.organizer_id
                d['firstname'] = x.firstname
                d['lastname'] = x.lastname
                d['phonenumber'] = x.phonenumber
                d['emailaddress'] = x.emailaddress
                list_organ.append(d)
                pass

            result['organizers'] = list_organ
        
        return result
    
    def find_ids(self, session):

        print("\nFinding all organizer ids ...")

        result = {}

        rows = session.query(Organizer).all()

        if not rows:
            result['message'] = "No organizers found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.organizer_id)
                pass

            result['organizer_ids'] = list_ids

        return result
    
    def update(self, session, organizer_id, data):

        print("\nUpdating organizer ...")
        print(organizer_id)
        print(data)
        
        result = {}

        organ = session.query(Organizer).get(organizer_id)

        organ.firstname = data['firstname']
        organ.lastname = data['lastname']
        organ.phonenumber = data['phonenumber']
        organ.emailaddress = data['emailaddress']
        
        
        session.commit()
        
        result['message'] = "Organizer updated!"

        return result

    def delete(self, session, organizer_id):

        print("\nDeleting organizer ...")
        print(organizer_id)

        result = {}

        organ = session.query(Organizer).get(organizer_id)
        session.delete(organ)
        session.commit()

        result['message'] = "Organizer deleted."

        return result
        
