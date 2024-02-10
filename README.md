# datafun-05-sql

##Project 05

##Overview
    Project 5 integrates Python and SQL, focusing on database interactions using SQLite. \n
    This project introduces logging, a useful tool for debugging and monitoring projects, \n 
    and involves creating and managing a database, building a schema, and performing various SQL operations, \n 
    including queries with joins, filters, and aggregations.

--Environment Setup
    ## The project requires the following external modules, so a virtual environment is recommended.
        ##pandas
        ##pyarrow

  1.**Create** and **activate** the project virtual environment.  Start in GitHub and create a new repository.
  Add a README.md file.
 
  2. Open VS Code terminal.

  2. Install all required packages into your local project virtual environment.

  3. After installing the required dependencies, update or generate a  **requirements.txt** file.
  
  4. Add a **.gitignore** file to your project with useful entries. See [.gitignore](.gitignore) example.  Add .venv/ and .vscode/ to the .gitignore.
  5. Document the steps and commands in your README.md.

  Terminal Commands:
  ```Powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  py -m pip freeze > requirements.txt
  ```

  ## Install pandas
  ## Install pyarrow

  --Project Start
    """In python file create a docstring with a brief introduction to you project"""

  --Import Dependencies (At the top of the project, after the Introduction)  ## Install any external packages \n 
  (those not in the Python Standard Library) into your active project with virtual environment first. 

  ```Powershell
  pip install pandas
  pip install pyarrow
  ```

  ## Freeze requirements
  ```Powershell
  py -m pip freeze > requirements.txt
  ```

## Push to GitHub

```Powershell
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/project-05.git
git push -u origin main
```

# add a data folder to your project

```Powershell
git add data
```
Add csv files to the data folder.

```Powershell
git commit -m "add data folder"
```

# create the database

import sqlite3
import pandas as pd
import pathlib
import pyarrow

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()