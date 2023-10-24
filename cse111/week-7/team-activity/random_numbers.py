import random

def main():
    """
    ...
    """
    numbers = [16.2, 75.1, 52.3]

    # Call append_random_numbers() and then print the modified list
    append_random_numbers(numbers)
    print(numbers)

    # Call append_random_numbers() and append 3 random numbers to the list
    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(numbers_list , qty=1):
    """
    Append a random number to a list of numbers.

    Parameters:
        numbers_list (list): A list of existing numbers.
        qty [int]: How many random numbers to append to the the list. Default 1.

    Returns:
        None
    """
    processed = 0

    if qty < 1:
        qty = 1

    while processed < qty:
        rand = random.uniform(0, 100) # Get a random float
        rand = round(rand, 1)
        numbers_list.append(rand) # Add the random float to the list
        processed += 1 # Avoid infinite loop by incrementing the counter

def append_random_words(): # TODO
    # Recap for stretch challenge
    # letters = ["A", "B", "C"]
    # random.choice(letters)
    words_list = [] # TODO
    pass

if __name__ == "__main__":
    main()