#!/usr/bin/env python3
""" this module is used to update a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """update a document in a collection
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
