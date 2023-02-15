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
    doc = {} # uses a doc to store the data
    for k, v in kwargs.items():
        doc.update(k, v)

    return mongo_collection.insert(doc).inserted_id
