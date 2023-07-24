#!/usr/bin/python3
"""This module contains a script that gather
data from an API
"""
from sys import argv
from urllib import request
import json


def gather_data_from_api():
    """Displays information about employee """
    url = f'https://jsonplaceholder.typicode.com/users/' + f'{argv[1]}'
    with request.urlopen(url) as response:
        content = response.read()
    employee = json.loads(content)
    employee_name = employee['name']
    to_do_url = url + '/todos'
    with request.urlopen(to_do_url) as response:
        content = response.read()
    tasks = json.loads(content)
    completed_tasks = []
    number_of_done_tasks = 0
    for task in tasks:
        if task['completed']:
            completed_tasks.append(task)
            number_of_done_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks,
            len(tasks)))
    for completed_task in completed_tasks:
        print('\t ', completed_task['title'])


if __name__ == '__main__':
    gather_data_from_api()
