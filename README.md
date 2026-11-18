# Student Task Manager

Project status: In Development

A Python console application for managing student tasks.

## Features

- Add tasks with title validation
- Display task identifiers, titles, and completion status
- Mark selected tasks as completed
- Delete tasks using valid identifiers
- Automated unit tests and GitHub Actions continuous integration

## Why branches are useful

Branches let feature work happen in isolation. Each feature can be developed,
reviewed, and tested without disturbing main. They support parallel work and
safe pull request review, so only finished work is merged into the release branch.

## Setup

```text
git clone https://github.com/somansaeed1/studenttaskmanager.git
cd studenttaskmanager
python main.py
```

## Usage

Use the numbered menu to add, display, complete, delete, or exit.
Task identifiers are shown when tasks are displayed.

## Test Instructions

Run the unittest suite from the repository root:

```text
python -m unittest discover -s tests -v
```
