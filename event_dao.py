# event_dao.py
# France Cheong
# 11/12/2018

# Import packages
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from schema import Event

class EventDAO():

    def create(self, session, data):

        print("\nCreating an a event ...")
        print(data)


        event = Event(venue = data['venue'],
                     date = data['date'],
                     times = data['times'],
                     capacity = data['capacity'],
                    )

        session.add(event)
        session.commit()

        result = {}
        result['message'] = 'Event added successfully!'
        inserted_event_id = event.event_id
        result['event_id'] = inserted_event_id
        return result

    def find_by_id(self, session, event_id):

        print("\nFinding event...")
        print(event_id)

        eve = session.query(Event).get(event_id)

        result = {}

        if not eve:
            result['message'] = "Event not found"
        else:
            d = {}
            d['event_id'] = eve.event_id
            d['venue'] = eve.venue
            d['date'] = eve.date
            d['times'] = eve.times
            d['capacity'] = eve.capacity

            
            result['event'] = d

        return result

    def find_all(self, session):

        print("\nFinding all event ...")

        result = {}

        rows = session.query(Event).all()

        if not rows:
            result['message'] = "No events found!"
        else:
            list_eve = []
            for x in rows:
                d = {}
                d['event_id'] = x.event_id
                d['venue'] = x.venue
                d['date'] = x.date
                d['times'] = x.times
                d['capacity'] = x.capacity

                list_eve.append(d)
                pass

            result['event'] = list_eve
        
        return result
    
    def find_ids(self, session):

        print("\nFinding all event ids ...")

        result = {}

        rows = session.query(Event).all()

        if not rows:
            result['message'] = "No Event found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.event_id)
                pass

            result['event_ids'] = list_ids

        return result
    
    def update(self, session, event_id, data):

        print("\nUpdating event ...")
        print(event_id)
        print(data)
        
        result = {}

        eve = session.query(Event).get(event_id)
        
        eve.venue = data['venue']
        eve.date = data['date']
        eve.times = data['times']
        eve.capacity = data['capacity']
        
        session.commit()
        
        result['message'] = "Event updated!"

        return result

    def delete(self, session, event_id):

        print("\nDeleting Event ...")
        print(event_id)

        result = {}

        eve = session.query(Event).get(event_id)
        session.delete(eve)
        session.commit()

        result['message'] = "Event deleted."

        return result
        
