#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks that all the boxes in a list of boxes containing keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    num = len(boxes) ''Gets the length of box ''
    viewed = set([0])
    unviewed_boxes = set(boxes[0]).difference(set([0]))
    while len(unviewed_boxes) > 0:
        Idbox = unviewed_boxes.pop()
        if not Idbox or Idbox >= num or Idbox < 0:
            continue
        if Idbox not in viewed:
            unview_boxes = unviewed_boxes.union(boxes[Idbox])
            viewed.add(Idbox)
    return n == len(viewed)
