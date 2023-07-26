#!/usr/bin/python3
"""This module contains a script that gather
data from an API
"""
import json
from sys import argv
from urllib import request


def export_to_json():
    """Export data in json format"""
    user = 1
    contents = '{'
    while (user <= 10):
        url = f'https://jsonplaceholder.typicode.com/users/' + f'{user}'
        with request.urlopen(url) as response:
            content = response.read()
        employee = json.loads(content)
        username = employee['username']
        to_do_url = url + '/todos'
        with request.urlopen(to_do_url) as response:
            content = response.read()
        tasks = json.loads(content)
        file_name = "todo_all_employees.json"
        count = 0
        with open(file_name, mode="a", encoding="utf-8") as f:
            contents = f'''"{user}": ''' + '['
            for task in tasks:
                contents += "{" + '"username": "{}", "task": {}, "completed": \
"{}"'.format(
                        username, task['title'], 'true' if task['completed']
                        else 'false') + '}'
                if count != (len(tasks) - 1):
                    contents += ', '
                else:
                    if user == 10:
                        contents += ']}'
                    else:
                        contents += '], '
                count += 1
                f.write(contents)
                contents = ''
        user += 1


if __name__ == '__main__':
    export_to_json()
