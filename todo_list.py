# Define the to-do list tasks
tasks = []

def view_tasks(tasks):
  # Print the current tasks
  if tasks:
    print("Current tasks:")
    for i, task in enumerate(tasks):
      print(i+1, task)
  else:
    print("No tasks to display.")

def add_task(tasks):
  # Ask the user for a new task and add it to the list
  new_task = input("Enter a new task: ")
  tasks.append(new_task)
  print("Task added to list.")

def remove_task(tasks):
  # Ask the user for the task to remove and remove it from the list
  task_to_remove = int(input("Enter the task to remove: "))
  tasks.pop(task_to_remove - 1)
  print("Task removed from list.")

# Present the user with a list of options
while True:
  print("""
  To-do List Options:
  1. View tasks
  2. Add task
  3. Remove task
  4. Quit
  """)
  choice = input("Enter your choice: ")

  # Choose the appropriate action
  if choice == "1":
    view_tasks(tasks)
  elif choice == "2":
    add_task(tasks)
  elif choice == "3":
    remove_task(tasks)
  elif choice == "4":
    break
  else:
    print("Invalid choice. Try again.")
