#!/usr/bin/env python3
"""contains list_all func"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    list = mongo_collection.find()
    if list:
        return list
    else:
        return []
