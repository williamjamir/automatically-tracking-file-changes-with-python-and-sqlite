from pathlib import Path
import sqlite3


def get_db_connection(database_file: Path) -> sqlite3.Connection:
    """ Return a connection instance from the given database_file. """
    return sqlite3.connect(database_file)


connection = get_db_connection(Path("acme.db"))