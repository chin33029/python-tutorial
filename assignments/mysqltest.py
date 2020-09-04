"""Test DB"""

import mysql.connector

conn = mysql.connector.connect(user='root', password='sunset96', host='127.0.0.1', database='sample_db')

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = '''CREATE TABLE EMPLOYEE2(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
)'''
cursor.execute(sql)

conn.close()

