# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:23:09 2021

@author: yaobv
"""
import pandas as pd
import sqlite3 as sql

url = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'

df = pd.read_csv(url)
df.columns = df.columns.str.lower()
df = df.rename(columns={'user id': 'user_id'})

conn = sql.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df.to_sql('review', conn, index=False, if_exists='replace')

ROW_COUNT = """
    SELECT COUNT(*)
    FROM review
    """

USERS_OVER_100 = """
    SELECT COUNT(user_id)
    FROM review
    WHERE nature >= 100 
    AND shopping >= 100;
    """

AVERAGE_REVIEWS = """
    SELECT  ROUND(AVG(sports), 1) as sports_avg,
		ROUND(AVG(religious), 1) as religion_avg,
		ROUND(AVG(nature), 1) as nature_avg,
		ROUND(AVG(theatre), 1) as theatre_avg,
		ROUND(AVG(shopping), 1) as shopping_avg,
		ROUND(AVG(picnic), 1) as picnic_avg
    FROM review;
    """
