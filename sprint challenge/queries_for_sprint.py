# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:27:44 2021

@author: yaobv
"""

DROP_demo_table = """
    DROP TABLE demo;
"""

CREATE_demo_table = """
    CREATE TABLE IF NOT EXISTS demo (
        s CHAR(4),
        x INT NOT NULL,
        y INT NOT NULL
        );
"""


ALL_table_names = """
    SELECT sql FROM sqlite_master
"""


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