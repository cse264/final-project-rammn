# Backend Manual

(Description here)

# Requirements:

- Google OAuth 2.0 client keys
- Python3
- Pip
- ...

# Run server:

1. Move into the base directory of "backend" within the command line.
2. Activate the Python environment (follow the section titled "Environment Configuration").
3. Set the following environment variables in your terminal session: `FLASK_APP = "RAMMN"` and `FLASK_ENV = "development"` (note, make sure `FLASK_APP` matches the name of your flask app folder).
4. Call the flask module by typing: `Flask run` and `python -m flask run`

# Installation Instructions:

Installation will ensure that the execution environment has all Python modules installed (including the RAMMN Flask project).

1. Follow the "Environment Configuration" section to ensure a valid "venv" is in your project.
2. Type `pip install -r requirements.txt` (this will get any dependencies)

# Environment Configuration:

Follow these steps to create and run the Python Virtual Environment (refered to as venv):

## Creating the Environment:
1. Change current working directory into the "backend" folder from "root".
2. Type `python -m venv venv` in console (or similar command for invoking venv).
3. Activate the script by typing: `. venv/bin/activate` (Bash) or `venv\Scripts\activate` (Windows).
4. Type `pip install -r requirements.txt`.

Warning: windows users may need to type `Set-ExecutionPolicy Unrestricted -Scope Process` if the execution is in PowerShell. This command changes process restrictions for the current PowerShell execution environment.

## Using the Environment:
1. Assuming the "venv" folder was created correctly, change current working directory into the "backend" folder "from "root".
2. Activate the script by typing: `. venv/bin/activate` (Bash) or `venv\Scripts\activate` (Windows).
3. Check installed packages by typing `pip freeze --local`.

# Run tests:

1. Follow the "Installation Instructions."
2. Type `pytest` in the backend app directory.

# Hosting (Heroku):

1. Update requirements by typing: `pip freeze > requirements.txt`.
2. Stage any changes to the repository to the remote heroku branch.
3. Push staged changes to trigger heroku deploy.

# Database (PostgreSQL):

For this project we used the structured query language PostgreSQL. Reasons for using this database model include: relational data model for powerful representaion of data relationships, transaction safe queries, and free remote database access via Heroku.

Use [PGADMIN](https://www.pgadmin.org/download/) for a free GUI database administration tool.