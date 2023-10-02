import csv


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self):
        print(f"Username: {self.username}")

    def __str__(self):
        print(f"<Username: {self.username}>")


class UserManager:
    def __init__(self):
        self.users = []  # list of user obj
        self.filename = "users.csv"
        self.load_users()

    def load_users(self) -> None:
        try:
            with open(self.filename, "r") as file_object:
                reader = csv.DictReader(file_object)
                for (
                    row
                ) in reader:  # in dict "username": "ram", "password":"ram!".  dict->obj
                    user = User(
                        username=row["username"], password=row["password"]
                    )  # instances
                    self.users.append(user)  # object
        except FileNotFoundError as exec:
            print(f"...{str(exec)} File not Found")

    def save_user(self, user: User) -> None:
        with open(self.filename, "a", newline="") as file_object:
            writer = csv.DictWriter(file_object, fieldnames=["username", "password"])
            if file_object.tell() == 0:
                writer.writeheader()
            writer.writerow(vars(user))  # in  dict format

    def get_user_by_username(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user


# ram = User(username="ram", password="ram!")

# user1 = UserManager()
# user1.save_user(user=ram)
# user1.load_users()
