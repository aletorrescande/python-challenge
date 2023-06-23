"""
This Python Script analyses the data from menu_data.csv and sales_data.csv to analyse business performance by menu items.
The results are the quantity sold, revenue, cost and profit for each type of product with the data provided from files.

"""

# Import pathlib to set the file path and csv library to read in the file:
from pathlib import Path
import csv
# Set the file Path:
csvpath = Path('./Resources/menu_data.csv')
csvpath

# Initialize list to hold the contents of the menu_data csv file
menu = []
# Open the input path (csvpath) as a file object 
with open(csvpath, 'r') as csvmenu:
    # Pass csv file to the csv.reader() function and use '," as a separator and return the csvreader object
    csvreader = csv.reader(csvmenu, delimiter=",")
    # Skip the header 
    csv_header = next(csvreader)
    # Loop over the rows and append every row to the `menu` list object
    for row in csvreader:
        menu.append(row)
        
# Set the file Path for sales csv:
csvpath_sales = Path('./Resources/sales_data.csv')
csvpath_sales

# Initialize list to hold the contents of the csv file
sales = []
# Open the input path (csvpath) as a file object 
with open(csvpath_sales , 'r') as csvsales:
    # Pass csv file to the csv.reader() function and use '," as a separator and return the csvreader object
    csvreader = csv.reader(csvsales, delimiter=",")
    # Skip the header 
    csv_header = next(csvreader)
    # Loop over the rows and add conent to menu list
    for row in csvreader:
        # append every row of the sales data to a new `sales` list object. 
        sales.append(row)
        
# Initialize an empty dictionary to hold the future aggregated per-product results.
report = {}
    
for row in sales:
    # set variables for quantity and menu item
    quantity = int(row[3])
    sales_item = row[4]
    # check if sales_item is included in report dictionary 
    if sales_item not in report.keys():
        report[sales_item] = {"01-count":0, "02-revenue":0, "03-cogs": 0, "04-profit": 0}
        # Create a nested loop by looping through every record in `menu`.
    for row in menu:
        #set columns needed of the menu data to their own variables:
        item = row[0]
        price = float(row[3])
        cost = int(row[4])
        profit = price - cost
        # Calculate the metrics per item (total quantity, total revenue, total cost and profit)
        # Use conditional to match sales_item from sales to items in menu list
        if sales_item == item:
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        else:
            print(f"{sales_item} does not equal {item}! NO MATCH!")


print(report)
## T.A. Justine Cho helped me nest the loop (for row in menu) to the loop for row in sales.

# Create a text file to hold Financial Analysis results
# Set the output file path
ramen_results_path = 'ramen_results.txt'

with open(ramen_results_path, 'w') as file:
    file.write(f"{report}")
    
