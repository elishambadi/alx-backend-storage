#!/usr/bin/env python3
"""Mongo DB"""

def list_all(mongo_collection):
    """List all records of collection"""
    return list(mongo_collection.find())
