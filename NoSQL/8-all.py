#!/usr/bin/env python3
"""
list_all: function .
"""

from typing import List, Dict
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (Collection): collection object.

    Returns:
        List[Dict]: A list of all documents in the collection.
        Returns an empty list if no documents are present.
    """
    documents = list(mongo_collection.find())
    return documents
