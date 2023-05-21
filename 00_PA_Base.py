# Import libraries
import pandas
from datetime import date

# Import functions from other files
from num_checker import num_checker
from user_input import get_item
from sorting import sort_dictionary
from export import export_file
from get_unit import get_unit
from string_checker import *

# Define function to format currency
def currency(x):
    return f'${x:.2f}'

# Main routine

show_instructions = yes_no("Do you want to read the instructions? ")

# Open and read file "instructions.txt" to the user
if show_instructions == "yes":
    print()
    f = open('instructions.txt', 'r')
    print(f.read())
    f.close()
print()

# Initialize empty dictionary to store item information
items = {}

# Prompt user for budget
budget = num_checker("What is your current budget? $", float)

item_name = ""
print()

# Loop to ask user for item information until user enters "xxx" as item name
while True:
    item_name, weight, cost = get_item()

    # Exit loop if user enters "xxx"
    if item_name == "xxx":
        break

    # Store item information in dictionary
    items[item_name] = {
        "Weight (g/ml)": weight, 
        "Weight (kg/l)": weight/1000, 
        "Cost": cost, 
        "Unit Price (per kg/l)": cost/(weight/1000)
    }
    print()

# Sort dictionary by unit price (per kg/l)
ordered_items = sort_dictionary(items, "Unit Price (per kg/l)")

# Find best value for ybudget
best_value = None

for key in ordered_items:
    if ordered_items[key]["Cost"] <= budget:
        best_value = key
        break

# Convert dictionary to Pandas DataFrame for display and export
item_frame = pandas.DataFrame(ordered_items)
item_frame = item_frame.transpose()

# Apply currency formatting to cost and unit price columns
addDollars = ["Cost", "Unit Price (per kg/l)"]
for varItem in addDollars:
    item_frame[varItem] = item_frame[varItem].apply(currency)

# Printing area
header_text = f"Current budget: {currency(budget)}"
footer_text = ""

if best_value != None:
    item_information = ordered_items[best_value]
    footer_text = f"Recommendation: {best_value}, {currency(item_information['Unit Price (per kg/l)'])} / kg, {item_information['Weight (g/ml)']}g product costs {currency(item_information['Cost'])}"
else:
    for key in sort_dictionary(items, "Cost"):
        cheapest = key
        break
    for key in sort_dictionary(items, "Unit Price (per kg/l)"):
        best_value = key
        break
    footer_text = f"There are no items that fit in your budget.\n\n\
        Cheapest: {cheapest}, {currency(ordered_items[cheapest]['Unit Price (per kg/l)'])} / (kg/l), {ordered_items[cheapest]['Weight (g/ml)']}g product costs {currency(ordered_items[cheapest]['Cost'])}\n\
        Best Value: {best_value}, {currency(ordered_items[best_value]['Unit Price (per kg/l)'])} / (kg/l), {ordered_items[best_value]['Weight (g/ml)']}g product costs {currency(ordered_items[best_value]['Cost'])}"

print(header_text)
print("\n")
print(item_frame.to_string())
print()
print(footer_text)

# Export DataFrame to raw text file

saving = yes_no("Would you like to save your results? (yes/no) ")

if saving == "yes":

    file_name, replaced = replace_blank('\nWhat do you want your file to be called? ', date.today())
    file_name = f"{file_name}.txt"

    if replaced:
        print(f"\nFile name was left blank and has been named \x1B[36m{file_name}\x1B[0m\n")

    export_file(item_frame, file_name, header_text, footer_text)