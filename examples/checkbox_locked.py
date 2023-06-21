import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Checkbox(
        "courses",
        message="Which courses would you like to take?",
        choices=["Programming fundamentals", "Fullstack development", "Data science", "DevOps"],
        locked=["Programming fundamentals"],
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
