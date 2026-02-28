# ============================================================
# TASK 1 - TO-DO LIST APPLICATION
# CodSoft Python Programming Internship
# ============================================================

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n  📋 No tasks found! Add some tasks to get started.\n")
        return
    print("\n" + "=" * 55)
    print(f"  {'#':<4} {'Status':<10} {'Task':<25} {'Added On'}")
    print("=" * 55)
    for i, task in enumerate(tasks, 1):
        status = "✅ Done  " if task["completed"] else "⏳ Pending"
        print(f"  {i:<4} {status:<10} {task['title']:<25} {task['date']}")
    print("=" * 55 + "\n")

def add_task(tasks):
    """Add a new task."""
    title = input("  Enter task description: ").strip()
    if not title:
        print("  ⚠️  Task cannot be empty!")
        return
    task = {
        "title": title,
        "completed": False,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"  ✅ Task '{title}' added successfully!")

def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_title = input(f"  Enter new description (current: '{tasks[num-1]['title']}'): ").strip()
            if new_title:
                tasks[num-1]["title"] = new_title
                save_tasks(tasks)
                print("  ✅ Task updated successfully!")
            else:
                print("  ⚠️  Task description cannot be empty!")
        else:
            print("  ⚠️  Invalid task number!")
    except ValueError:
        print("  ⚠️  Please enter a valid number!")

def mark_complete(tasks):
    """Mark a task as complete or incomplete."""
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to toggle completion: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["completed"] = not tasks[num-1]["completed"]
            status = "completed" if tasks[num-1]["completed"] else "marked as pending"
            save_tasks(tasks)
            print(f"  ✅ Task '{tasks[num-1]['title']}' {status}!")
        else:
            print("  ⚠️  Invalid task number!")
    except ValueError:
        print("  ⚠️  Please enter a valid number!")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  🗑️  Task '{removed['title']}' deleted successfully!")
        else:
            print("  ⚠️  Invalid task number!")
    except ValueError:
        print("  ⚠️  Please enter a valid number!")

def main():
    print("\n" + "🌟" * 20)
    print("      📝  TO-DO LIST APPLICATION")
    print("🌟" * 20)

    tasks = load_tasks()

    while True:
        print("\n  ---- MENU ----")
        print("  1. View All Tasks")
        print("  2. Add Task")
        print("  3. Update Task")
        print("  4. Mark Task Complete/Incomplete")
        print("  5. Delete Task")
        print("  6. Exit")
        print()

        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("\n  👋 Goodbye! Stay productive!\n")
            break
        else:
            print("  ⚠️  Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
