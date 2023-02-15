#!/usr/bin/env python3
"""
Mongo DB methods
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return schools matching a given topic
    """
    return mongo_collection.find({"topic": topic})
