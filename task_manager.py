from user import User
import csv


class Task:
    def __init__(self, name, is_completed=False):
        self.name = name
        self.is_completed = is_completed

    def __str__(self) -> str:
        return f"<name: {self.name}>"

    def __repr__(self) -> str:
        return f"name: {self.name} task status: {self.is_completed}"


class TaskManager:
    def __init__(self, user: User):
        self.user = user
        self.tasks = []
        self.filename = f"{user.username}_tasks.csv"
        self._load_tasks()

    def _load_tasks(self) -> None:
        try:
            with open(self.filename, "r") as file_object:
                reader = csv.DictReader(file_object)
                for row in reader:  # row= {"name":"hari","is_completed":False}
                    task = Task(name=row["name"], is_completed=row["is_completed"])
                    self.tasks.append(task)
        except FileNotFoundError:
            print(f"...{self.filename} not Found")

    def get_tasks(self):
        return self.tasks

    def create_task(self, task_name: str, is_completed=False):
        task = Task(name=task_name, is_completed=is_completed)
        self.tasks.append(task)
        self.save_task(task=task)

    def save_task(self, task: Task) -> None:
        with open(self.filename, "a", newline="") as file_object:
            writer = csv.DictWriter(file_object, fieldnames=["name", "is_completed"])
            if file_object.tell() == 0:
                writer.writeheader()
            writer.writerow({"name": task.name, "is_completed": task.is_completed})

    def save_tasks(self, tasks: list[Task]) -> None:
        with open(self.filename, "w", newline="") as file_object:
            writer = csv.DictWriter(file_object, fieldnames=["name", "is_completed"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow({"name": task.name, "is_completed": task.is_completed})

    def get_user_by_username(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user

    def get_task_by_task_name(self, task_name: str) -> Task | None:
        for task in self.tasks:
            if task.name == task_name:
                return task

    def update_task(self, task_name: str, is_completed: bool):
        task = self.get_task_by_task_name(task_name)
        if task:
            task.is_completed = is_completed
            self.save_tasks(self.tasks)

    def delete_task(self, task_name: str):  # 0 coding 1 Cleaning 2 Cooking
        task = self.get_task_by_task_name(task_name)
        if task:
            self.tasks.remove(task)
            self.save_tasks(self.tasks)


# user_object_gita = User(username="gita", password="gita!")
# print(user_object_gita.username)
# # user_object_rita = User(username="rita", password="rita!")
# task_manager = TaskManager(user=user_object_gita)


# task_manager.create_task(task_name="playing")


# task_manager.update_task(task_name="Reporting", is_completed=False)
# print(task_manager.get_tasks())

# task_manager.delete_task("Reporting")


# task_manager.create_task(task_name="Washing")
# print(task_manager.get_task_by_task_name(task_name="Coding"))

# task_manager.update_task(task_name="Coding", is_completed=True)
