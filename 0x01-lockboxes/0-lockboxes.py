#!/usr/bin/python3
"""
This module determines if all the boxes can be opened or not.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened using the keys contained in them.

    Parameters:
    - boxes (list of lists): A list of lists where each inner list represents
      the keys contained in a box.

    The first box, boxes[0], is unlocked initially.

    Returns:
    - bool: True if all boxes can be opened using the keys contained in them,
    otherwise False.

    If the input list is empty, returns False.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    keys = set(boxes[0])
    visited = {0}

    while keys:
        new_keys = set()
        for key in keys:
            if key < num_boxes and key not in visited:
                visited.add(key)
                new_keys.update(boxes[key])
        keys = new_keys - visited

    return len(visited) == num_boxes
