import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.List(
        "size",
        message="What size do you need?",
        choices=["Choice %s" % i for i in range(20)],
        carousel=False,
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
