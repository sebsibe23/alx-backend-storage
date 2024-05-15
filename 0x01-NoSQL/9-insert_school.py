#!/usr/bin/env python3
'''Task 9's module.
'''

def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection.
    '''
    try:
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
    except Exception as e:
        print(f"An error occurred: {e}")
