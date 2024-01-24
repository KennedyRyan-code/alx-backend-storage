#!/usr/bin/env python3
"""
a function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    list docs in mongodb collection

    """
    cursor = mongo_collection.find()

    docs = list(cursor)
    return docs
