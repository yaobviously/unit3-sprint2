# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:17:07 2021

@author: yaobv
"""
import sqlite3
import psycopg2 as pg2
from postgres_pipeline import HOST, DBNAME, USER, PASSWORD, create_connections


SQL_DB = r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Databases\data\rpg_db.sqlite3'


pg_conn, sql_conn = create_connections(dbname = DBNAME, user = USER,
                                       host = HOST, password = PASSWORD)

curs_sql = sql_conn.cursor()
curs_pg = pg_conn.cursor()

armory_table = curs_sql.execute("SELECT * FROM armory_item").fetchall()

CREATE_armory_table = """
    CREATE TABLE IF NOT EXISTS armory_table (
        item_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        val INT NOT NULL,
        weight INT NOT NULL
        );
"""

curs_pg.execute(CREATE_armory_table)
pg_conn.commit()
curs_pg.close()

INSERT_armory_table = """
    INSERT INTO armory_table (
        item_id,
        name,
        val,
        weight
        )
    VALUES (
        %s,
        %s,
        %s,
        %s
        )
"""

for item in armory_table:
    curs_pg = pg_conn.cursor()
    curs_pg.execute(INSERT_armory_table, item)
    pg_conn.commit()
    curs_pg.close()

