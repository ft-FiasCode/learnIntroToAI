# Task 1 - Event Registration System
# Create an empty dictionary
participants = {}

while True:
    name = input("Please enter your name: ")
    email = input("Pease enter your email: ")

    try:
        if email in participants:
            raise Exception("Email already registered! Please use another email")
        participants[email] = name
        print(f"{name} registered successfully!")


    except Exception as e:
        print(e)

    more = input("Do you want to add another participant? (yes/no): ").lower()
    if more != "yes":
        break

print("\nAll Registered Participants:")
for email, name in participants.items():
    print(f"Name: {name}, Email: {email}")

print("\nTotal Number of registered Participants", len(participants))
