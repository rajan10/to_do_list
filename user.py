import json
import csv


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self):
        print(f"Username: {self.username}")

    def __str__(self):
        print(f"<Username: {self.username}>")


user = User(username="ram", password="ram!")


class UserManager:
    def __init__(self):
        self.users = []  # list of user obj
        self.load_users()

    def load_users(self) -> None:
        with open("users.csv", "r") as file_object:
            reader = csv.DictReader(file_object)
            for (
                row
            ) in reader:  # in dict "username": "ram", "password":"ram!".  dict->obj
                user = User(
                    username=row["username"], password=row["password"]
                )  # instances
                self.users.append(user)  # object

    def save_user(self, user: User) -> None:
        with open("users.csv", "a") as file_object:
            user_writer = csv.DictWriter(
                file_object, fieldnames=["username", "password"]
            )
            user_writer.writerow(vars(user))  # in  dict format

    def get_user_by_username(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user


class User1:
    def __init__(self):
        self.users = []
        self.load_users()  # load the users.json file in r mode
        self.logged_in_user = None

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = []

    def save_users(self, user):  # to dict form in w mode
        with open("users.json", "w") as file:
            json.dump(self.user, file)  # dict to json  ??

    def register(self, username, password):
        user = {"username": username, "password": password}  # user is a dict object
        self.users.append(user)
        self.save_users(user)

    def login(self, username, password) -> bool:
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                self.logged_in_user = username
                # app.load_tasks()
                return True

    def logout(self):
        self.logged_in_user = None
        self.tasks = []  # clear the tasks list


# new_user = Users()
