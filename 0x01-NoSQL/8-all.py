#!/usr/bin/env python3
"""This module is used to list all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """list all documents in a collection
    """
    return mongo_collection.find()


if __name__ == "__main__":
    list_all(mongo_collection)
