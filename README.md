# Todo Console Application

This is a simple, in-memory command-line todo application written in Python.

## Features

- Add, list, update, and delete tasks.
- Mark tasks as complete or incomplete.
- View task details (title, description, status, created date) on demand.
- All tasks are stored in memory and are lost when the application exits.

## Requirements

- Python 3.13+

## How to Run

1. Navigate to the `src` directory:

    ```bash
    cd src
    ```

2. Run the application:

    ```bash
    python main.py
    ```

> **Note:** The application must be run from inside the `src/` directory. Running it from the project root will cause import errors.

## Commands

- **1. Add task**: Add a new task with a title and optional description.
- **2. List tasks**: View all tasks. After listing, enter a task ID to see its full details.
- **3. Update task**: Edit the title and description of an existing task.
- **4. Delete task**: Remove a task from the list (with confirmation).
- **5. Mark complete/incomplete**: Toggle the completion status of a task.
- **6. Exit**: Quit the application.
