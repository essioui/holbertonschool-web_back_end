#!/usr/bin/env python3
"""
10-update_topics.py changes all topics
"""


def update_topics(mongo_collection, name, topics):
    """
    will be the pymongo collection object
    Args:
        name: (string) will be the school name to update
        topics (list of strings) will be the list of topics
    return: dict
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
