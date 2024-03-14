#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    num = len(boxes)
    viewed_box = set([0])
    unviewed = set(boxes[0]).difference(set([0]))
    while len(unviewed) > 0:
        IdBox = unviewed.pop()
        if not IdBox or IdBox >= num or IdBox < 0:
            continue
        if IdBox not in viewed_box:
            unviewed = unviewed.union(boxes[IdBox])
            viewed_box.add(IdBox)
    return num == len(viewed_box)
