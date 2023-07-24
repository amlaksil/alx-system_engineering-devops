#!/usr/bin/python3
"""This module contains a script that gather
data from an API
"""
import json
from sys import argv
from urllib import request


def export_to_csv():
    """Export data in CSV format"""
    url = f'https://jsonplaceholder.typicode.com/users/' + f'{argv[1]}'
    with request.urlopen(url) as response:
        content = response.read()
    employee = json.loads(content)
    username = employee['username']
    to_do_url = url + '/todos'
    with request.urlopen(to_do_url) as response:
        content = response.read()
    tasks = json.loads(content)
    file_name = f"{argv[1]}.csv"
    with open(file_name, mode="w", encoding="utf-8") as f:
        for task in tasks:
            line = f'''"{task['userId']}","{username
            }","{task['completed']}","{task['title']}"\n'''
            f.write(line)
    print(tasks)


if __name__ == '__main__':
    export_to_csv()
