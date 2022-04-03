# Backend Manual

## Requirements:

- Google OAuth 2.0 client keys
- Python3
- Pip
- ...

## Run server:

1. Move into the base directory of "backend" within the command line.
2. Activate the Python environment (follow the section titled "Environment Configuration").
3. Call the flask module by typing: `python -m flask run`

## Installation Instructions:

Follow the following steps to install
- 

## Environment Configuration:

To activate the environment varibles, type the following in your CLI:
- Bash : `. venv/bin/activate`
- Windows : `venv\Scripts\activate`

Warning: windows users may need to type `Set-ExecutionPolicy Unrestricted -Scope Process` if the execution is in PowerShell. This command changes process restrictions for the current PowerShell executio environment.

To list the installed packages for the environment, type:
- `pip freeze --local` (note, run this after activation)

## TODO:

- get database url from the path