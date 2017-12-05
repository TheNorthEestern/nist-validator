# NIST Password Validator

This module is a NIST compliant password validator for use anywhere you need to check the validity of a password.

# Getting Started

This project is only compatible with **Python 3**, so you'll need to make sure you [have it installed before proceeding](https://www.google.com/search?q=how+to+install+python+3).

Once you have that out of the way, install the dependencies for this project. Feel free to use your favorite environment manager, but do note that this package was built and tested with [_virtualenv_](https://virtualenv.pypa.io/en/stable/). The instructions below make use of [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), so you'll need to install that as well to follow along.

# Usage

```bash
$ cat <input_passwords> | ./password_validator <password_list>
```

# Example

```bash
$ mkvirtualenv password_validator python=$(which python3)
$ pip install -r requirements.txt
$ chmod +x password_validator.py
$ cat input_passwords.txt | ./password_validator.py weak_password_list.txt
``` 
# Running Tests

```bash
$ pytest tests.py
```
