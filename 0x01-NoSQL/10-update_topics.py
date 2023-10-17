#!/usr/bin/env python3
"""Mongo DB"""

def update_topics(mongo_collection, name, topics):
    """Update Several Topics"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
