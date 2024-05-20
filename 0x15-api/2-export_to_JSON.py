#!/usr/bin/python3
""" api to fetch user data """

import requests
import sys
import json

if __name__ == '__main__':

    user_id = sys.argv[1]
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(user_id))
    user_name = user_data.json().get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    userdict = {}
    taskList = []

    for task in todo.json():
        if task.get('userId') == int(user_id):
            taskdict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user_data.json().get('username')}
            taskList.append(taskdict)
    userdict[user_id] = taskList

    filename = f'{user_id}.json'
    with open(filename, mode='w') as file:
        json.dump(userdict, file)
