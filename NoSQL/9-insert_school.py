#!/usr/bin/env python3
"""
9-insert_school.py function inserts a new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the collection
    Args:
        mongo_collection: collection object.
        **kwargs (Any): Key-value
    return: the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
