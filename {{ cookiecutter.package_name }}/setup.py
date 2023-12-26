import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "{{ cookiecutter.module_name }}", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="{{ cookiecutter.package_name }}",
    version=ABOUT["__version__"],
    url="{{ cookiecutter.git_repo }}",
    project_urls={
        "Code": "{{ cookiecutter.git_repo }}",
        "Issue tracker": "{{ cookiecutter.git_repo }}/issues",
    },
    license="{{ cookiecutter.license }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor>={{ cookiecutter.tutor_version }}.0.0,<{{ cookiecutter.tutor_version + 1 }}.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>={{ cookiecutter.tutor_version }}.0.0,<{{ cookiecutter.tutor_version + 1 }}.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "{{ cookiecutter.plugin_name }} = {{ cookiecutter.module_name }}.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        {%- if cookiecutter.license == "AGPLv3" %}
        "License :: OSI Approved :: GNU Affero General Public License v3",
        {%- elif cookiecutter.license == "Apache 2.0" %}
        "License :: OSI Approved :: Apache Software License",
        {%- elif cookiecutter.license == "BSDv3" %}
         "License :: OSI Approved :: BSD License",
        {%- elif cookiecutter.license == "MIT" %}
        "License :: OSI Approved :: MIT License",
        {%- elif cookiecutter.license == "Not open source" %}
        "License :: Other/Proprietary License",
        {%- endif %}
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
