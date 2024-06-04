#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        cur_key = keys.pop()
        for key in boxes[cur_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)
