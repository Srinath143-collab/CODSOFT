import os
import json
from datetime import datetime

# Function to load existing to-do lists from a JSON file
def load_lists():
    if os.path.exists("todo_lists.json"):
        with open("todo_lists.json", "r") as file:
            return json.load(file)
    else:
        return {}

# Function to save to-do lists to a JSON file
def save_lists(lists):
    with open("todo_lists.json", "w") as file:
        json.dump(lists, file, indent=4)

# Function to display available lists
def display_lists(lists):
    print("Available lists:")
    for list_name in lists:
        print("-", list_name)

# Function to create a new to-do list
def create_list(lists):
    list_name = input("Enter the name of the new list: ")
    if list_name not in lists:
        lists[list_name] = []
        print("New list created successfully!")
    else:
        print("List with the same name already exists.")

# Function to add a task to a to-do list
def add_task(lists):
    list_name = input("Enter the name of the list: ")
    if list_name in lists:
        task = input("Enter the task: ")
        lists[list_name].append({"task": task, "created_at": str(datetime.now())})
        print("Task added successfully!")
    else:
        print("List does not exist.")

# Function to display tasks in a to-do list
def display_tasks(lists):
    list_name = input("Enter the name of the list: ")
    if list_name in lists:
        print(f"Tasks in {list_name}:")
        for idx, task in enumerate(lists[list_name]):
            print(f"{idx + 1}. {task['task']} (Created at: {task['created_at']})")
    else:
        print("List does not exist.")

# Main function
def main():
    lists = load_lists()
    
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Display available lists")
        print("2. Create a new list")
        print("3. Add a task to a list")
        print("4. Display tasks in a list")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_lists(lists)
        elif choice == "2":
            create_list(lists)
        elif choice == "3":
            add_task(lists)
        elif choice == "4":
            display_tasks(lists)
        elif choice == "5":
            save_lists(lists)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
