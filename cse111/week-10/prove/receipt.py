# Author - Dylan Butterfield, CSE111, 3:15 Class
import csv
from datetime import datetime

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        with open('request.csv', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first line
            ordered_items = []
            subtotal = 0
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                if product_number in products_dict:
                    product = products_dict[product_number]
                    product_name = product[1]
                    product_price = float(product[2])
                    total_price = product_price * quantity

                    ordered_items.append(f"{product_name}: {quantity} @ {product_price}")
                    subtotal += total_price
                else:
                    print(f"Product with number {product_number} not found.")

            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax

            print_receipt(ordered_items, len(ordered_items), subtotal, sales_tax, total)
            print_current_datetime()
            print("Thank you for shopping at the Inkom Emporium.")
    except FileNotFoundError:
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'")
    except PermissionError:
        print("Error: permission denied")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n'{e.args[0]}'")

def print_receipt(items, num_items, subtotal, sales_tax, total):
    print("Inkom Emporium\n")
    for item in items:
        print(item)
    print()
    print(f"Number of Items: {num_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}\n")

def print_current_datetime():
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

def read_dictionary(products, key_column_index):
    compound_dict = {
        "D150": ["D150", "1 gallon milk", 2.85],
        "D083": ["D083", "1 cup yogurt", 0.75],
        "D215": ["D215", "1 lb cheddar cheese", 3.35],
        "P019": ["P019", "iceberg lettuce", 1.15],
        "P020": ["P020", "green leaf lettuce", 1.79],
        "P021": ["P021", "butterhead lettuce", 1.83],
        "P025": ["P025", "8 oz arugula", 2.19],
        "P143": ["P143", "1 lb baby carrots", 1.39],
        "W231": ["W231", "32 oz granola", 3.21],
        "W112": ["W112", "wheat bread", 2.55],
        "C013": ["C013", "twix candy bar", 0.85],
        "H001": ["H001", "8 rolls toilet tissue", 6.45],
        "H014": ["H014", "facial tissue", 2.49],
        "H020": ["H020", "aluminum foil", 2.39],
        "H021": ["H021", "12 oz dish soap", 3.19],
        "H025": ["H025", "toilet cleaner", 4.50]
    }

    with open(products, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row

    return compound_dict

if __name__ == '__main__':
    main()
