# Todo App - Initial Specification
**Spec ID:** 001  
**Created:** 2025-12-13  
**Status:** Active  
**Phase:** I - In-Memory Console App

## 1. Overview
A command-line todo application that manages tasks in memory during runtime. Tasks are lost when the application exits (no persistence in Phase I).

## 2. User Stories

### US-001: Add Task
**As a** user  
**I want to** add a new task with a title and description  
**So that** I can track things I need to do

**Acceptance Criteria:**
- User is prompted for task title (required, 1-100 chars)
- User is prompted for task description (optional, max 500 chars)
- Task is assigned a unique auto-incrementing ID
- Task is created with status "incomplete" by default
- Confirmation message shows task ID and title
- Invalid input shows error and re-prompts

**Example Interaction:**
```
> add
Enter task title: Buy groceries
Enter description (optional): Milk, eggs, bread
✓ Task #1 "Buy groceries" added successfully
```

### US-002: List Tasks
**As a** user  
**I want to** see all my tasks  
**So that** I know what needs to be done

**Acceptance Criteria:**
- Shows all tasks with ID, title, and status
- Complete tasks marked with [✓], incomplete with [ ]
- Tasks numbered sequentially
- Empty list shows friendly message
- Description shown on demand (optional)

**Example Output:**
```
Your Tasks:
1. [ ] Buy groceries
2. [✓] Call dentist
3. [ ] Finish project report

Total: 3 tasks (1 complete, 2 incomplete)
```

### US-003: Update Task
**As a** user  
**I want to** edit task title and description  
**So that** I can correct mistakes or add details

**Acceptance Criteria:**
- User provides task ID to update
- User can update title, description, or both
- Original values shown as defaults
- Invalid ID shows error message
- Confirmation shows updated task

**Example Interaction:**
```
> update
Enter task ID: 1
Current title: Buy groceries
New title (press Enter to keep): Buy groceries and snacks
Current description: Milk, eggs, bread
New description: Milk, eggs, bread, chips
✓ Task #1 updated successfully
```

### US-004: Delete Task
**As a** user  
**I want to** remove a task  
**So that** I can clean up completed or cancelled items

**Acceptance Criteria:**
- User provides task ID to delete
- Confirmation prompt before deletion (safety check)
- Task removed from list
- Invalid ID shows error message
- Remaining tasks retain their IDs (no renumbering)

**Example Interaction:**
```
> delete
Enter task ID: 2
Delete task "Call dentist"? (y/n): y
✓ Task #2 deleted successfully
```

### US-005: Mark Complete/Incomplete
**As a** user  
**I want to** toggle task completion status  
**So that** I can track my progress

**Acceptance Criteria:**
- User provides task ID
- Status toggles: incomplete → complete or complete → incomplete
- Visual confirmation of new status
- Invalid ID shows error message

**Example Interaction:**
```
> complete
Enter task ID: 1
✓ Task #1 marked as complete

> incomplete
Enter task ID: 1
✓ Task #1 marked as incomplete
```

## 3. Data Model

### Task Class
```python
class Task:
    id: int              # Auto-incrementing, starts at 1
    title: str           # Required, 1-100 characters
    description: str     # Optional, max 500 characters
    is_complete: bool    # Default: False
    created_at: datetime # Auto-set on creation
```

### Storage Manager
```python
class MemoryStore:
    tasks: list[Task]    # In-memory list of all tasks
    next_id: int         # Counter for task IDs
```

## 4. Command Structure

### Main Menu
```
Todo App - Main Menu
1. Add task
2. List tasks
3. Update task
4. Delete task
5. Mark complete/incomplete
6. Exit

Enter choice (1-6):
```

### Alternative: Direct Commands (pick one approach)
```
Commands: add, list, update, delete, complete, incomplete, exit
> 
```

## 5. Technical Architecture

### Project Structure
```
src/
├── __init__.py
├── main.py              # Entry point, main loop
├── models/
│   ├── __init__.py
│   └── task.py          # Task class definition
├── storage/
│   ├── __init__.py
│   └── memory_store.py  # MemoryStore class
└── cli/
    ├── __init__.py
    ├── interface.py     # Menu/command handling
    └── validators.py    # Input validation
```

### Key Classes & Responsibilities

**Task (models/task.py)**
- Data class for task properties
- Validation logic for title/description length
- String representation for display

**MemoryStore (storage/memory_store.py)**
- CRUD operations: add(), get(), update(), delete()
- Task ID generation
- List filtering (all, complete, incomplete)

**CLI Interface (cli/interface.py)**
- Main menu loop
- User input handling
- Display formatting
- Error message presentation

**Validators (cli/validators.py)**
- Title validation (1-100 chars)
- Description validation (max 500 chars)
- ID validation (positive integer, exists)
- Yes/no confirmation validation

## 6. Non-Functional Requirements

### Error Handling
- Invalid input: Show clear error, allow retry
- Task not found: "Error: Task #X not found"
- Empty input (where required): "Error: Title cannot be empty"
- No crashes on any user input

### User Experience
- Clear prompts with examples
- Confirmation messages after actions
- Graceful exit on "exit" command
- No technical jargon in user-facing messages

### Code Quality
- Type hints on all functions
- Docstrings (Google style)
- PEP 8 compliant
- Unit testable structure

## 7. Success Criteria

✅ **Feature Complete:**
- All 5 user stories implemented and working
- No runtime errors on valid inputs
- Graceful error handling on invalid inputs

✅ **Code Quality:**
- Passes PEP 8 linting
- All functions have type hints and docstrings
- Clear separation of concerns (models/storage/cli)

✅ **User Experience:**
- Intuitive command flow
- Helpful error messages
- Clean, readable output

## 8. Out of Scope (Future Phases)

- ❌ File persistence
- ❌ Database storage
- ❌ Task priorities
- ❌ Due dates
- ❌ Categories/tags
- ❌ Search functionality
- ❌ Task sorting

## 9. Testing Checklist

### Manual Tests
- [ ] Add task with valid title and description
- [ ] Add task with title only (no description)
- [ ] Add task with empty title (should fail)
- [ ] Add task with 101-char title (should fail)
- [ ] List tasks when empty
- [ ] List tasks with multiple tasks
- [ ] Update existing task
- [ ] Update non-existent task (should fail)
- [ ] Delete existing task with confirmation
- [ ] Delete task - decline confirmation
- [ ] Mark task as complete
- [ ] Mark task as incomplete
- [ ] Complete non-existent task (should fail)
- [ ] Exit application cleanly

## 10. Dependencies
- Python 3.13+
- UV (package manager)
- Standard library only (no external packages required)

## 11. Approval & Sign-off

**Specification Author:** [Your Name]  
**Approved By:** Self (Phase I learning project)  
**Approval Date:** 2025-12-13  
**Ready for Implementation:** ✓ Yes