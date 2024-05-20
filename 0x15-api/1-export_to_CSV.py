#!/usr/bin/python3
""" Python script to export data in the CSV format """

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_name = user_data.json().get('username')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for to in todo.json():
            writer.writerow(
                [user_id, user_name, to.get('completed'), to.get('title')])
