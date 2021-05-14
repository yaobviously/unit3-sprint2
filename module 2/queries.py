# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:15:50 2021

@author: yaobv
"""

CREATE_char_table = """
    CREATE TABLE IF NOT EXISTS character_table (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        level INT NOT NULL,
        exp INT NOT NULL,
        hp INT NOT NULL,
        strength INT NOT NULL,
        intelligence INT NOT NULL,
        dexterity INT NOT NULL,
        wisdom INT NOT NULL
        );
"""

INSERT_INTO_char_table = """
    INSERT INTO character_table  (
        character_id,
        name,
        level,
        exp,
        hp,
        strength,
        intelligence,
        dexterity,
        wisdom
        )
    VALUES  (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s        
   )
    ON CONFLICT (character_id) DO NOTHING;
"""

EXTRACT_chars = """
    SELECT *
    FROM charactercreator_character;
"""

EXTRACT_armory_table = """
    SELECT *
    FROM armory_item;
"""

CREATE_armory_table = """
    CREATE TABLE IF NOT EXISTS armory_table (
        item_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        val INT NOT NULL,
        weight INT NOT NULL
        );
"""