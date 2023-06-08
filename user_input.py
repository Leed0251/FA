from string_checker import *
from num_checker import *
from get_unit import *

def get_item():
    
    # Get item name
    item_name = not_blank("Item name (or 'xxx' to quit): ", None)
    if item_name == "xxx":
        return "xxx", None, None

    # Get item info
    weight = get_unit("Weight: ")
    cost = num_checker("Price: $", float)

    # return all the info
    return item_name,weight,cost