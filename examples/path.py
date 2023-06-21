import os
import sys
from pprint import pprint

import inquirer3


sys.path.append(os.path.realpath("."))

questions = [
    inquirer3.Path("path", message="Give me some any type of path"),
    inquirer3.Path("directory", path_type=inquirer3.Path.DIRECTORY, message="Give me directory"),
    inquirer3.Path("file", path_type=inquirer3.Path.FILE, message="Give me file"),
    inquirer3.Path(
        "existing_file",
        path_type=inquirer3.Path.FILE,
        exists=True,
        message="Give me existing file",
    ),
]

answers = inquirer3.prompt(questions)

pprint(answers)
