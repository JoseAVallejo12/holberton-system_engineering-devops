#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import csv
    from sys import argv
    import requests

    URI_base = 'https://jsonplaceholder.typicode.com'
    tasks_query = {"userId": 1}
    user = requests.get(str(URI_base + "/user/" + argv[1])).json()
    tasks = requests.get(str(URI_base + "/todos"), params=tasks_query)
    user_task_done = []

    for task in tasks.json():
        if (task.get("completed")):
            user_task_done.append(task.get("title"))

    print('Employee {} is done with tasks({}/{}):'.format(
        user.get("name"),
        len(user_task_done),
        (len(tasks.json()) - len(user_task_done))
    ))
    for val in user_task_done:
        print("\t ", end="")
        print('{}'.format(val))
