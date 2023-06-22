import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer3  # noqa


if __name__ == "__main__":

    questions = [
        inquirer3.Text("user", message="Please enter your github username", validate=lambda _, x: x != "."),
        inquirer3.Password("password", message="Please enter your password"),
        inquirer3.Text("repo", message="Please enter the repo name", default="default"),
        inquirer3.Checkbox(
            "topics",
            message="Please define your type of project?",
            choices=["common", "backend", "frontend"],
        ),
        inquirer3.Text(
            "organization",
            message=(
                "If this is a repo from a organization please enter the organization name,"
                " if not just leave this blank"
            ),
        ),
        inquirer3.Confirm(
            "correct",
            message="This will delete all your current labels and create a new ones. Continue?",
            default=False,
        ),
    ]

    answers = inquirer3.prompt(questions)

    # Ask again, using previous values as defaults

    answers = inquirer3.prompt(questions, answers=answers)

    pprint(answers)
