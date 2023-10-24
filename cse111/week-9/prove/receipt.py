# Author - Dylan Butterfield, CSE111, 3:15 Class
import csv


def main():
    products_dict = read_dictionary('products.csv', 0)
    print(products_dict)
    with open('request.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            if product_number in products_dict:
                product = products_dict[product_number]
                product_name = product[1]
                product_price = float(product[2])
                total_price = product_price * quantity

                print(f"Product: {product_name}")
                print(f"Requested Quantity: {quantity}")
                print(f"Product Price: {product_price}")
                print(f"Total Price: {total_price}")
                print()
            else:
                print(f"Product with number {product_number} not found.")
                print()


def read_dictionary(products, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename (str): The name of the CSV file to read.
        key_column_index (int): The index of the column to use as the keys in the dictionary.
    
    Returns:
        dict: A compound dictionary that contains the contents of the CSV file.
    """
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


# Call the main function
if __name__ == '__main__':
    main()