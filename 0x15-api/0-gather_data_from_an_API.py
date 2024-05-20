#!/usr/bin/python3
""" api to fetch user data """

import requests
import sys

if __name__ == '__main__':

    user_id = sys.argv[1]
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(user_id))
    user_name = user_data.json().get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    total_task = comp = 0
    for task in todo.json():
        if task.get('userId') == int(user_id):
            total_task += 1
            if task.get('completed'):
                comp += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, comp, total_task))

    print('\n'.join(["\t " + task.get('title') for task in todo.json()
          if task.get('userId') == int(user_id) and task.get('completed')]))