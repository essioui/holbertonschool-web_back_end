#!/usr/bin/env python3
"""Print info from nginx logs"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # عدد المستندات في المجموعة
    print(f"{collection.estimated_document_count()} logs")

    # حساب عدد المستندات لكل نوع من الطرق
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    # حساب عدد المستندات التي تحتوي على method=GET و path=/status
    check_get = collection.count_documents({'method': 'GET', 'path': "/status"})
    print(f"{check_get} status check")
