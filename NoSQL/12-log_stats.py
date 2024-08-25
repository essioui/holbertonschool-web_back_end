#!/usr/bin/env python3
"""
12-log_stats.py
"""
from pymongo import MongoClient


def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    total_logs = collection.estimated_document_count()
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")
    status_check = collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
