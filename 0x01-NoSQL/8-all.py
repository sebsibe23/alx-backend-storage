#!/usr/bin/env python3
'''Task 8's module.
'''

def list_all(mongo_collection):
    '''Lists all documents in a collection.
    '''
    try:
        return [doc for doc in mongo_collection.find()]
    except Exception as e:
        print(f"An error occurred: {e}")
