import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


def initials(answers):
    return "Are these your initials? {}{}".format(answers["name"][0], answers["surname"][0])


questions = [
    inquirer3.Text("name", message="What's your name?"),
    inquirer3.Text("surname", message="{name}, what's your surname?"),
    inquirer3.Text("alias", message="What's your Alias, {name}?", default="{surname}"),
    inquirer3.Confirm("initials", message=initials, default=True),
]

answers = inquirer3.prompt(questions)

pprint(answers)
