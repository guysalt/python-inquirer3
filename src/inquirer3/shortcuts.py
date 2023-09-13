from typing import Optional, Iterable, Any, Union, Callable

import inquirer3.questions as questions
from inquirer3.render.console import ConsoleRender


def text(
    message: Any,
    default: Optional[str] = None,
    ignore: Union[bool, Callable] = False,
    validate: Union[bool, Callable] = True,
    show_default: Union[bool, Callable] = False,
    trim_header: bool = True,
    autocomplete=None,
    render: Optional[ConsoleRender] = None,
    raise_keyboard_interrupt: bool = False
) -> str:
    render = render or ConsoleRender(raise_keyboard_interrupt=raise_keyboard_interrupt)
    question = questions.Text(
        name="", message=message, default=default, ignore=ignore, validate=validate, show_default=show_default,
        autocomplete=autocomplete, trim_header=trim_header,
    )
    return render.render(question)


def editor(
    message: Any,
    default: Optional[str] = None,
    ignore: Union[bool, Callable] = False,
    validate: Union[bool, Callable] = True,
    show_default: Union[bool, Callable] = False,
    trim_header: bool = True,
    autocomplete=None,
    render: Optional[ConsoleRender] = None,
    raise_keyboard_interrupt: bool = False
) -> str:
    render = render or ConsoleRender(raise_keyboard_interrupt=raise_keyboard_interrupt)
    question = questions.Editor(
        name="", message=message, default=default, ignore=ignore, validate=validate, show_default=show_default,
        autocomplete=autocomplete, trim_header=trim_header,
    )
    return render.render(question)


def password(
    message: Any,
    echo: str = "*",
    default: Any = None,
    ignore: Union[bool, Callable] = False,
    validate: Union[bool, Callable] = True,
    show_default: Union[bool, Callable] = False,
    trim_header: Union[bool, Callable] = True,
    autocomplete: Optional[Callable] = None,
    render: Optional[ConsoleRender] = None,
) -> str:
    render = render or ConsoleRender()
    question = questions.Password(
        name="", message=message, echo=echo, default=default, ignore=ignore, validate=validate,
        show_default=show_default, trim_header=trim_header, autocomplete=autocomplete,
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
