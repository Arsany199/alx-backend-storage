#!/usr/bin/env python3
"""model that return some topic"""


def schools_by_topic(mongo_collection, topic):
    """function that return a topic"""
    return list(mongo_collection.find({"topics": topic}))
