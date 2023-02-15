#!/usr/bin/python3
"""
MongoDB methods
"""
def list_all(mongo_collection):
    """
    List all documents in the given collection
    Args: collection from MongoDB
    Return: array of documents
    """
    return [doc for doc in mongo_collection.find()]
