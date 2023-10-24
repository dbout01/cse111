# Author - Dylan Butterfield, CSE 111, 3:15PM Class

import random  # <- global


def main():
    make_sentence(0, "past")


# 1. Return a randomly chosen determiner based on quantity
def get_determiner(quantity):  # <- parameter
    if quantity == 1:
        words = ["a", "one", "the"]  # <- arguments
    else:
        words = ["some", "many", "the"]
    return random.choice(words)


# 2. Return a randomly chosen noun based on quantity
def get_noun(quantity):  # <- parameter
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",  # <- arguments
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)


# 3. Return a randomly chosen verb based on quantity and tense
def get_verb(quantity, tense):  # <- parameter
    if tense == "past":
        if quantity == 1:
            words = ["laughed", "ate", "drank",  # <- arguments
                     "ran", "walked", "thought", "wrote"]
        else:
            words = ["laughed", "ate", "drank",
                     "ran", "walked", "thought", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["laughs", "eats", "drinks",
                     "runs", "walks", "thinks", "writes"]
        else:
            words = ["laugh", "eat", "drink", "run", "walk", "think", "write"]
    elif tense == "future":
        if quantity == 1:
            words = ["will laugh", "will eat", "will drink",
                     "will run", "will walk", "will think", "will write"]
        else:
            words = ["will laugh", "will eat", "will drink",
                     "will run", "will walk", "will think", "will write"]
    else:
        words = []
    return random.choice(words)


# 4. Build and return a sentence - helps create sentence
def make_sentence():  # <- parameter
    quantity = random.choice([1, 2])  # <- arguments
    noun = get_noun(quantity)
    verb_tense = random.choice(["past", "present", "future"])
    verb = get_verb(quantity, verb_tense)
    determiner = get_determiner(quantity)
    sentence = (f"{determiner.capitalize()} {noun} {verb}.")
    return sentence


# 5. Generates and prints six sentences
def main():  # <- parameter
    for i in range(6):
        print(make_sentence())


# 6. gets a preposition to use
def get_preposition(quantity):  # <- parameter
    if quantity == 1:
        words = ["about", "above", "across", "after", "along",  # <- arguments
                 "around", "at", "before", "behind", "below",
                 "beyond", "by", "despite", "except", "for",
                 "from", "in", "into", "near", "of",
                 "off", "on", "onto", "out", "over",
                 "past", "to", "under", "with", "without"]
    return random.choice(words)


# 7. builds a prepositional phrase
def get_prepositional_phrase(quantity):  # <- parameter
    get_preposition()
    get_determiner(quantity)
    get_noun(quantity)
    return '[prepositional phrase]'


# 8. Allows main to be called so 6 results can be printed
if __name__ == '__main__':
    main()


# CODE MAP
"""
1. Return a randomly chosen determiner based on quantity
2. Return a randomly chosen noun based on quantity
3. Return a randomly chosen verb based on quantity and tense
4. Build and return a sentence - helps create sentence
5. Generates and prints six sentence
6. Gets a preposition to use
7. Builds a prepositional phrase
8. Allows main to be called so 6 results can be printed
"""
