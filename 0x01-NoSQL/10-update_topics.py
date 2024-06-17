#!/usr/bin/env python3
"""module updates som docs"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a collection's document based on the name"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
)
