# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:50:58 2021

@author: yaobv
"""
import pandas as pd
import sqlite3 as sql
import psycopg2 as pg2


file = r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Databases\data\titanic.csv'

df = pd.read_csv(file)
df.columns = df.columns.str.lower()
df = df.rename(columns = {'siblings/spouses aboard' : 'sibling_or_spouse', 
                          'parents/children aboard' : 'parents_or_children'})

conn = sql.connect('titanic.sql')

df.to_sql('titanic', conn, if_exists = 'replace')

HOST = 'ziggy.db.elephantsql.com'
DBNAME = 'sayxwhec'
USER = 'sayxwhec'
PASSWORD = 'eUZz0cxrO9Ya5LdmeyAp5iSpGHszLCAH'

pg_conn = pg2.connect(dbname = DBNAME, host = HOST,
                      user = USER, password = PASSWORD)

pg_curs = pg_conn.cursor()

CREATE_titanic_table = """
    CREATE TABLE IF NOT EXISTS titanic (
        passenger_id SERIAL PRIMARY KEY,
        survived INT NOT NULL,
        pclass INT NOT NULL,
        name VARCHAR(90) NOT NULL,
        sex VARCHAR(6) NOT NULL,
        age INT NOT NULL,
        sibling_or_spouse INT NOT NULL,
        parents_or_children INT NOT NULL,
        fare FLOAT NOT NULL
        );
"""

pg_curs.execute(CREATE_titanic_table)
pg_conn.commit()
pg_curs.close()

INSERT_titanic_table = """
    INSERT INTO titanic (
        passenger_id,
        survived,
        pclass,
        name,
        sex,
        age,
        sibling_or_spouse,
        parents_or_children,
        fare
        )
    VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        );
"""

sql_curs = conn.cursor()

titanic_data = sql_curs.execute("SELECT * FROM titanic").fetchall()

for p in titanic_data:
    pg_curs = pg_conn.cursor()
    pg_curs.execute(INSERT_titanic_table, p)
    pg_conn.commit()
    pg_curs.close()
    