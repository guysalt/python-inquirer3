from typing import Any

import inquirer3.questions as questions
from inquirer3.render.console import ConsoleRender


def text(message, default=None, autocomplete=None, trim_header=True, render=None, **kwargs):
    render = render or ConsoleRender()
    question = questions.Text(name="", message=message, default=default, autocomplete=autocomplete,
                              trim_header=trim_header, **kwargs)
    return render.render(question)


def editor(message, render=None, **kwargs):
    render = render or ConsoleRender()
    question = questions.Editor(name="", message=message, **kwargs)
    return render.render(question)


def password(message, default=None, autocomplete=None, trim_header=True, render=None,
             **kwargs):
    render = render or ConsoleRender()
    question = questions.Password(name="", message=message, default=default, autocomplete=autocomplete,
                                  trim_header=trim_header, **kwargs)
    return render.render(question)


def confirm(message, default=None, trim_header=True, render=None, **kwargs):
    render = render or ConsoleRender()
    question = questions.Confirm(name="", message=message, default=default, trim_header=trim_header, **kwargs)
    return render.render(question)


def list_input(message, choices=None, default: Any = None, ignore=False, validate=True, carousel=False, other=False,
               autocomplete=None, trim_header=True, trim_choices=False, render=None):
    render = render or ConsoleRender()
    question = questions.List(name="", message=message, choices=choices, default=default, ignore=ignore,
                              validate=validate, carousel=carousel, other=other, autocomplete=autocomplete,
                              trim_header=trim_header, trim_choices=trim_choices)
    return render.render(question)


def checkbox(message, choices=None, locked=None, default: Any = None, ignore=False, validate=True, carousel=False,
             other=False, autocomplete=None, trim_header=True, trim_choices=False, render=None):
    render = render or ConsoleRender()
    question = questions.Checkbox(name="", message=message, choices=choices, locked=locked, default=default,
                                  ignore=ignore, validate=validate, carousel=carousel, other=other,
                                  autocomplete=autocomplete, trim_header=trim_header, trim_choices=trim_choices)
    return render.render(question)


def path(message, default: Any = None, trim_header=True, path_type="any", exists=None,
         normalize_to_absolute_path=False, render=None, **kwargs):
    render = render or ConsoleRender()
    question = questions.Path(name="", message=message, default=default, trim_header=trim_header, path_type=path_type,
                              exists=exists, normalize_to_absolute_path=normalize_to_absolute_path, **kwargs)
    return render.render(question)
