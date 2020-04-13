# Mars Rover Kata (Python)

A Python implementation of the Mars Rover Kata, using VSCode, facilitated by David Sturgis as part of the Boston Software Crafters meetup on April 13th, 2020.

Team Members: (TBD)

# To Install Requirements

I recommend setting up a virtual environment of your choice, to keep this project's requirements separate from other Python stuff on your system.

( Intro to VirtualEnvs: https://docs.python.org/3/tutorial/venv.html )

I prefer PipEnv: https://pipenv-fork.readthedocs.io/en/latest/ since it both manages project depedencies and a virtual environment to contain them.

    Once PipEnv is installed, you can run
    ```pipenv sync```
    To ensure that all dependencies are installed and up to date, and
    ```pipenv shell```
    To get a shell that uses this new environment.

If you'd rather not use PipEnv, you can install the requirements manually with:

```pip install -r requirements.txt```

# To Run the Tests

```pytest```

# To Run the Tests with Coverage

```pytest --cov=kata .```

# To Run in Watch Mode with Coverage
(Will automatically re-run tests with coverage when files are edited)

```ptw --runner "pytest --cov=kata"```
