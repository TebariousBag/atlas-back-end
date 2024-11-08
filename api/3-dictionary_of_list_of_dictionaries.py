#!/usr/bin/python3
""" get data from api"""
import json
import requests


def get_employee():
    """ get data for all employees """
    """ get user info and todos info from the site provided """
    users_request = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_request = requests.get("https://jsonplaceholder.typicode.com/todos")
    """ status request 200 is success """
    if users_request.status_code != 200 or todos_request.status_code != 200:
        print("error")
        return
    """ parse json data and convert to python """
    users_data = users_request.json()
    todos_data = todos_request.json()
    """ dict to hold """
    data = {}
    """ iterate through users """
    for user in users_data:
        USER_ID = user.get("id")
        USERNAME = user.get("username")
        """ get tasks for each user """
        user_tasks = [
            task for task in todos_data if task.get('userId') == USER_ID]
        """ list of tasks"""
        task_list = [{
            "username": USERNAME,
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in user_tasks]

        data[str(USER_ID)] = task_list
    """ save to json file """
    filename_json = "todo_all_employees.json"
    """ open file, write as file """
    """ data save to file """
    with open(filename_json, mode='w') as file:
        json.dump(data, file)

    print(f"saved to {filename_json}")
    """ print the data"""
    with open(filename_json, mode='r') as file:
        print(file.read())


if __name__ == "__main__":
    get_employee()
