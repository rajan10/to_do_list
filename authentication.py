from user import User

from user import UserManager


usermanager = UserManager()


class Authentication:
    def register(self, username: str, password: str) -> None:
        user = User(username, password)
        usermanager.save_user(user=user)

    def authenticate(self, username: str, password: str) -> bool:
        user = usermanager.get_user_by_username(username=username)
        if not user:
            return False
        if user.password == password:
            return True
        else:
            return False


auth = Authentication()
# auth.register(username="ganesh", password="ganesh!")
print(auth.authenticate(username="dfdf", password="radfdfm!"))
