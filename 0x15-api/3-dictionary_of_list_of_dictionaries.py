#!/usr/bin/python3
""" api to fetch user data """

import json
import requests
import sys

if __name__ == '__main__':

    user_id = sys.argv[1]
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(user_id))
    user_name = user_data.json().get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    todoall = {}
    for user in user_data:
        taskList = []
        for task in todo.json():
            if task.get('userId') == int(user_id):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)

        todoall[user.get('id')] = taskList

        with open("todo_all_employees.json", mode='w') as file:
            json.dumps(todoall, file)
