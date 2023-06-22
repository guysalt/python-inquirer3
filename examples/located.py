import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


LangQuestion = [
    inquirer3.List(
        "lang",
        message="Select Language",
        choices=["English", "Français", "Deutsch", "Español"],
    ),
]

answers = inquirer3.prompt(LangQuestion)

pprint(answers)
