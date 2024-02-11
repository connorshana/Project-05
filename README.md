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
    Push to Git (doe this frequently throught the project).
    
         ```Powershell
    git commit -m "add data folder"
    ```
9. Add csv files to the data folder.  In this project authors.csv and books.csv were used
    Import data to cvs files:
       authors:
   
        author_id,first,last
        10f88232-1ae7-4d88-a6a2-dfcebb22a596,Harper,Lee
        c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70,George,Orwell
        e0b75863-866d-4db4-85c7-df9bb8ee6dab,F. Scott,Fitzgerald
        7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d,Aldous,Huxley
        8d8107b6-1f24-481c-8a21-7d72b13b59b5,J.D.,Salinger
        0cc3c8e4-e0c0-482f-b2f7-af87330de214,Ray,Bradbury
        4dca0632-2c53-490c-99d5-4f6d41e56c0e,Jane,Austen
        16f3e0a1-24cb-4ed6-a50d-509f63e367f7,J.R.R.,Tolkien
        06cf58ab-90f1-448d-8e54-055e4393e75c,J.R.R.,Tolkien
        6b693b96-394a-4a1d-a4e2-792a47d7a568,J.K.,Rowling
       
       books:  book_id,title,year_published,author_id
        d6f83870-ff21-4a5d-90ab-26a49ab6ed12,To Kill a Mockingbird,1960,10f88232-1ae7-4d88-a6a2-dfcebb22a596
        0f5f44f7-44d8-4f49-b8c4-c64d847587d3,1984,1949,c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70
        f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2,The Great Gatsby,1925,e0b75863-866d-4db4-85c7-df9bb8ee6dab
        38e530f1-228f-4d6e-a587-2ed4d6c44e9c,Brave New World,1932,7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d
        c2a62a4b-cf5c-4246-9bf7-b2601d542e6d,The Catcher in the Rye,1951,8d8107b6-1f24-481c-8a21-7d72b13b59b5
        3a1d835c-1e15-4a48-8e8c-b12239604e98,Fahrenheit 451,1953,0cc3c8e4-e0c0-482f-b2f7-af87330de214
        c6e67918-e509-4a6b-bc3a-979f6ad802f0,Pride and Prejudice,1813,4dca0632-2c53-490c-99d5-4f6d41e56c0e
        be951205-6cc2-4b3d-96f1-7257b8fc8c0f,The Hobbit,1937,16f3e0a1-24cb-4ed6-a50d-509f63e367f7
        dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f,The Lord of the Rings,1954,06cf58ab-90f1-448d-8e54-055e4393e75c
        ca8e64c3-1e67-47f5-82cc-3e4e30f63b75,Harry Potter and the Philosopher's Stone,1997,6b693b96-394a-4a1d-a4e2-                792a47d7a568


11. Create the database

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
        import logging

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

