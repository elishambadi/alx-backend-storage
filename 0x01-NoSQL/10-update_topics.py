#!/usr/bin/env python3
"""
MongoDB methods
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update the topics taught in a certain school
    """
    filter = {
        name: name
    }
    mongo_collection.update(filter, {$set: {topics: topics}})
