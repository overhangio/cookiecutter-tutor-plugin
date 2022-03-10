import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.md"), "rt", encoding="utf8") as f:
        return f.read()


setup(
    name="{{ cookiecutter.package_name }}",
    use_scm_version=True,
    url="{{ cookiecutter.git_repo }}",
    project_urls={
        "Code": "{{ cookiecutter.git_repo }}",
        "Issue tracker": "{{ cookiecutter.git_repo }}/issues",
    },
    license="{{ cookiecutter.license }}",
    author="{{ cookiecutter.author }}",
    description="{{ cookiecutter.plugin_name}} plugin for Tutor",
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor"],
    setup_requires=["setuptools-scm"],
    entry_points={
        "tutor.plugin.v0": [
            "{{ cookiecutter.plugin_name }} = {{ cookiecutter.module_name }}.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
