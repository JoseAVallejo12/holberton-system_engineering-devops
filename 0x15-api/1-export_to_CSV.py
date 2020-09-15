#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    URI_base = 'https://jsonplaceholder.typicode.com'
    tasks_query = {"userId": argv[1]}
    user_query = {"id": argv[1]}
    user = requests.get(str(URI_base + "/users/"), params=user_query).json()
    tasks = requests.get(str(URI_base + "/todos"), params=tasks_query).json()
    user_list = []
    with open('{}.csv'.format(user[0].get("id")), 'w') as file:
        writer = csv.writer(file,
                            quoting=csv.QUOTE_ALL,
                            delimiter=',',
                            quotechar='"')
        for task in tasks:
            writer.writerow([
                user[0].get("id"),
                user[0].get("username"),
                task.get("completed"),
                task.get("title")
            ])
