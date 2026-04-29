""" utils.py
Helper functions.
"""

def find_by_name(name, items):
    """
    Searches a list of items for a item with a name that matches the provided name.
    
    :param name (string): The name to search for.
    :param items (objects with object.name): The list of items to be searched.

    :returns the found item
    """
    item = [item for item in items if item.name == name]

    if len(item) > 0:
        return item[0]
    
    return None