"""
Task 0 - Lockboxes

contains a function to check if all boxes, represented as lists of keys
within a list, can be unlocked.
"""

def canUnlockAll(boxes):
    """
	Checks if all boxes in the list can be unlocked by iterating through
 	the keys in each box.
	
	Parameters:
    boxes (list of list of int): The outer list represents all boxes, 
    while each inner list represents the keys in a single box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

    unlocked = [False] * len(boxes)
    unlocked[0] = True
    stack = [key for key in boxes[0]]

    while stack:
        key = stack.pop()

        if key < len(boxes):
            if not unlocked[key]:
                unlocked[key] = True
                stack.extend(boxes[key])

    return all(unlocked)
