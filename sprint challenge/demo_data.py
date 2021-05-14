# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:10:00 2021

@author: yaobv
"""
import sqlite3 as sql

conn = sql.connect('demo_data.sqlite3')
curs = conn.cursor()


def execute_query(conn, query, read=True):
    """
    There are 3 rows.
    There are 2 rows with x and y >= 5.
    There are 2 unique values in y
    """

    curs = conn.cursor()
    curs.execute(query)
    if read:
        result = curs.fetchall()
        return result
    else:
        conn.commit()
        curs.close()
        return "It has been written."


CREATE_demo_table = """
    CREATE TABLE IF NOT EXISTS demo (
        s CHAR(4),
        x INT NOT NULL,
        y INT NOT NULL
        );
"""

curs.execute(CREATE_demo_table)
conn.commit()
curs.close()

values_to_insert = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

INSERT_INTO_demo = """
    INSERT INTO demo (
        s,
        x,
        y
        )
    VALUES (
        ?,
        ?,
        ?)
"""

for values in values_to_insert:
    curs = conn.cursor()
    curs.execute(INSERT_INTO_demo, values)
    conn.commit()
    curs.close()


ROW_count = """
    SELECT COUNT(*)
    FROM demo;
"""

XYboth_atleast_5 = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 
    AND y >= 5;
"""

UNIQUE_y = """
    SELECT COUNT(DISTINCT(y))
    FROM demo;
"""

row_count = execute_query(conn, ROW_count)
xy_at_least_5 = execute_query(conn, XYboth_atleast_5)
unique_y = execute_query(conn, UNIQUE_y)
