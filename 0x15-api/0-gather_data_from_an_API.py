#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv

    URI_base = 'https://jsonplaceholder.typicode.com'
    tasks_query = {"userId": argv[1]}
    user_query = {"id": argv[1]}
    user = requests.get(str(URI_base + "/users/"), params=user_query).json()
    tasks = requests.get(str(URI_base + "/todos"), params=tasks_query).json()
    user_task_done = []

    for task in tasks:
        if (task.get("completed")):
            user_task_done.append(task.get("title"))

    print('Employee {} is done with tasks({}/{}):'.format(
        user[0].get("name"),
        len(user_task_done),
        len(tasks)
    ))
    for val in user_task_done:
        print("\t ", end="")
        print('{}'.format(val))
