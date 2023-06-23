import os
import shutil
import sys
from pathlib import Path

import nox

python_versions = ["3.11", "3.10", "3.9", "3.8"]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "linting",
    "safety",
    "tests",
    "docs-build",
)


@nox.session(python=python_versions[0])
def linting(session) -> None:
    """Lint using pre-commit."""
    args = session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    session.install(
        "pre-commit",
        "pre-commit-hooks",
        "bandit",
        "black",
        # "darglint",
        "flake8",
        # "flake8-bugbear",
        "flake8-docstrings",
        "isort",
        # "pep8-naming",
        "pyupgrade",
    )
    session.run("pre-commit", *args)


@nox.session(python=python_versions[0])
def safety(session) -> None:
    """Scan dependencies for insecure packages."""
    session.install(".", "safety")
    session.run("safety", "check")


@nox.session(python=python_versions)
def mypy(session) -> None:
    """Type-check using mypy."""
    args = session.posargs or ["src", "tests", "docs/conf.py"]
    session.install(".")
    session.install("mypy", "pytest")
    session.run("mypy", *args)
    if not session.posargs:
        session.run("mypy", f"--python-executable={sys.executable}", "noxfile.py")


@nox.session(python=python_versions)
def tests(session) -> None:
    """Run the test suite."""
    session.install(".")
    session.install("coverage[toml]", "pexpect", "pytest", "pygments")
    try:
        session.run("coverage", "run", "--parallel", "-m", "pytest", *session.posargs)
    finally:
        if session.interactive:
            session.notify("coverage", posargs=[])


@nox.session(python=python_versions[0])
def coverage(session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["report"]

    session.install("coverage[toml]")

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)


@nox.session(name="docs-build", python=python_versions[0])
def docs_build(session) -> None:
    """Build the documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    if not session.posargs and "FORCE_COLOR" in os.environ:
        args.insert(0, "--color")

    session.install(".")
    session.install("sphinx", "furo", "myst-parser")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-build", *args)


@nox.session(python="3.9")
def docs(session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = session.posargs or ["--open-browser", "docs", "docs/_build"]
    session.install(".")
    session.install("sphinx", "sphinx-autobuild", "furo", "myst-parser")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-autobuild", *args)
