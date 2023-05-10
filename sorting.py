from collections import OrderedDict
from operator import getitem

def sort_dictionary(dict, key):
    # Use lambda method to sort dictionary
    ordered_items = OrderedDict(sorted(dict.items(),
    key = lambda x: getitem(x[1], key)))

    return ordered_items
    