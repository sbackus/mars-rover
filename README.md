# Mars Rover Kata (Python)

A Python implementation of the Mars Rover Kata, using VSCode, facilitated by David Sturgis as part of the Boston Software Crafters meetup on April 13th, 2020.

Team Members: (TBD)

# To Install Requirements

Set up a virtual environment of your choice:
Intro to VirtualEnvs: https://docs.python.org/3/tutorial/venv.html
Popular tools:
* PipEnv: https://pipenv-fork.readthedocs.io/en/latest/
* Poetry: https://python-poetry.org/docs/

After activating your virtual environment, install the requirements:

```pip install -r requirements.txt```

# To Run the Tests

```pytest```

# To Run the Tests with Coverage

```pytest --cov=kata .```

# To Run in Watch Mode with Coverage
(Will automatically re-run tests with coverage when files are edited)

```ptw --runner "pytest --cov=kata"```
