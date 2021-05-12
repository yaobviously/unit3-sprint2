# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:06:47 2021

@author: yaobv
"""
import psycopg2 as pg2
import sqlite3 

DBNAME = 'editacdx'
USER = 'editacdx'
HOST = 'queenie.db.elephantsql.com'
PASSWORD = 'Ux-Q4r8VDmjJLQMs63QyA_7hRlY4pzFj'

conn = pg2.connect(dbname = DBNAME,
                   user = USER,
                   host = HOST,
                   password = PASSWORD)

curs = conn.cursor()

