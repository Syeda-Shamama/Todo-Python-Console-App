from dataclasses import dataclass, field
from datetime import datetime
import time

@dataclass
class Task:
    """Represents a single task in the todo application."""
    id: int
    title: str
    description: str
    is_complete: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate post-initialization."""
        if not (1 <= len(self.title) <= 100):
            raise ValueError("Title must be between 1 and 100 characters.")
        if self.description and len(self.description) > 500:
            raise ValueError("Description cannot exceed 500 characters.")

    def __str__(self):
        """Return a string representation of the task."""
        status = "[✓]" if self.is_complete else "[ ]"
        return f"{status} #{self.id}: {self.title}"
