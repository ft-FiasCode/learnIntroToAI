''' Task 3 - Write a function that takes another function
as input and applies it to each element in a list '''

def apply_to_each(my_list, func):
    result = []
    for item in my_list:
        new_item = func(item)
        result.append(new_item)
    return result

def square(x):
    return x * x

def double(x):
    return x * 2

# A list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# Calling our functions with input another function

print(apply_to_each(numbers, square))

print(apply_to_each(numbers, double)) 

