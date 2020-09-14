#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import csv
    from sys import argv
    import requests

    URI_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    URI_task = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(URI_user).json()
    tasks = requests.get(URI_task).json()
    user_task = 0
    user_task_done = []
    for task in tasks:
        if str(task.get("userId")) == argv[1]:
            user_task += 1
            if (task.get("completed")):
                user_task_done.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(user_task_done),
        (user_task - len(user_task_done))
    ))
    for val in user_task_done:
        print("     {}".format(val))
