#!/usr/bin/python3
""" get data from api"""
import sys
import requests


def get_employee(employee_id):
    """ get data """

    """ get user info and todos info from the site provided"""
    user_request = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos_request = requests.get(f"https://jsonplaceholder.typicode.com/todos/{employee_id}")
    
    """ status request 200 is success """
    """ if not 200 then error """
    if user_request.status_code != 200 or todos_request.status_code != 200:
        print("error")
        return
    
    """ parse json data and convert to python """
    user_data = user_request.json()
    todos_data = todos_request.json()

    """ now get data from parsed data"""
    """ use get to access keys, first we get 'name' """
    EMPLOYEE_NAME = user_data.get("name")
    """ check for tasks that are 'completed' """
    DONE_TASKS = [task for task in todos_data if task.get('completed')]
    """ now we know how many tasks total, and how many are done"""
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(todos_data)

