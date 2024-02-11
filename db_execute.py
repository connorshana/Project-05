# Imports
import pandas as pd
import pyarrow
import pathlib
import logging
import sqlite3
import csv


logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():
    db_filepath = pathlib.Path("C:\\Users\\blehman\\Projects\\datafun-05-sql\\project.db")
    #execute_sql_from_file(db_filepath, 'sql_file/create_tables.sql')
    execute_sql_from_file(db_filepath, 'sql_file/insert_records.sql')
    execute_sql_from_file(db_filepath, 'sql_file/update_records.sql')
    execute_sql_from_file(db_filepath, 'sql_file/delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_join.sql')

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()