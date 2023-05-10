# Import libraries
import pandas
from datetime import date

# Import functions from other files
from num_checker import num_checker
from user_input import get_item
from sorting import sort_dictionary
from yes_no_checker import yes_no
from export import export_file

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

# Loop to ask user for item information until user enters "xxx" as item name
while True:
    item_name, weight, cost = get_item()

    # Exit loop if user enters "xxx"
    if item_name == "xxx":
        break

    # Store item information in dictionary
    items[item_name] = {
        "Weight (g)": weight, 
        "Weight (kg)": weight/1000, 
        "Cost": cost, 
        "Unit Price (per kg)": cost/(weight/1000)
    }
    print()

# Sort dictionary by unit price (per kg)
ordered_items = sort_dictionary(items, "Unit Price (per kg)")

# Find best value for budget
best_value = None

for key in ordered_items:
    if ordered_items[key]["Cost"] <= budget:
        best_value = key
        break

# Convert dictionary to Pandas DataFrame for display and export
item_frame = pandas.DataFrame(ordered_items)
item_frame = item_frame.transpose()

# Apply currency formatting to cost and unit price columns
addDollars = ["Cost", "Unit Price (per kg)"]
for varItem in addDollars:
    item_frame[varItem] = item_frame[varItem].apply(currency)

# Printing area
header_text = f"Current budget: {currency(budget)}"

print(header_text)
print("\n")
print(item_frame.to_string())

if best_value != None:
    item_information = ordered_items[best_value]
    footer_text = f"Recommendation: {best_value}, {currency(item_information['Unit Price (per kg)'])} / kg, {item_information['Weight (g)']}g packet costs {currency(item_information['Cost'])}"
    print()
    print(footer_text)

# Export DataFrame to raw text file
file_name = f"{date.today()}.txt"

export_file(item_frame, file_name, header_text, footer_text)