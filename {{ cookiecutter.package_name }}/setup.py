import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(
    os.path.join(here, "{{ cookiecutter.module_name }}", "__about__.py"),
    "rt",
    encoding="utf-8",
) as f:
    exec(f.read(), about)

setup(
    name="{{ cookiecutter.package_name }}",
    version=about["__version__"],
    url="{{ cookiecutter.git_repo }}",
    project_urls={
        "Code": "{{ cookiecutter.git_repo }}",
        "Issue tracker": "{{ cookiecutter.git_repo }}/issues",
    },
    license="{{ cookiecutter.license }}",
    author="{{ cookiecutter.author }}",
    description="{{ cookiecutter.plugin_name}} plugin for Tutor",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=["tutor-openedx"],
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
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
