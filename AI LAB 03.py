# Task 3 - Browser History Tracker
# Creating a empty stack
history = []

# push a new URL when visited
def visit_url(url):
    history.append(url)
    print(f"Visited: {url}")

# pop (go back) to the previous URL
def go_back():
    if len(history) > 1:
        history.pop()
        print(f"Back to: {history[-1]}")
    elif history:
        print("Only one page in history, cant go back.")
    else:
        print("No history available.")

# Peek at current page
def current_page():
    if history:
        print(f"Current page: {history[-1]}")
    else:
        print("No page currently open.")

# Show history in reverse order (most recent website first)
def show_history():
    if history:
        print("\nBrowser History (most recent first):")
        for url in reversed(history):
            print(url)
    else:
        print("History is empty")

# Testing the code 
visit_url("google.com")
visit_url("uetmardan.edu.pk")
visit_url("github.com")

current_page()
go_back()
current_page()

show_history()
