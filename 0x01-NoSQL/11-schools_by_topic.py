#!/usr/bin/env python3
"""Mongo DB"""


def schools_by_topic(mongo_collection, topic):
    """Search School by topic"""
    return list(mongo_collection.find({"topics": topic}))
