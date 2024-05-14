#!/usr/bin/env python3
'''Task 11's module.
'''

def schools_by_topic(mongo_collection, topic):
    '''Returns the list of schools having a specific topic.
    '''
    try:
        topic_filter = {
            'topics': {
                '$elemMatch': {
                    '$eq': topic,
                },
            },
        }
        return [doc for doc in mongo_collection.find(topic_filter)]
    except Exception as e:
        print(f"An error occurred: {e}")
