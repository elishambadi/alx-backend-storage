#!/usr/bin/env python3
"""Mongo DB"""

def insert_school(mongo_collection, **kwargs):
    """Insert based on Kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
