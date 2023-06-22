import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


with open("examples/test_questions.json") as fd:
    questions = inquirer3.load_from_json(fd.read())

answers = inquirer3.prompt(questions)

pprint(answers)
