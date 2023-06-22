import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [
    inquirer3.Editor(
        "poem", message="Write me a poem please", default="Roses are red,", validate=lambda _, x: x.count("\n") >= 2
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
