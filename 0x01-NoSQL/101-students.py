#!/usr/bin/env python3
"""MongoDB Scripts"""

def top_students(mongo_collection):
    """Return students sorted by Avg score"""
    return list(mongo_collection.find().sort([("averageScore", -1)]))
