# Import necessary functions and modules

import pandas
from datetime import *

from num_checker import * 
from user_input import *
from sorting import *
from export import *
from string_checker import *

# Define a function to format currency

def currency(x):
    return f'${x:.2f}'

# Prompt the user to determine if they want to read the instructions

show_instructions = yes_no("Do you want to read the instructions? ")

if show_instructions == "yes":
    # Display the instructions if requested
    f = open('README.txt', 'r')
    print("\x1B[0m")
    print(f.read())
    f.close()
print()

items = {}

# Prompt the user to enter their budget
budget = num_checker("What is your current budget? $", float)

item_name = ""

# Prompt the user to enter item details until they enter 'xxx'
while True:
    item_name, weight, cost = get_item(items)

    # Exit the loop if 'xxx' is entered
    if item_name == "xxx":
        break

    # Add the item details to the items dictionary
    items[item_name] = {
        "Weight (g/ml)": weight, 
        "Weight (kg/l)": weight/1000, 
        "Cost": cost, 
        "Unit Price (per kg/l)": cost/(weight/1000)
    }

if len(items) == 0:
    exit()

# Sort the items dictionary by "Unit Price (per kg/l)"
ordered_items = sort_dictionary(items, "Unit Price (per kg/l)")

# Find the first item that fits within the budget
best_value = None
for key in ordered_items:
    if ordered_items[key]["Cost"] <= budget:
        best_value = key
        break

# Convert the items dictionary to a pandas DataFrame
item_frame = pandas.DataFrame(ordered_items)
item_frame = item_frame.transpose()

# Format the "Cost" and "Unit Price (per kg/l)" columns as currency
addDollars = ["Cost", "Unit Price (per kg/l)"]
for varItem in addDollars:
    item_frame[varItem] = item_frame[varItem].apply(currency)

header_text = f"Current budget: {currency(budget)}"
footer_text = ""

# Create the header and footer text for displaying recommendations
if best_value != None:
    item_information = ordered_items[best_value]
    footer_text = f"Recommendation: {best_value}, {currency(item_information['Unit Price (per kg/l)'])} / kg, {item_information['Weight (g/ml)']}g product costs {currency(item_information['Cost'])}"
else:
    cheapest = next(iter(sort_dictionary(items, "Cost")))
    best_value = next(iter(sort_dictionary(items, "Unit Price (per kg/l)")))
    footer_text = f"There are no items that fit in your budget.\n\n\
        Cheapest: {cheapest}, {currency(ordered_items[cheapest]['Unit Price (per kg/l)'])} / (kg/l), {ordered_items[cheapest]['Weight (g/ml)']}g product costs {currency(ordered_items[cheapest]['Cost'])}\n\
        Best Value: {best_value}, {currency(ordered_items[best_value]['Unit Price (per kg/l)'])} / (kg/l), {ordered_items[best_value]['Weight (g/ml)']}g product costs {currency(ordered_items[best_value]['Cost'])}"

# Display the header, item frame, and footer text
print("\x1B[0m")
print(header_text)
print("\n")
print(item_frame.to_string())
print()
print(footer_text)
print()

# Prompt the user to save the results and export them to a file if desired
saving = yes_no("Would you like to save your results? (yes / no) ")

if saving == "yes":
    file_name, replaced = not_blank('\nWhat do you want your file to be called? ', date.today())
    file_name = f"{file_name}.txt"

    print("\x1B[0m")
    if replaced:
        print(f"\nFile name was left blank and has been named \x1B[36m{file_name}\x1B[0m\n")

    export_file(item_frame, file_name, header_text, footer_text)