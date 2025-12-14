from typing import List, Optional
from models.task import Task

class MemoryStore:
    """Manages tasks in memory."""

    def __init__(self):
        """Initializes the memory store."""
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str) -> Task:
        """Adds a new task to the store."""
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Gets a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """Gets all tasks."""
        return self.tasks

    def update_task(self, task_id: int, title: str, description: str) -> Optional[Task]:
        """Updates a task."""
        task = self.get_task(task_id)
        if task:
            task.title = title
            task.description = description
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def toggle_complete(self, task_id: int) -> Optional[Task]:
        """Toggles the completion status of a task."""
        task = self.get_task(task_id)
        if task:
            task.is_complete = not task.is_complete
            return task
        return None
