<!--
Create a changelog entry for every new user-facing change (where the "users" are plugin developers).
Please respect the following instructions:
- Group changes by date, with newest changes first.
- Prefix your changes with either [Bugfix], [Improvement], [Feature], [Security], [Deprecation].
- You may optionally append "(by @<author>)" at the end of the line, where "<author>" is either one (just one)
  of your GitHub username, real name or affiliated organization. -->

# Changelog

## 2025-01-30

- [Improvement] Migrate from `setup.py` (setuptools) to `pyproject.toml` (hatch) (by @CodeWithEmad).

## 2025-01-03

- [Improvement] Added support for tutor v19 (by @Danyal-Faheem).

## 2024-07-25

- [Improvement] Plugin's generated `README.rst` file is now more dynamic and compatibility for Python 3.7 is dropped (by @CodeWithEmad)
- [Bugfix] `.github` directory creation issue resolved (by @CodeWithEmad)

## 2024-01-01

- [Improvement] Happy New Year!
  - Fix compatibility issue with Python 3.12 by removing dependency on `pkg_resources`.
  - Cookiecutter hooks to check input data validation.
  - Various licenses support.
  - New documentation format.
  - GitHub Actions for new plugins.
  - `dev` mode added to extra entries.
  (by @CodeWithEmad).

## 2023-11-21

- [Improvement] Mark compatibility with python 3.11 and 3.12 (by @CodeWithEmad).

## 2023-11-06

- [Improvement] Recommend putting job scripts under "tasks" directory instead of "jobs", for consistency with official plugins (by @CodeWithEmad).
- [Improvement] Start keeping a changelog (by @kdmccormick).
