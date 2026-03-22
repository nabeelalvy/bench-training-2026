import json
import argparse
from datetime import datetime
from dataclasses import dataclass


def read_json_file(filepath):
    try:
        with open(filepath) as file:
            return json.load(file)
    except FileNotFoundError:
            raise FileNotFoundError(f"Error: The file '{filepath}' was not found.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to decode JSON from the file: {e}")

def write_to_json_file(filepath, tasks):
    try:
        with open(filepath, 'w') as file:
            json.dump(convert_to_dict(tasks), file, indent=4)
        print(f"Successfully data written to '{filepath}'")
    except IOError as e:
        print(f"Error writing to file: {e}")

def convert_to_dict(tasks):
    return [task.to_dict() for task in tasks]


@dataclass
class Task:
    id: int
    title: str
    status: str
    created_at: datetime

    @staticmethod
    def to_task_obj(task_obj):
        return Task(
            int(task_obj["id"]),
            str(task_obj["title"]),
            str(task_obj["status"]),
            datetime.fromisoformat(task_obj["created_at"])
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

class TaskManager:

    TASKS_FILE = "tasks.json"

    def __init__(self):
        self.tasks = self.hydrate_tasks() or []

    def _next_id(self):
        return max((task.id for task in self.tasks), default=0) + 1

    def hydrate_tasks(self):
        try:
            tasks_data = read_json_file(TaskManager.TASKS_FILE)
            return [Task.to_task_obj(task) for task in tasks_data]
        except (FileNotFoundError, ValueError) as e:
            print(e)
            return []

    def print_tasks(self):
        if not self.tasks:
            print("No tasks available to print.")
            return

        for task in self.tasks:
            print(f"{task.id:<3} | {task.title:<35} | {task.status:<5} | {task.created_at}")

    def add_task(self, title, status="todo"):
        self.tasks.append(Task(self._next_id(), title, status, datetime.now()))
        write_to_json_file(TaskManager.TASKS_FILE, self.tasks)

    def complete_task(self, id):
        for task in self.tasks:
            if task.id == int(id):
                task.status = "done"
                task.created_at = datetime.now()
                write_to_json_file(TaskManager.TASKS_FILE, self.tasks)
                break
        else:
            print(f"No task found with id={id}")

    def list_tasks(self, filter=None):
        if filter is None:
            self.print_tasks()
        else:
            for task in self.tasks:
                if task.status == filter:
                    print(f"{task.id} - {task.title} [{task.status}]")

    def delete_task(self, id):
        updated_tasks = [task for task in self.tasks if task.id != int(id)]
        if len(self.tasks) != len(updated_tasks):
            write_to_json_file(TaskManager.TASKS_FILE, updated_tasks)
        else:
            print(f"No tasks found with id={id}.")


def configure_parser():
    parser = argparse.ArgumentParser(
        description="Manage tasks via CLI"
    )

    parser.add_argument(
        "-at",
        dest="add_task",
        metavar="Add new task",
        help="Add a new task"
    )

    parser.add_argument(
        "-ct",
        dest="complete_task",
        metavar="Mark a task as complete",
        help="Mark a task as complete"
    )

    parser.add_argument(
        "-dt",
        dest="delete_task",
        metavar="Delete a task",
        help="Delete a task"
    )

    parser.add_argument(
        "-l",
        "--list",
        dest="list_task",
        action="store_true",
        help="List tasks"
    )

    parser.add_argument(
        "--filter",
        choices=["todo", "done"],
        help="Filter tasks by status"
    )

    return parser.parse_args()

def main():
    args = configure_parser()
    manager = TaskManager()
    commands = {
        "add": lambda: manager.add_task(args.add_task),
        "complete": lambda: manager.complete_task(args.complete_task),
        "delete": lambda: manager.delete_task(args.delete_task),
        "list": lambda: manager.list_tasks(filter=args.filter),
    }

    if args.add_task:
        commands["add"]()
    elif args.complete_task:
        commands["complete"]()
    elif args.delete_task:
        commands["delete"]()
    elif args.list_task:
        commands["list"]()
    elif args.filter and not args.list_task:
        print("--filter only works with --list")
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

