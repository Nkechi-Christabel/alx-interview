#!/usr/bin/python3
def canUnlockAll(boxes):
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
