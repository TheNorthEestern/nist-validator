#!/usr/bin/env python3
"""Password Validator

Usage:
  password_validator.py <filename>
"""
import sys
from validators.nist import NISTValidator
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version="Password Validator 1.0.0")
    input_stream = sys.stdin.read().splitlines()
    try:
        with open(arguments["<filename>"]) as password_file:
            file_contents = password_file.read().splitlines()
            validator = NISTValidator(input_stream=input_stream, password_list=file_contents)
            validator.validate()
    except FileNotFoundError:
        print("The specified file could not be found.")
