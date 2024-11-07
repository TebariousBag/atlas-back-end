#!/usr/bin/python3
""" get data from api"""
import sys
import requests


def get_employee(employee_id):
	""" get data """

	""" get user info and todos info from the site provided"""
	user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
	todos = f"https://jsonplaceholder.typicode.com/todos/{employee_id}"
	