import os
import re
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


def phone_validation(answers, current):
    if not re.match(r"\+?\d[\d ]+\d", current):
        raise inquirer3.errors.ValidationError("", reason="I don't like your phone number!")

    return True


questions = [
    inquirer3.Text("name", message="What's your name?"),
    inquirer3.Text("surname", message="What's your surname, {name}?"),
    inquirer3.Text(
        "phone",
        message="What's your phone number",
        validate=phone_validation,
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
