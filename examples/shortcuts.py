import os
import sys


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


text = inquirer3.text(message="Enter your username")
print(text)
password = (inquirer3.password(message="Please enter your password"),)
print(password)
checkbox = inquirer3.checkbox(message="Please define your type of project?", choices=["common", "backend", "frontend"])
print(checkbox)
choice = inquirer3.list_input("Public or private?", choices=["public", "private"])
print(choice)
correct = inquirer3.confirm(
    "This will delete all your current labels and " "create a new ones. Continue?", default=False
)
print(correct)
