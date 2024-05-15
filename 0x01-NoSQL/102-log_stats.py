#!/usr/bin/env python3
'''Task 15's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs.

    Args:
        nginx_collection: The MongoDB collection
        containing Nginx request logs.

    '''
    try:
        # Print total number of logs
        print('{} logs'.format(nginx_collection.count_documents({})))

        # Print count for each HTTP method
        print('Methods:')
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        for method in methods:
            req_count = len(list(nginx_collection.find({'method': method})))
            print('\tmethod {}: {}'.format(method, req_count))

        # Print count of status check requests
        status_checks_count = len(list(
            nginx_collection.find({'method': 'GET', 'path': '/status'})
        ))
        print('{} status check'.format(status_checks_count))
    except Exception as e:
        print(f"An error occurred: {e}")


def print_top_ips(server_collection):
    '''Prints statistics about the top 10 HTTP IPs in a collection.
    '''
    try:
        # Print header
        print('IPs:')

        # Aggregate request logs to get top 10 IPs
        request_logs = server_collection.aggregate([
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ])

        # Print IP statistics
        for request_log in request_logs:
            ip = request_log['_id']
            ip_requests_count = request_log['totalRequests']
            print('\t{}: {}'.format(ip, ip_requests_count))
    except Exception as e:
        print(f"An error occurred: {e}")


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')

        # Print Nginx request logs stats
        print_nginx_request_logs(client.logs.nginx)

        # Print top IPs stats
        print_top_ips(client.logs.nginx)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    run()
