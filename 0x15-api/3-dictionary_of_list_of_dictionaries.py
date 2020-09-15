#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""

if __name__ == "__main__":
    import json
    import requests

    URI_base = 'https://jsonplaceholder.typicode.com'
    users = requests.get(str(URI_base + "/users")).json()
    tasks = requests.get(str(URI_base + "/todos")).json()
    user_dict = {}

    with open('todo_all_employees.json', 'w') as file:
        for user in users:
            user_dict.update({user.get("id"): []})
            tasks_query = {"userId": user.get("id")}
            tasks = requests.get(str(URI_base + "/todos"),
                                 params=tasks_query).json()
            for task in tasks:
                user_dict.get(user.get("id")).append(
                    {
                        "username": user.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")
                    })
        file.write(json.dumps(user_dict))
