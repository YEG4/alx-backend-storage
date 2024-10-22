#!/usr/bin/env python3
"""This module is used to insert a document in a collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert a document in a collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
