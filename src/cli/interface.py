from storage.memory_store import MemoryStore
from cli.validators import validate_task_id, validate_title, validate_description, validate_yes_no

def handle_add_task(store: MemoryStore):
    """Handles adding a new task."""
    title = input("Enter task title: ")
    if not validate_title(title):
        return
    description = input("Enter description (optional): ")
    if not validate_description(description):
        return
    task = store.add_task(title, description)
    print(f"✓ Task #{task.id} \"{task.title}\" added successfully")

def handle_list_tasks(store: MemoryStore):
    """Handles listing all tasks."""
    tasks = store.get_all_tasks()
    if not tasks:
        print("Your task list is empty.")
        return
    print("Your Tasks:")
    complete_count = 0
    for i, task in enumerate(tasks, 1):
        if task.is_complete:
            complete_count += 1
        print(f"{i}. {task}")
    print(f"\nTotal: {len(tasks)} tasks ({complete_count} complete, {len(tasks) - complete_count} incomplete)")

def handle_update_task(store: MemoryStore):
    """Handles updating a task."""
    task_id_str = input("Enter task ID: ")
    task_id = validate_task_id(task_id_str, store)
    if task_id is None:
        return
    task = store.get_task(task_id)
    new_title = input(f"Current title: {task.title}\nNew title (press Enter to keep): ")
    if not new_title:
        new_title = task.title
    elif not validate_title(new_title):
        return
    new_description = input(f"Current description: {task.description}\nNew description: ")
    if not new_description:
        new_description = task.description
    elif not validate_description(new_description):
        return
    store.update_task(task_id, new_title, new_description)
    print(f"✓ Task #{task_id} updated successfully")

def handle_delete_task(store: MemoryStore):
    """Handles deleting a task."""
    task_id_str = input("Enter task ID: ")
    task_id = validate_task_id(task_id_str, store)
    if task_id is None:
        return
    task = store.get_task(task_id)
    answer = input(f"Delete task \"{task.title}\"? (y/n): ")
    if validate_yes_no(answer):
        store.delete_task(task_id)
        print(f"✓ Task #{task_id} deleted successfully")

def handle_toggle_complete(store: MemoryStore):
    """Handles toggling the completion status of a task."""
    task_id_str = input("Enter task ID: ")
    task_id = validate_task_id(task_id_str, store)
    if task_id is None:
        return
    task = store.toggle_complete(task_id)
    status = "complete" if task.is_complete else "incomplete"
    print(f"✓ Task #{task_id} marked as {status}")

def print_main_menu():
    """Prints the main menu."""
    print("\nTodo App - Main Menu")
    print("1. Add task")
    print("2. List tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark complete/incomplete")
    print("6. Exit")
