import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))

import inquirer3  # noqa


questions = [
    inquirer3.Password("password1", message="What's your password"),
    inquirer3.Password("password2", message="Password echoing dots", echo="."),
    inquirer3.Password("password3", message="Password no echo", echo=""),
]

answers = inquirer3.prompt(questions)

pprint(answers)
