"""DESCRIPTION: 
    Asks the user for two intergers:
        1. the number of manufactured items
        2. the number of items that the user will pack per box

    The program must compute and print the number of boxes necessary to hold the items.
    This must be a whole number. Note that the last box may be packed with fewer items than
    the other boxes."""

#import math for 'math.ceil' to work
import math

#Get two numbers from users as asked in decription
num_of_items = int(input(f"Enter the number of items: "))
num_of_items_per_box = int(input(f"Enter the number of items per box: "))

#function to find amount of boxes
boxes = math.ceil(num_of_items / num_of_items_per_box)

#print an empty line
print()

#Display results of functions
print(f"For {num_of_items} items, packing {num_of_items_per_box} items in each box, you will need {boxes} boxes.")
