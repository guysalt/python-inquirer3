from typing import Optional, Iterable, Any, Union, Callable

import inquirer3.questions as questions
from inquirer3.render.console import ConsoleRender


def text(
    message: Any,
    default: Optional[str] = None,
    autocomplete=None,
    trim_header: bool = True,
    render: Optional[ConsoleRender] = None,
    **kwargs
) -> str:
    render = render or ConsoleRender()
    question = questions.Text(
        name="", message=message, default=default, autocomplete=autocomplete, trim_header=trim_header, **kwargs
    )
    return render.render(question)


def editor(message: Any, render: Optional[ConsoleRender] = None, **kwargs) -> str:
    render = render or ConsoleRender()
    question = questions.Editor(name="", message=message, **kwargs)
    return render.render(question)


def password(
    message: Any,
    default: Optional[str] = None,
    autocomplete=None,
    trim_header: bool = True,
    render: Optional[ConsoleRender] = None,
    **kwargs
) -> str:
    render = render or ConsoleRender()
    question = questions.Password(
        name="", message=message, default=default, autocomplete=autocomplete, trim_header=trim_header, **kwargs
    )
    return render.render(question)


def confirm(
    message: Any,
    default: Optional[str] = None,
    trim_header: bool = True,
    render: Optional[ConsoleRender] = None,
    **kwargs
) -> str:
    render = render or ConsoleRender()
    question = questions.Confirm(name="", message=message, default=default, trim_header=trim_header, **kwargs)
    return render.render(question)


def list_input(
    message: Any,
    choices: Optional[Iterable] = None,
    default: Any = None,
    ignore: Union[bool, Callable] = False,
    validate: Union[bool, Callable] = True,
    carousel: bool = False,
    other: bool = False,
    autocomplete: Optional[Callable] = None,
    trim_header: bool = True,
    trim_choices: bool = False,
    render: Optional[ConsoleRender] = None,
) -> str:
    render = render or ConsoleRender()
    question = questions.List(
        name="",
        message=message,
        choices=choices,
        default=default,
        ignore=ignore,
        validate=validate,
        carousel=carousel,
        other=other,
        autocomplete=autocomplete,
        trim_header=trim_header,
        trim_choices=trim_choices,
    )
    return render.render(question)


def checkbox(
    message: Any,
    choices: Optional[Iterable] = None,
    locked: Optional[Iterable] = None,
    default: Any = None,
    ignore: Union[bool, Callable] = False,
    validate: Union[bool, Callable] = True,
    carousel: bool = False,
    other: bool = False,
    autocomplete: Optional[Callable] = None,
    trim_header: bool = True,
    trim_choices: bool = False,
    render: Optional[ConsoleRender] = None,
) -> str:
    render = render or ConsoleRender()
    question = questions.Checkbox(
        name="",
        message=message,
        choices=choices,
        locked=locked,
        default=default,
        ignore=ignore,
        validate=validate,
        carousel=carousel,
        other=other,
        autocomplete=autocomplete,
        trim_header=trim_header,
        trim_choices=trim_choices,
    )
    return render.render(question)


def path(
    message: Any,
    default: Any = None,
    trim_header: bool = True,
    path_type: str = "any",
    exists: Optional[bool] = None,
    normalize_to_absolute_path: bool = False,
    render: Optional[ConsoleRender] = None,
    **kwargs
) -> str:
    render = render or ConsoleRender()
    question = questions.Path(
        name="",
        message=message,
        default=default,
        trim_header=trim_header,
        path_type=path_type,
        exists=exists,
        normalize_to_absolute_path=normalize_to_absolute_path,
        **kwargs
    )
    return render.render(question)
