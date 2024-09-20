from datetime import datetime

# Define Task class with priority feature
class Task:
    def __init__(self, title, description, due_date, priority="Medium"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.priority = priority

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def update_task(self, new_title=None, new_description=None, new_due_date=None, new_priority=None):
        if new_title:
            self.title = new_title
        if new_description:
            self.description = new_description
        if new_due_date:
            self.due_date = new_due_date
        if new_priority:
            self.priority = new_priority

# TaskManager to handle task list operations
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description, due_date, priority="Medium"):
        
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)

    def complete_task(self, index):
        
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def incomplete_task(self, index):
        
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_incomplete()

    def remove_task(self, index):
        
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def update_task(self, index, title=None, description=None, due_date=None, priority=None):
        
        if 0 <= index < len(self.tasks):
            self.tasks[index].update_task(title, description, due_date, priority)

    def list_tasks(self):
        
        if not self.tasks:
            print("\nNo tasks to display.")
        else:
            print("\nTask List:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{i+1}. {task.title} - Due: {task.due_date.date()} - Priority: {task.priority} - Status: {status}")
    
    def list_overdue_tasks(self):
        
        print("\nOverdue Tasks:")
        overdue_found = False
        today = datetime.now().date()
        for i, task in enumerate(self.tasks):
            if task.due_date.date() < today and not task.completed:
                overdue_found = True
                print(f"{i+1}. {task.title} - Due: {task.due_date.date()} - Priority: {task.priority}")
        if not overdue_found:
            print("No overdue tasks.")

def main_menu():
    print("\nTaskMaster Menu:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Mark Task as Incomplete")
    print("4. Remove Task")
    print("5. Update Task")
    print("6. List All Tasks")
    print("7. List Overdue Tasks")
    print("8. Exit")

def add_task_flow(manager):
    
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

    # Choose priority
    priority = input("Enter task priority (Low, Medium, High): ")
    if priority not in ["Low", "Medium", "High"]:
        priority = "Medium"  # default to Medium

    manager.add_task(title, description, due_date, priority)

def complete_task_flow(manager):
    
    manager.list_tasks()
    index = int(input("Enter the number of the task to complete: ")) - 1
    manager.complete_task(index)

def incomplete_task_flow(manager):
    
    manager.list_tasks()
    index = int(input("Enter the number of the task to mark as incomplete: ")) - 1
    manager.incomplete_task(index)

def remove_task_flow(manager):
    
    manager.list_tasks()
    index = int(input("Enter the number of the task to remove: ")) - 1
    manager.remove_task(index)

def update_task_flow(manager):
    
    manager.list_tasks()
    index = int(input("Enter the number of the task to update: ")) - 1
    new_title = input("Enter new title (press Enter to keep current): ") or None
    new_description = input("Enter new description (press Enter to keep current): ") or None
    new_due_date_str = input("Enter new due date (YYYY-MM-DD) (press Enter to keep current): ") or None
    new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d") if new_due_date_str else None
    new_priority = input("Enter new priority (Low, Medium, High) (press Enter to keep current): ") or None
    
    manager.update_task(index, new_title, new_description, new_due_date, new_priority)

def main():
    manager = TaskManager()

    while True:
        main_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_task_flow(manager)
        elif choice == "2":
            complete_task_flow(manager)
        elif choice == "3":
            incomplete_task_flow(manager)
        elif choice == "4":
            remove_task_flow(manager)
        elif choice == "5":
            update_task_flow(manager)
        elif choice == "6":
            manager.list_tasks()
        elif choice == "7":
            manager.list_overdue_tasks()
        elif choice == "8":
            print("Thank you for using TaskMaster!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
