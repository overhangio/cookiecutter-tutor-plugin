# https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html

import os
import shutil
import subprocess


TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;34m [INFO]: "
HINT = "\x1b[3;34m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "
ERROR = "\x1b[1;31m [ERROR]: "
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))


def check_git_installed():
    try:
        subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT)
        return True
    except Exception:
        return False


def initial_git():
    if check_git_installed():
        try:
            subprocess.call(["git", "init", "-q"])
            if "{{ cookiecutter.git_repo }}":
                subprocess.call(
                    ["git", "remote", "add", "origin", "{{ cookiecutter.git_repo }}"]
                )
            print(SUCCESS + "Git repository created." + TERMINATOR)
        except Exception:
            print(ERROR + "Git repository creation failed." + TERMINATOR)
    else:
        print(WARNING + "Git is not installed. Initial step ignored." + TERMINATOR)


if __name__ == "__main__":
    if "{{ cookiecutter.init_git }}" == "y":
        initial_git()
    if "{{ cookiecutter.license }}" == "Not open source":
        remove_file("LICENSE.txt")
    if "{{ cookiecutter.include_ci }}" == "n":
        remove_dir(".github")
    print(HINT + "Project initialization completed. \U0001F389" + TERMINATOR)
    print(HINT + "Happy hacking!" + TERMINATOR)
