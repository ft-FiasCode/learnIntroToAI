# Task 05 - Text file analyzer 
try:
    with open("text.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
        num_chars = len(content)
        print("Total number of characters are: ", num_chars)

except FileNotFoundError:
    print("file not found")

