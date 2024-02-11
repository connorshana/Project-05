Shana Connor
# datafun-05-sql

# Project 05

"""Read.me file to demonstrate capabilities and documentation for Project 05."""

# Overview
    Project 5 integrates Python and SQL, focusing on database interactions using SQLite. \n
    This project introduces logging, a useful tool for debugging and monitoring projects, \n 
    and involves creating and managing a database, building a schema, and performing various SQL operations, \n 
    including queries with joins, filters, and aggregations.

# Environment Setup
 
1. Start in GitHub and create a new repository.
      Add a README.md file.
2. Open VS Code terminal.  Clone your Git repository into VS Code.  Copy the URL of your Github repo and paste into 
         ```git clone (URL here)```
3. **Create** and **activate** the project virtual environment.
    Terminal Commands:
  ```Powershell
  python -m venv .venv
  .venv\Scripts\Activate```

4. Import Dependencies.  Install any external packages (those not in the Python Standard Library) into your active project with virtual environment first.
  ```Powershell
  pip install pandas
  pip install pyarrow
  ```

5.Create a requirements.txt file and list your dependencies:
    For this project:
        pandas and pyarrow
6.Import Logging:
    Logging is recommended for most professional projects. Implement logging to enhance debugging and maintain a record of     program execution.

        1.Configure logging to write to a file named log.txt.
        2.Log the start of the program using logging.info().
        3.Log the end of the program using logging.info().
        4.Log exceptions using logging.exception().
        5.Log other major events using logging.info().
        6.Log the start and end of major functions using logging.debug().

    ```import logging```
    # Configure logging to write to a file, appending new logs to the existing file
    ```logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %        (message)s')```

    ```logging.info("Program started") # add this at the beginning of the main method
    logging.info("Program ended")  # add this at the end of the main method```

7. Install all required packages into your local project virtual environment.
    ```pip install -r requirements.txt```
      
 8. Freeze dependencies
        ```py -m pip freeze > requirements.txt``` 
  
 9. Add a **.gitignore** file to your project with:
     .venv/ and .vscode/
    
        ## Core project requirements:
            .venv
            requirements.txt
            gitignore
            log.txt
        
7. Push to GitHub

    ```Powershell
    git init
    git add .
    git commit -m "initial commit"
    git branch -M main
    git remote add origin https://github.com/yourusername/project-05.git
    git push -u origin main
    ```

8. Add a data folder to your project

    ```Powershell
        git add data
        ```
9. Add csv files to the data folder.

    ```Powershell
    git commit -m "add data folder"
    ```

10. Create the database

        ```import sqlite3
        import pandas as pd
        import pathlib
        import pyarrow```

Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

```def create_database():
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
    main()```

11. Create SQL files:
        1. Create_tables.sql - create your database schema using sql
        2. Insert_records.sql - insert at least 10 additional records into each table.
        3. Update_records.sql - update 1 or more records in a table.
        4. Delete_records.sql - delete 1 or more records from a table.
        5. Query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
        6. Query_filter.sql - use WHERE to filter data based on conditions.
        7. Query_sorting.sql - use ORDER BY to sort data.
        8. Query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
        9. Query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

12.  Find extension to view tables.  #SQLite Viewer.

13.  Intergrate Python and SQL.  Use python:

    ```import sqlite3

        def execute_sql_from_file(db_filepath, sql_file):
        with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")```

14. Define Main Function for SQL Operations Script.
    Implement a main() function to execute the project SQL operations logic.

        ```def main():
        db_filepath = 'your_database.db'

        # Create database schema and populate with data
        execute_sql_from_file(db_filepath, 'insert_records.sql')
        execute_sql_from_file(db_filepath, 'update_records.sql')
        execute_sql_from_file(db_filepath, 'delete_records.sql')
        execute_sql_from_file(db_filepath, 'query_aggregation.sql')
        execute_sql_from_file(db_filepath, 'query_filter.sql')
        execute_sql_from_file(db_filepath, 'query_sorting.sql')
        execute_sql_from_file(db_filepath, 'query_group_by.sql')
        execute_sql_from_file(db_filepath, 'query_join.sql')

        logging.info("All SQL operations completed successfully")```

15. Execute the Script.
    Ensure the main function only executes when the script is run directly, not when imported as a module by using             standard boilerplate code.

