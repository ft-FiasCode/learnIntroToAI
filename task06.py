# Task 1 - Implement a recursive function to generate fibonacci numbers up to a given limit

# Taking input from user
num = int(input("Enter a number: "))
# Recursive Function
def fibonacci(num):
    if num  == 0: # as the fibonacci series of 0 is 0
        return 0
    elif num == 1: # as the fibonacci of 1 is 0 + 1 = 1
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
for i in range(num):
    print(fibonacci(i), end= " ")

    