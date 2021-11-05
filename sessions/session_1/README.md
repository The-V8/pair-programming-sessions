# Challenge 1

## Challenge Description

`Two-fer` or `2-fer` is short for two for one. One for you and one for me.

Given a name, return a string with the message:

```text
One for name, one for me.
```

Where "name" is the given name.

However, if the name is missing, return the string:

```text
One for you, one for me.
```

Here are some examples:

|Name      |String to return
|:---------|:------------------
|Alexander |One for Alice, one for me.
|Oliver    |One for Oliver, one for me.
|          |One for you, one for me.
|Peter     |One for Peter, one for me.

## Coding & Testing Setup

1. Have Python (at least version 3.5) installed. Download at [python.org](https://www.python.org/)
1. [optional] Start a virtual environment for the challenges by running: `python -m venv .venv` in the root of the repo
1. [optional] Use your virtual environment by running: `source .venv/bin/activate` on Linux, Mac and WSL2
1. Install the requirements by running: `pip install -r requirements.txt` from the root of the repo
1. Run the tests with [Pytest](https://github.com/bats-core/bats-core#installation) from the current session folder:

```bash
pytest tests/
```

## Acceptance criteria

- Write a program in Python that implements the Two-Fer functionality as described in `sessions/session_1/two_fer.py`
- Test the given example behavior with pytest
- You solved the problem with the driver/navigator approach to pair programming
