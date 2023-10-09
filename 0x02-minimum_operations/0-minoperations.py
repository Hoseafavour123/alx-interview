#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Returns minimum number of operations for text file size to reach n"""
    text = ['H']
    text_copy = text[:]
    operations = 0

    if n > 0:
        for i in range(n):
            if len(text) != n - 1 and len(text + text) < n:
                text.extend(text_copy)
                operations += 2
            if len(text) == n:
                return operations
            text.extend(text_copy)
            text_copy = text[:]
            operations += 1
            if len(text) == n or len(text) > n:
                return operations

    else:
        return 0
