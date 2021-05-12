# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:44:58 2021

@author: yaobv
"""
import sqlite3 as sql

db = r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Module_One\data\rpg_db.sqlite3'

conn = sql.connect(db)
curs = conn.cursor()

queries = [TOTAL_CHARACTERS, TOTAL_SUBCLASS, TOTAL_ITEMS, WEAPONS, NON_WEAPONS,
           CHARACTER_ITEMS, CHARACTER_WEAPONS, AVG_CHARACTER_ITEMS,
           AVG_CHARACTER_WEAPONS]

TOTAL_CHARACTERS = """
        SELECT COUNT(*)
        FROM charactercreator_character;
        """

TOTAL_SUBCLASS = """
        SELECT COUNT(*)
        FROM charactercreator_necromancer;
        """

TOTAL_ITEMS = """
        SELECT COUNT(*)
        FROM armory_item;
        """

WEAPONS = """
        SELECT COUNT(*)
        FROM armory_item ai 
        INNER JOIN armory_weapon aw
        ON ai.item_id = aw.item_ptr_id ;
        """

NON_WEAPONS = """
        SELECT COUNT(*)
        FROM armory_item ai 
        WHERE ai.item_id NOT IN (SELECT item_ptr_id as item_id
							FROM armory_weapon);
        """

CHARACTER_ITEMS = """
        SELECT character_id, COUNT(*) as num_items
        FROM charactercreator_character_inventory cci 
        GROUP BY character_id
        ORDER BY num_items DESC 
        LIMIT 20;
        """

CHARACTER_WEAPONS = """
        SELECT character_id, COUNT(*) as num_weapons
        FROM charactercreator_character_inventory cci 
        WHERE cci.item_id IN (SELECT item_ptr_id AS weapon_id
                              FROM armory_weapon)
        GROUP BY character_id
        ORDER BY num_weapons DESC 
        LIMIT 20;
        """

AVG_CHARACTER_ITEMS = """
        SELECT AVG(item_count)
        FROM (SELECT COUNT(item_id) as item_count
              FROM charactercreator_character_inventory cci
              GROUP BY character_id);
        """

AVG_CHARACTER_WEAPONS = """
        SELECT AVG(num_weapons)
        FROM (SELECT COUNT(*) as num_weapons
              FROM charactercreator_character_inventory cci 
              WHERE cci.item_id IN (SELECT item_ptr_id AS weapon_id
                                    FROM armory_weapon)
              GROUP BY character_id);
        """


def connect_to_db(database):
    return sql.connect(database)


def return_query(conn, query):
    curs = conn.cursor()

    for q in queries:
        result = curs.execute(q).fetchall()
        print(result)
    curs.close()


if __name__ == "__main__":
    conn = connect_to_db(db)
    query_results = return_query(conn, WEAPONS)
