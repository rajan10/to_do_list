import json
from user import User


class TodoApplication:
    def __init__(self, user: User):
        self.user = user
        self.tasks = []  # 0 Cleaning, 1 Coding,2 Deploying

    def load_tasks(self):
        try:
            with open(f"{self.user.logged_in_user}_tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, AttributeError) as exec:
            print(f"...Exception occured while loading  task {str(exec)}")
            self.tasks = []

    def get_tasks(self):
        return self.tasks

    def create_task(self, task_name):
        task = {"name": task_name, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def save_tasks(self):
        with open(f"{new_user.logged_in_user}_tasks.json", "w") as file:
            json.dump(
                self.tasks, file
            )  # dict to json  # CHECK HERE old tasks are save each time

    def update_task(self, task_index, task_name, completed):
        task = self.tasks[task_index]
        task["name"] = task_name
        task["completed"] = completed
        self.save_tasks()

    def delete_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()
