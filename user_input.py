from string_checker import *
from num_checker import *

def get_item():
    
    # Get item name
    item_name = string_checker("Item name: ")
    if item_name == "xxx":
        return "xxx", None, None

    # Get item info
    weight = num_checker("Weight (grams): ", int)
    cost = num_checker("Price: $", float)

    # return all the info
    return item_name,weight,cost