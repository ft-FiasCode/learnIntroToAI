#  Task 2 - Customer Service Call Center
queue = []

# Defining a enqueue function
def enqueue(call):
    queue.append(call)
    print(f"{call} added to the queue. ")

# Defining a dequeue function
def dequeue():
    if not queue:
        print("No calls to attend")
    else:
        call = queue.pop(0)
        print(f"Attending call from {call}")

# Defining a display function
def display():
    if not queue:
        print("No calls in waiting.")
    else:
        print("Current waiting calls: ", queue)

# Testing
"""enqueue("Ali")
enqueue("Sara")
enqueue("Ahmad")
display()

dequeue()
display() """

# Adding a menu system for Customer service call center
while True:
    print("-- Customer Service Call Center --- ")
    print("1. Add a new call (enqueue)")
    print("2. Attend a call (dequeue)")
    print("3. Show waiting calls")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter caller name: ")
        enqueue(name)
    
    elif choice == "2":
        dequeue()

    elif choice == "3":
        display()

    elif choice == "4":
        print("Existing...")
        break
    else:
        print("Invalid choice! Please try again.")

