#!/usr/bin/env python3
"""contains update_topics func"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    query = {"name": name}
    new_value = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_value)
