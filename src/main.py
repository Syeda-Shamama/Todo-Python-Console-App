from storage.memory_store import MemoryStore
from cli.interface import (
    handle_add_task,
    handle_list_tasks,
    handle_update_task,
    handle_delete_task,
    handle_toggle_complete,
    print_main_menu,
)

def main():
    """Main function for the todo application."""
    store = MemoryStore()
    while True:
        print_main_menu()
        choice = input("Enter choice (1-6): ")
        if choice == '1':
            handle_add_task(store)
        elif choice == '2':
            handle_list_tasks(store)
        elif choice == '3':
            handle_update_task(store)
        elif choice == '4':
            handle_delete_task(store)
        elif choice == '5':
            handle_toggle_complete(store)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
