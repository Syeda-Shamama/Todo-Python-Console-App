from typing import Optional
from storage.memory_store import MemoryStore

def validate_task_id(task_id_str: str, store: MemoryStore) -> Optional[int]:
    """Validates the given task ID string."""
    try:
        task_id = int(task_id_str)
        if store.get_task(task_id):
            return task_id
        else:
            print("Error: Task not found.")
            return None
    except ValueError:
        print("Error: Invalid ID. Please enter a number.")
        return None

def validate_title(title: str) -> bool:
    """Validates the task title."""
    if 1 <= len(title) <= 100:
        return True
    print("Error: Title must be between 1 and 100 characters.")
    return False

def validate_description(description: str) -> bool:
    """Validates the task description."""
    if len(description) <= 500:
        return True
    print("Error: Description cannot exceed 500 characters.")
    return False

def validate_yes_no(answer: str) -> bool:
    """Validates a yes/no answer."""
    return answer.lower() in ['y', 'yes']
