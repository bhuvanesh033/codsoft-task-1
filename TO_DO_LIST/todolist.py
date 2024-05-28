class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            print(f"Task '{task}' added.")
        else:
            print("Task cannot be empty.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-do List Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
