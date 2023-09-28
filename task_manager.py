from user import User
import csv


class Task:
    def __init__(self, name, is_completed=False):
        self.name = name
        self.is_completed = is_completed


class TaskManager:
    def __init__(self, user: User):
        self.user = user
        self.tasks = []
        self._load_tasks()

    def _load_tasks(self) -> None:
        filename = f"{self.user.username}_tasks.csv"
        try:
            with open(filename, "r") as file_object:
                reader = csv.DictReader(file_object)
                for row in reader:
                    task = Task(name=row["name"], is_completed=row["is_completed"])
                    self.tasks.append(task)
        except FileNotFoundError:
            print(f"...{filename} not Found")

    def get_tasks(self):
        return self.tasks

    def create_task(self, task_name: str, is_completed=False):
        task = Task(name=task_name, is_completed=is_completed)
        self.tasks.append(task)
        self.save_task(task=task)

    def save_task(self, task: Task) -> None:
        with open(f"{self.user.username}_tasks.csv", "a", newline="") as file_object:
            writer = csv.DictWriter(file_object, fieldnames=["name", "is_completed"])
            if file_object.tell() == 0:
                writer.writeheader()
            writer.writerow({"name": task.name, "is_completed": task.is_completed})

    def save_tasks(self, tasks: list[Task]) -> None:
        with open(f"{self.user.username}_tasks.csv", "w") as file_object:
            writer = csv.DictWriter(file_object, fieldnames=["name", "is_completed"])
            writer.writeheader()
            for task in tasks:
                writer.writerow({"name": task.name, "is_completed": task.is_completed})

    def get_task_by_task_name(self, task_name: str) -> Task | None:
        for task in self.tasks:
            if task.name == task_name:
                return task

    def update_task(self, task_name: str, is_completed: bool):
        task = self.get_task_by_task_name(task_name)
        if task:
            task.is_completed = is_completed
            # to do save logic

    def delete_task(self, task_name: str):  # 0 coding 1 Cleaning 2 Cooking
        task = self.get_task_by_task_name(task_name)
        if task:
            self.tasks.remove(task)


user_object = User(username="hari", password="hari!")
task_manager = TaskManager(user=user_object)

task_manager.create_task(task_name="Coding")
