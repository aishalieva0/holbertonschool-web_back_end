#!/usr/bin/env python3
"""contains schools_by_topic func"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    query = {"topics": topic}
    return mongo_collection.find(query)
