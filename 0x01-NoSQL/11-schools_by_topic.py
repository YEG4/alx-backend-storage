#!/usr/bin/env python3
""" this module is used to list doucments for a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """this function returns the list of doucments that match a specific topic

    Args:
        mongo_collection (pymongo object): collection to search in
        topic (string):  a string to search for
    """
    return mongo_collection.find({"topics": topic})
