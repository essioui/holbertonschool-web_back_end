#!/usr/bin/env python3
"""
11-schools_by_topic.py
"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: collection object
        topic (string) will be topic searched
    return:
    the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
