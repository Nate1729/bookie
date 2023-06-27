# Standard Library
import sys, csv
from typing import Optional

# bookie imports
from bookie import summary, arg_parser, models


def process_file(file_path: str) -> Optional[list[models.Receipt]]:
    with open(file_path, "r") as f:
        entries = [models.receipt_from_dict(line) for line in csv.DictReader(f)]
        return entries


if __name__ == "__main__":
    try:
        file_name = arg_parser.validate_arguments(sys.argv)
    except arg_parser.InputError as e:
        print(f'There was an issue with the inputs.\nError: "{e}"')
        sys.exit(1)

    data = process_file(file_name)
    if data is None:
        sys.exit(1)
    summary.summarize(data)
