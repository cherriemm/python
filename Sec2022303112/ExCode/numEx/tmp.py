import sqlite3
import os
# -*- coding:UTF-8 -*-
def create_db(path):
    if os.path.exists(path):
        os.remove(path)
    db_hw_db_path = path
    con = sqlite3.connect(db_hw_db_path)
    table_position = """
    CREATE TABLE Position(
        POSITIONID TEXT CHECK(POSITIONID IN ('A', 'B','C', 'D')) PRIMARY KEY, 
        SALARY INT CHECK(SALARY IN (10000, 6000, 3000, 1000)));"""
    table_person = """
    CREATE TABLE Person(
        NAME TEXT(32),
        GENDER TEXT(2),
        BIRTH DATE,
        ID TEXT(18) PRIMARY KEY,
        POSITIONID TEXT,
        FOREIGN KEY (POSITIONID) REFERENCES Position(POSITIONID) );"""

    if con is not None :
        cur = con.cursor()
        cur.execute(table_position)
        cur.execute(table_person)
        return 0
    else:
        return -1



create_db("./t.db")