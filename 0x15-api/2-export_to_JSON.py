#!/usr/bin/python3
""" API and convert to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    USERNAME = res.json().get('username')
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    data = {USER_ID: []}
    for task in tasks:
        STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": STATUS,
                                  "username": USERNAME})
    filename = f"{USER_ID}.json"
with open(filename, "w") as f:
    f.write(json.dumps(data))
