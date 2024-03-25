#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    read = get('https://jsonplaceholder.typicode.com/todos')
    data = read.json()
    tasks = []
    tasks_done = 0
    all_tasks = 0
    read = get('https://jsonplaceholder.typicode.com/users')
    data_user = read.json()

    for user in data_user:
        if user.get('userId') == int(argv[1]):
            all_tasks += 1

            if user.get('completed') is True:
                tasks_done += 1
                tasks.append(user.get('title'))
            
    print(f"Employee {argv[1]} is done with tasks({tasks_done}/{all_tasks}):")

    for task in tasks:
        print("\t {}".format(task))
