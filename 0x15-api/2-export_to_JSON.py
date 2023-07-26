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
    file_name = f"{argv[1]}.json"
    count = 0
    with open(file_name, mode="w", encoding="utf-8") as f:
        contents = '{' + f'''"{argv[1]}": ''' + '['
        for task in tasks:
            contents += "{" + '''"task": "{}", "completed": {}, "username":\
{}'''.format(task['title'], task['completed'], username) + '}'
            if count != (len(tasks) - 1):
                contents += ', '
            else:
                contents += ']}'
            count += 1
            f.write(contents)
            contents = ''


if __name__ == '__main__':
    export_to_csv()
