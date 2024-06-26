#!/usr/bin/env python3
"""model that lists stds with avg score"""


def top_students(mongo_collection):
    """returns all students sorted in average score"""
    students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return (students)
