from string_checker import *
from num_checker import *
from get_unit import *

def get_item(current_items):
    
    # Get item name
    item_name = not_blank("Item name (or 'xxx' to quit): ", None)

    if item_name in current_items:
        user_response = yes_no("Item in list, would you like to replace it? ")

        if user_response == "no":
            return get_item(current_items)

    if item_name == "xxx":
        return "xxx", None, None

    # Get item info
    weight = get_unit("Weight: ")
    cost = num_checker("Price: $", float)
    print()

    # return all the info
    return item_name, weight,cost