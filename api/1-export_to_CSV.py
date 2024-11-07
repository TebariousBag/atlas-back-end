#!/usr/bin/python3
""" get data from api"""
import requests
import sys


def get_employee(employee_id):
    """ get data """

    """ get user info and todos info from the site provided"""
    user_request = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos_request = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

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
    """ get key data 'id' """
    USER_ID = user_data.get("id")
    """ check for tasks that are 'completed' """
    DONE_TASKS = [task for task in todos_data if task.get('completed')]
    """ now we know how many tasks total, and how many are done"""
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(todos_data)

    """ print statement how many tasks are done """
    print(f"Employee {EMPLOYEE_NAME} is done with tasks("
          f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    """ PRINT EACH TASK """
    for task in DONE_TASKS:
        print(f"\t {task.get('title')}")

    """ create csv file """
    """ from data we have 'id' """
    filename = f"{USER_ID}.csv"


""" functionallity to run as main """
if __name__ == "__main__":
    """ get employee id make sure its int"""

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("must be int")
        sys.exit(1)
    """ call the function"""
    get_employee(employee_id)
