import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Checkbox(
        "interests",
        message="What are you interested in?",
        choices=["Choice %s" % i for i in range(40)],
        default=["Choice 2", "Choice 10"],
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
