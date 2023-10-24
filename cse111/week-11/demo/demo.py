numbers = [1, 2, 3, 4]

print(numbers)

def do_to_all_items(nums, functions):
    for func in functions:
        for i, num in enumerate(nums):
            nums[i] = func(num)    

def divide(num):
    return num / 5

def add(num):
    return num + 10

def sqr(num):
    return num ** 2

def multiply(num):
    return num * 74

do_to_all_items(numbers, [sqr, multiply, add, divide])

print(numbers)