# Backend Manual

## Requirements:

- Google OAuth 2.0 client keys
- Python3
- Pip
- ...

## Run server:

1. Move into the base directory of "backend" within the command line.
2. Activate the Python environment (follow the section titled "Environment Configuration").
3. Set the following environment variables in your terminal session: `FLASK_APP = "RAMMN"` and `FLASK_ENV = "development"` (note, make sure `FLASK_APP` matches the name of your flask app folder).
4. Call the flask module by typing: `Flask run` and `python -m flask run`

## Installation Instructions:

1. Type `pip install` (this will get any dependencies)

## Run tests:

1. Follow the "Installation Instructions."
2. Type `pytest` in the backend app directory.

## Environment Configuration:

To activate the environment varibles, type the following in your CLI:
- Bash : `. venv/bin/activate`
- Windows : `venv\Scripts\activate`

Warning: windows users may need to type `Set-ExecutionPolicy Unrestricted -Scope Process` if the execution is in PowerShell. This command changes process restrictions for the current PowerShell executio environment.

To list the installed packages for the environment, type:
- `pip freeze --local` (note, run this after activation)

## Hosting (Heroku):

## Database (PostgreSQL):

For this project we used the structured query language PostgreSQL. Reasons for using this database model include: relational data model for powerful representaion of data relationships, transaction safe queries, and free remote database access via Heroku.

Use [PGADMIN](https://www.pgadmin.org/download/) for a free GUI database administration tool.

## TODO:

- get database url from the path