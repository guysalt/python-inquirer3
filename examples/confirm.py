import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Confirm("continue", message="Should I continue"),
    inquirer3.Confirm("stop", message="Should I stop", default=True),
]

answers = inquirer3.prompt(questions)

pprint(answers)
