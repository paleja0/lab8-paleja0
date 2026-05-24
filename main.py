"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file

def print_help():
    print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        if sys.argv[1] == "--help":
            print_help()
            return

        file_path = sys.argv[1]

        tasks = read_todo_file(file_path)

        args = sys.argv[2:]
        
        changes_made = False

        i = 0
        while i < len(args):
            command = args[i]

            if command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1 

            elif command == "add":
                
                if i + 1 >= len(args):
                    raise IndexError('Task description required for "add".')
                new_task = args[i + 1]
                tasks.append(new_task)
                print(f'Task "{new_task}" added.')
                changes_made = True
                i += 2 

            elif command == "remove":
              
                if i + 1 >= len(args):
                    raise IndexError('Task description required for "remove".')
                task_to_remove = args[i + 1]
                
                if task_to_remove in tasks:
                    tasks.remove(task_to_remove)
                    print(f'Task "{task_to_remove}" removed.')
                    changes_made = True
                else:
                    print(f'Task "{task_to_remove}" not found.')
                i += 2 

            else:
            
                raise ValueError("Command not found!")

        if changes_made:
            write_todo_file(file_path, tasks)

    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()