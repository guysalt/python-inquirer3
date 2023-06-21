import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Checkbox(
        "interests",
        message="What are you interested in?",
        choices=["Computers", "Books", "Science", "Nature", "Fantasy", "History"],
        default=["Computers", "Books"],
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
