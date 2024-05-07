#!/usr/bin/env python3
"""contains list_all func"""
import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection"""
    list = mongo_collection.list_collections()
    if list:
        return list
    else:
        return []
