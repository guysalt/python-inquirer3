import os
import sys


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


text = inquirer3.text(message="Enter your username")
print(text)
password = (inquirer3.password(message="Please enter your password"),)
print(password)
checkbox = inquirer3.checkbox(choices=["common", "backend", "frontend"], message="Please define your type of project?")
print(checkbox)
choice = inquirer3.list_input(choices=["public", "private"], message="Public or private?")
print(choice)
correct = inquirer3.confirm(
    message="This will delete all your current labels and " "create a new ones. Continue?", default=False
)
print(correct)
