import json


class TodoApplication:
    def __init__(self):
        self.users = []
        self.load_users() # load the users.json file in r mode
        self.logged_in_user = None
        self.tasks = []
        self.load_tasks() # load logged_in_user_tasks.json in r mode
    
    def load_users(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = []
            
    def load_tasks(self):
        try:
            with open(f"{self.logged_in_user}_tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, AttributeError):
            self.tasks = []
            
    def save_users(self):   # to dict form in w mode
        with open("users.json", "w") as file:
            json.dump(self.users, file)
    
    def register(self, username, password):
        user = { "username": username, "password": password}   # user is a dict object
        self.users.append(user)
        self.save_users()
        
    def login(self, username, password):
        for user in self.users: 
            if user["username"] == username and user["password"] == password:
                self.logged_in_user = username
                return True
    
    def logout(self):
        self.logged_in_user = None
        self.tasks = []  # clear the tasks list
    
    def get_tasks(self):
        return self.tasks
    
    def create_task(self, task_name):
        task = {"name": task_name, "completed": False} 
        self.tasks.append(task)
        self.save_tasks()
        
    def save_tasks(self):
        with open(f"{self.logged_in_user}_tasks.json", "w") as file:
            json.dump(self.tasks, file)
            
    def update_task(self, task_index, task_name, completed):
        task = self.tasks[task_index]
        task["name"] = task_name
        task["completed"] = completed
        self.save_tasks()
    
    def delete_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()
        
    