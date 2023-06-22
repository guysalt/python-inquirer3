import inquirer3


suggestions = ["inquirer3", "hello", "world", "foo", "bar", "baz", "qux"]


def autocomplete_fn(_text, state):
    # Every time the user presses TAB, we'll switch to the next suggestion
    # The `state` variable contains the index of the current suggestion
    # We can wrap it around to the first suggestion if we reach the end
    return suggestions[state % len(suggestions)]


questions = [
    inquirer3.Text(
        "name",
        message="Press TAB to cycle through suggestions",
        autocomplete=autocomplete_fn,
    ),
]

answers = inquirer3.prompt(questions)

print(answers)
