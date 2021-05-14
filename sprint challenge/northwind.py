import sqlite3 as sql

file = r'C:\Users\yaobv\Lambda Unit 3 Sprint 2\Databases\sprint challenge\northwind_small.sqlite3'

conn = sql.connect(file)
curs = conn.cursor()

def execute_query(conn, query):
    """
    Function written to read only
    """

    curs = conn.cursor()    
    results = curs.execute(query).fetchall()
    return results 

MOST_EXPENSIVE = """
    SELECT productname
    FROM product
    ORDER BY unitprice DESC
    LIMIT 10;
"""

AVERAGE_HIRE_AGE = """
    SELECT AVG(hiredate - birthdate) as avg_hire_age
    FROM employee;
"""

AVERAGE_HIRE_AGE_BY_CITY = """
    SELECT city, AVG(hiredate - birthdate)
    FROM employee
    GROUP BY city;
"""

SUPPLIERS_MOST_EXPENSIVE = """
    SELECT p.productname, p.unitprice, s.companyname
    FROM product p
    LEFT JOIN supplier s
    ON p.supplierid = s.id
    ORDER BY p.unitprice DESC
    LIMIT 10;
"""

LARGEST_CATEGORY = """
   SELECT catname, COUNT(catname) as total_cat_entries
   FROM (SELECT c.categoryname AS catname
   FROM product p
   LEFT JOIN category c
   ON p.categoryid = c.id) s
   ORDER BY total_cat_entries DESC
   LIMIT 1;
"""

MAXEMP_TERRITORIES = """
    SELECT e.lastname, e.firstname
    FROM employee e
    INNER JOIN 
    (SELECT employeeid, COUNT(territoryid) as tot_territories
    FROM employeeterritory
    GROUP BY employeeid
    ORDER BY tot_territories DESC
    LIMIT 1) s
    ON e.id = s.employeeid;
"""

expensive_items = execute_query(conn, MOST_EXPENSIVE)
avg_hire_age = execute_query(conn, AVERAGE_HIRE_AGE)
avg_age_by_city = execute_query(conn, AVERAGE_HIRE_AGE_BY_CITY)
ten_most_expensive = execute_query(conn, SUPPLIERS_MOST_EXPENSIVE)
largest_category = execute_query(conn, LARGEST_CATEGORY)
most_territories = execute_query(conn, MAXEMP_TERRITORIES)


print(expensive_items)
print(avg_hire_age)
print(avg_age_by_city)
print(ten_most_expensive)
print(largest_category)
print(most_territories)
