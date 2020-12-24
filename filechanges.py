from pathlib import Path
import sqlite3
from typing import Tuple
import contextlib

def get_db_file() -> Path:
    return Path("acme.db")


def get_db_connection(database_file: Path) -> sqlite3.Connection:
    """ Return a connection instance from the given database_file. """
    return sqlite3.connect(database_file)

def run_cmd(query: str, execute_commit: bool):
    """Run a specific command on the SQLite DB"""
    with contextlib.closing( get_db_connection(get_db_file())) as connection:
        if connection:
             with contextlib.closing(connection.cursor()) as cursor:
                cursor.execute(query)
                if execute_commit:
                    connection.commit()
            

def create_table(table_name: str):
    """ Create a table and a INDEX. """
    with contextlib.closing( get_db_connection(get_db_file())) as connection:
        if connection:
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (name TEXT not NULL, mdf5 );"
            create_index_table_query = f"CREATE INDEX IF NOT EXISTS idxfile ON {table_name} (name)"

            with contextlib.closing(connection.cursor()) as cursor:
                cursor.execute(create_table_query)
                cursor.execute(create_index_table_query)
                connection.commit()


create_table('acme')
