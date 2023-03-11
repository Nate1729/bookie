from typing import Optional
from enum import Enum 

class InputError(Exception):
    pass

class FileExtensions(str, Enum):
    CSV = 'csv'

def get_file_extension(file_name: str) -> Optional[str]:
    if '.' not in file_name:
        return None
    return file_name.split('.')[-1]

def validate_arguments(args: list[str]) -> str:
    """Validates command line arguments.
    raises an exception for an invalid argument
    or returns a string of the correct file name
    to process.
    """
    if len(args) < 2:
        raise InputError("You must pass an input file!")
    if len(args) > 2:
        raise InputError("Too many arugments!")

    _, file_name = args

    if get_file_extension(file_name) != FileExtensions.CSV:
        raise InputError("The file must be a csv file!")

    return file_name

