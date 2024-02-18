<!--
Create a changelog entry for every new user-facing change (where the "users" are plugin developers).
Please respect the following instructions:
- Group changes by date, with newest changes first.
- Prefix your changes with either [Bugfix], [Improvement], [Feature], [Security], [Deprecation].
- You may optionally append "(by @<author>)" at the end of the line, where "<author>" is either one (just one)
  of your GitHub username, real name or affiliated organization. -->

# Changelog

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
