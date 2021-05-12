# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:17:07 2021

@author: yaobv
"""
import sqlite3
from queries import EXTRACT_chars

conn = sqlite3.connect(r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Databases\data\rpg_db.sqlite3')

curs = conn.cursor()

curs.execute(EXTRACT_chars).fetchall()
