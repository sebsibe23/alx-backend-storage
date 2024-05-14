#!/usr/bin/env python3
'''Task 10's module.
'''

def update_topics(mongo_collection, name, topics):
    '''
     Changes all topics of a collection's 
     document based on the name.
    '''
    try:
        mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
        )
    except Exception as e:
        print(f"An error occurred: {e}")
