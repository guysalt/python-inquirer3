import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--mode", default="install", choices=["install", "inject"], help="Specify which mode to use"
    )
    parser.add_argument("-p", "--package", help="Specify which package to install")
    parser.add_argument("-pe", "--package-environment", help="Specify which package to install")

    options = parser.parse_args()
    mode = options.mode
    package_to_install = options.package
    package_environment = options.package_environment

    constraint_path = Path(".github", "workflows", "constraints.txt")
    with constraint_path.open(mode="r") as constraint_file:
        for line in constraint_file:
            constraint_package, version = line.split("==")
            if constraint_package == package_to_install:
                package_constraint = constraint_package

    if mode == "install":
        os.system(f"pipx {mode} {package_constraint}")  # nosec B605
    elif mode == "inject":
        os.system(f"pipx {mode} {package_environment} {package_constraint}")  # nosec B605


if __name__ == "__main__":
    main()
