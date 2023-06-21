import inquirer3
from inquirer3.themes import GreenPassion


q = [
    inquirer3.Text("name", message="Whats your name?", default="No one"),
    inquirer3.List("jon", message="Does Jon Snow know?", choices=["yes", "no"], default="no"),
    inquirer3.Checkbox(
        "kill_list", message="Who you want to kill?", choices=["Cersei", "Littlefinger", "The Mountain"]
    ),
]

inquirer3.prompt(q, theme=GreenPassion())
