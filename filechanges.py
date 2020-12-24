import os
import sqlite3


def getbasefile():
    return os.path.splitext(os.path.basename(__file__))[0]


def connectdb():
    dbfile = getbasefile() + ".db"
    return sqlite3.connect(dbfile)


connection = connectdb()