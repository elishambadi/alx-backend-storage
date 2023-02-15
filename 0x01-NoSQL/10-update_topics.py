#!/usr/bin/env python3
"""
MongoDB methods
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics taught in a certain school
    """
    mongo_collection.update({"name": name}, {"$set": {"topics": topics}})
