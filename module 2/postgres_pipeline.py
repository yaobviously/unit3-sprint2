# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:06:47 2021

@author: yaobv
"""
import psycopg2 as pg2
import sqlite3
from queries import EXTRACT_chars, INSERT_INTO_char_table

DBNAME = 'editacdx'
USER = 'editacdx'
HOST = 'queenie.db.elephantsql.com'
PASSWORD = 'Ux-Q4r8VDmjJLQMs63QyA_7hRlY4pzFj'

SQLITE_DB = r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Databases\data\rpg_db.sqlite3'

def create_connections(dbname, user, host, password, sqldb = SQLITE_DB):
    """ creates a connection to remote Postgres and local SQLite """
    pg_conn = pg2.connect(dbname = dbname, user = user,
                          host = host, password = password)
    sql_conn = sqlite3.connect(sqldb)
    
    return pg_conn, sql_conn


def execute_query(conn, query, read = True):
    """ fetches data and returns it or writes data and commits it """
    curs = conn.cursor()
    curs.execute(query)
    if read:
        results = curs.fetchall()
        curs.close()
        return results
    else:
        conn.commit()
        curs.close()
        return "CUD Query Executed"
    
    
if __name__ == "__main__":
    pg_conn, sql_conn = create_connections(DBNAME, USER, HOST, PASSWORD)
    pull_results = execute_query(sql_conn, EXTRACT_chars)
    ### results structure = [(a1, a2, a3, a4.. a9), (...), (...)]
    # pg_curs = pg_conn.cursor()
    
    for character in pull_results:
        pg_curs = pg_conn.cursor()    
        pg_curs.execute(INSERT_INTO_char_table, character)
        pg_conn.commit()
        pg_curs.close()
