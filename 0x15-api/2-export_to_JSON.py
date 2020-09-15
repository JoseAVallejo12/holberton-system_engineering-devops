#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    URI_base = 'https://jsonplaceholder.typicode.com'
    tasks_query = {"userId": argv[1]}
    user_query = {"id": argv[1]}
    user = requests.get(str(URI_base + "/users/"), params=user_query).json()
    tasks = requests.get(str(URI_base + "/todos"), params=tasks_query).json()
    user_dict = {argv[1]: []}

    with open('{}.json'.format(user[0].get("id")), 'w') as file:
        for task in tasks:
            user_dict.get(argv[1]).append(
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user[0].get("username")
                })
        file.write(json.dumps(user_dict))
