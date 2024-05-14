#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    try:
        print('{} logs'.format(nginx_collection.count_documents({})))
        print('Methods:')
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        for method in methods:
            req_count = len(list(nginx_collection.find({'method': method})))
            print('\tmethod {}: {}'.format(method, req_count))
        status_checks_count = len(list(
            nginx_collection.find({'method': 'GET', 'path': '/status'})
        ))
        print('{} status check'.format(status_checks_count))
    except Exception as e:
        print(f"An error occurred: {e}")


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        print_nginx_request_logs(client.logs.nginx)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    run()
