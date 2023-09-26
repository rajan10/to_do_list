from todo_application import TodoApplication

def menu_display():
    app = TodoApplication()
    while True:
        if app.logged_in_user:
            print(f"\nLogged in as {app.logged_in_user}")
            print("1. Create Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                task_name = input("Enter task name: ")
                app.create_task(task_name)
            elif choice == "2":
                tasks = app.get_tasks()
                for i, task in enumerate(tasks):
                    status = "Done" if task["completed"] else "Not Done"
                    print(f"{i + 1}. {task['name']} ({status})")
            elif choice == "3":
                task_index = int(input("Enter task number to update: ")) - 1
                task_name = input("Enter updated task name: ")
                completed = input("Is it completed? (True/False): ").capitalize() == "True"
                app.update_task(task_index, task_name, completed)
            elif choice == "4":
                task_index = int(input("Enter task number to delete: ")) - 1
                app.delete_task(task_index)
            elif choice == "5":
                app.logout()
        else:
            print("\nTodo List Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                app.register(username, password)
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if app.login(username, password):
                    print(f"Welcome, {username}!")
                else:
                    print("Login failed. Check your credentials.")
            elif choice == "3":
                print("Goodbye!")
                break