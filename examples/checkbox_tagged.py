import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Checkbox(
        "interests",
        message="What are you interested in?",
        choices=[
            ("Computers", "c"),
            ("Books", "b"),
            ("Science", "s"),
            ("Nature", "n"),
            ("Fantasy", "f"),
            ("History", "h"),
        ],
        default=["c", "b"],
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
