print("Welcome to To-Do List\n")

tasks = []

for i in range(1, 4):
    task = input(f"Enter task {i}: ")
    tasks.append(task)

print("\nYour To-Do List:")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
