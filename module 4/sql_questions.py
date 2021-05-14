# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:01:25 2021

@author: yaobv
"""

# Answering Titanic Questions with SQL. Geez, I realized I didn't make it 
# clear that I did all of these queries on my remote database on 
# ElephantSQL. The only problem I solved in this script was the Bonus Question
# using my local titanic.csv file, so it won't print at the end. 
# My answer to the last question is 48.

import pandas as pd

titanic_csv = r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Databases\data\titanic.csv'
df = pd.read_csv(titanic_csv)
df.columns = df.columns.str.lower()

Question_1_Query = """
    SELECT survived, COUNT(survived)
    FROM titanic
    GROUP BY survived;
"""

did_not_survive = 545
survived = 342

Question_2_Query = """
    SELECT pclass, COUNT(pclass) as total
    FROM titanic
    GROUP BY pclass;
"""
pclass_1 = 216
pclass_2 = 487
pclass_3 = 184

Question_3_Query = """
    SELECT pclass, survived, COUNT(survived)
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
"""

pclass1 = {'dead' : 80, 'alive' : 136}
pclass2 = {'dead': 97, 'alive' : 87}
pclass3 = {'dead' : 368, 'alive' : 119}
    
Question_4_Query = """
    SELECT survived, AVG(age)
    FROM titanic
    GROUP BY survived
    ORDER BY survived;
"""

average_age_died = 30.2
average_age_survived = 28.4

Question_5_query = """
    SELECT pclass, AVG(age)
    FROM titanic
    GROUP BY pclass;
"""

average_age_pclass1 = 38.8
average_age_pclass2 = 25.2
average_age_pclass3 = 30.0

Question_6_query_a = """
    SELECT pclass, AVG(fare)
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass;
"""

average_fare_pclass1 = 84.2
average_fare_pclass2 = 20.7
average_fare_pclass3 = 13.7

Question_6_query_b = """
    SELECT survived, AVG(fare)
    FROM titanic
    GROUP BY survived;
"""

average_fare_survived = 48.4
average_fare_died = 22.2

Question_7_query_a = """
    SELECT pclass, AVG(sibling_or_spouse)
    FROM titanic
    GROUP BY pclass;
"""

average_sibspouse_pclass1 = 0.42
average_sibspouse_pclass2 = 0.4
average_sibspouse_pclass3 = 0.62

Question_7_query_b = """
    SELECT survived, AVG(sibling_or_spouse)
    FROM titanic
    GROUP BY survived;
"""

average_sibspouse_died = 0.56
average_sibspouse_survived = 0.47

Question_8_query_a = """
    SELECT pclass, AVG(parents_or_children)
    FROM titanic
    GROUP BY pclass;
"""

average_parchild_pclass1 = 0.36
average_parchild_pclass2 = 0.38
average_parchild_pclass3 = 0.4

Question_8_query_b = """
    SELECT survived, AVG(parents_or_children)
    FROM titanic
    GROUP BY survived;
"""

average_parchild_died = 0.33
average_parchild_survived = 0.46


Question_9_query = """
    SELECT name, COUNT(name) 
    FROM Titanic 
    GROUP BY name
    HAVING COUNT(name) > 1;
"""

duplicate_names = 'No'


### QUESTION 10: Figuring out how many couples there are on the Titanic

df['last_name'] = [name[-1] for name in df['name'].str.split()]
df['title_name'] = [name[0] for name in df['name'].str.split()]

df_filtered = df[df['siblings/spouses aboard'] > 0].copy().reset_index()

grouped = df_filtered.groupby('last_name')['title_name'].unique().reset_index()

grouped['title_name'] = [list(titles) for titles in grouped['title_name']]

# Creating a for-loop to identify couples by checking to see whether each
# surname's list of titles includes both Mr. and Mrs. Appending the resulting
# Booleans to a list and adding the list as a column. I could skip that part,
# but I like my DataFrames complete. Habit.

couples = []

for title in grouped['title_name']:
    p = all(x in title for x in ['Mr.', 'Mrs.'])
    couples.append(p)
    
grouped['couple'] = couples

total_couples = grouped['couple'].sum()

print(f'There were {total_couples} couples on the Titanic')
