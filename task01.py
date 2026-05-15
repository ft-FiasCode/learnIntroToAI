# Task 1 - Online Shopping Cart System

# Creating a list 
shopping_cart = ['mobile phone', 'laptop', 'milk', 'sugar' , 'rice',
 'water bottle', 'power bank' , 'daal', 'body spray' 'perfume', 'tea', 'cooking oil']

# user input to add item into shopping cart
item = input("Enter item to add: ")
shopping_cart.append(item)

print(shopping_cart)

# Adding item at a specific index
shopping_cart.insert(0, 'Chicken Sausages')
print(shopping_cart)

# Removing an item by name
shopping_cart.remove('water bottle')


# Removing item by index
removed_item = shopping_cart.pop(0)
print("\n The removed item is: ", removed_item)

# Displaying the items 
print("\n Shopping Cart Items: ")
for item in shopping_cart:
    print("-", item)

# Displaying total count
print("\nTotal items in cart: ", len(shopping_cart))
