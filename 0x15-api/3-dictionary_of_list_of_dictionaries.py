#!/usr/bin/python3
""" api to fetch user data """

import json
import requests
import sys

if __name__ == '__main__':

    user_data = requests.get("https://jsonplaceholder.typicode.com/users")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    todoall = {}
    for user in user_data.json():
        taskList = []
        for task in todo.json():
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)

        todoall[user.get('id')] = taskList

        with open("todo_all_employees.json", mode='w') as file:
            json.dump(todoall, file)
