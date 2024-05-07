#!/usr/bin/env python3
"""contains insert_school func"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
