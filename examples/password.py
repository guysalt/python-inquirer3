import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


questions = [inquirer3.Password("password", message="What's your password")]

answers = inquirer3.prompt(questions)

pprint(answers)
