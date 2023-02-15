#!/usr/bin/env python3
"""
Mongo DB Methods
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new doc into collection
    Args: collection, kwargs of data for document
    return: id of new document
    """
    x = mongo_collection.insert(kwargs)
    return x.inserted_id
