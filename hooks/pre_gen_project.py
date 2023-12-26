# https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html

import re
import sys


# The content of this string is evaluated by Jinja, and plays an important role.
# It updates the cookiecutter context to trim leading and trailing spaces
"""
{{ cookiecutter.update({ "plugin_name": cookiecutter.plugin_name | trim }) }}
{{ cookiecutter.update({ "package_name": cookiecutter.package_name | trim }) }}
{{ cookiecutter.update({ "module_name": cookiecutter.module_name | trim }) }}
{{ cookiecutter.update({ "email": cookiecutter.email | trim }) }}
{{ cookiecutter.update({ "tutor_version": cookiecutter.tutor_version | int }) }}
"""

TERMINATOR = "\x1b[0m"
ERROR = "\x1b[1;31m [ERROR]: "
WARNING = "\x1b[1;33m [WARNING]: "
VALID_REGEX = r"^[-_a-zA-Z0-9]+$"
EMAIL_REGEX = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
to_validate = {
    "plugin_name": "{{ cookiecutter.plugin_name }}",
    "package_name": "{{ cookiecutter.package_name }}",
    "module_name": "{{ cookiecutter.module_name }}",
}


def check_validation():
    for key, value in to_validate.items():
        if not value:
            print(ERROR + f"{key.title().replace('_', ' ')} can't be empty")
            sys.exit(1)
        if not re.match(VALID_REGEX, value):
            print(
                ERROR
                + f"{key.title().replace('_', ' ')} is not a valid name!"
                + TERMINATOR
            )
            sys.exit(1)


def check_email():
    email = "{{ cookiecutter.email | trim}}"
    if not re.match(EMAIL_REGEX, email):
        print(ERROR + f"{email} is not a valid email address!" + TERMINATOR)
        sys.exit(1)


def check_repo_is_github():
    if (
        "github.com" not in "{{ cookiecutter.git_repo.lower() | trim }}"
        and "{{ cookiecutter.include_ci }}" == "y"
    ):
        print(
            WARNING
            + "Provided repository URL is not associated with a GitHub repository! GitHub CI files won't be generated."
            + TERMINATOR
        )
        "{{ cookiecutter.update({ 'include_ci': 'n' }) }}"


if __name__ == "__main__":
    check_validation()
    check_email()
    check_repo_is_github()
