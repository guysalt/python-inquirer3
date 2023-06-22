import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Text("name", message="What's your name?"),
    inquirer3.Text(
        "surname", message="What's your surname, {name}?", ignore=lambda x: x["name"].lower() == "anonymous"
    ),
    inquirer3.Confirm("married", message="Are you married?"),
    inquirer3.Text("time_married", message="How long have you been married?", ignore=lambda x: not x["married"]),
]

answers = inquirer3.prompt(questions)

pprint(answers)
