tasks = []

def add_task():
    name = input("Task name: ")
    category = input("Category: ")
    priority = input("Priority (High/Medium/Low): ")
    tasks.append((name, category, priority))

def show_tasks():
    for t in tasks:
        print("Task:", t[0], "| Category:", t[1], "| Priority:", t[2])

while True:
    print("\n1.Add Task\n2.Show Tasks\n3.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    else:
        break