# Bookie

[![CI](https://github.com/Nate1729/bookie/actions/workflows/main.yml/badge.svg)](https://github.com/Nate1729/bookie/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Nate1729/bookie/branch/main/graph/badge.svg?token=Q1J7O5T153)](https://codecov.io/gh/Nate1729/bookie)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Bookie is a bookeeping command line tool. The idea behind this
came from me not wanting to use spreadsheets to have to handle all of my data.

# How to Use
Pull the repository down and install dependencies
```bash
poetry install
```

You need to have a `.csv` file with all the data in the proper format.
Proper format means having a header row which _at least_ includes
- `date` in `yyy-mm-dd HH:MM` format
- `vendor` in plain-text
- `amount` positive or negative number
    - no currency markings
    - no thousands separator
    - 2 or 0 decimal places
    - cents separator is a period `.`.

Lastly to run the command
```bash
poetry run bookie/main.py <file_path_to_csv>
```

# Running Test Suite
Make sure you have already run `poetry install` so `pytest` is installed.
Assuming you have already done that, you can run
```bash
poetry run pytest
```

If you would like to get test coverage as well you will need to add
the `--cov` flag like this
```bash
poetry run pytest --cov=bookie
```
