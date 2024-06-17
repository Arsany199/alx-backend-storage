#!/usr/bin/env python3
"""list all docs in a collection"""


def list_all(mongo_collection):
    """function that list all docs in a collection"""
    docs = mongo_collection.find()
    if docs.count() == 0:
        return ([])
    return (docs)
