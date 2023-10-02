from user import User, UserManager
from task_manager import TaskManager  #
from authentication import Authentication


class TodoApplication:
    def __init__(self):
        self.user_manager = UserManager()  # manages users that use the app
        self.task_manager = None
        self.authenticator = Authentication(self.user_manager)

    def create_task_manager(
        self, user
    ):  # logged in user with task and create a task manager to do CRUD operations on task
        self.task_manager = TaskManager(
            user
        )  # creates a task manager object  with a specific user and asiggns to self.task_manager

    def register_user(self, username, password):  # user registers with username and pw
        self.task_manager.register(username, password)

    def login_user(
        self, username, password
    ):  # when registered user logs in, the app checks if the user is the right person
        user = self.authenticator.authenticate(username, password)
        if user:
            self.create_task_manager(user)
            return True
        return False

    def create_task(self, task_name):  # logged in user creates task
        if self.task_manager:
            self.task_manager.create_task(task_name)

    def get_tasks(self):  # when logged in user wants to see tasks
        if self.task_manager:
            return self.task_manager.get_tasks()
        return []

    def update_task(
        self, task_name, is_completed
    ):  # if logged in user completes the task, we update_task
        if self.task_manager:
            self.task_manager.update_task(task_name, is_completed)

    def delete_task(self, task_name):  # if looged in user wants to delete the task
        if self.task_manager:
            self.task_manager.delete_task(task_name)

    def logout_user(
        self,
    ):  # if logged in user wnats to log out and after log out,  task_manager becomes None
        self.task_manager = None
