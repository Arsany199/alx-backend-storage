#!/usr/bin/env python3
"""model to insert doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """function to insert doc"""
    return (mongo_collection.insert(kwargs))
