''' Task 2 - Create a higher order function that filters
a list of numbers ,returning only the even numbers '''

def custom_filter(function, numbers):
    result = []
    for n in numbers:
        if function(n):
            result.append(n)
    return result

def is_even(n):
    return n % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,10]
evens = custom_filter(is_even,nums)
print("Even Numbers in the list are: ",evens)

