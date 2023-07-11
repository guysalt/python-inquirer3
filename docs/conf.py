"""Sphinx configuration."""
from datetime import datetime


project = "inquirer3"
author = "Guy Salton"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
# workaround for bug: https://github.com/sphinx-doc/sphinx/issues/9383
linkcheck_ignore = [
    "codeofconduct.html",
    "contributing.html",
    "examples.html",
]
