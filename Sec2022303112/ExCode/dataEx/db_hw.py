#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目十八：实现数据库的操作
import sqlite3
import os

db_hw_db_path = ""  # 全局变量，在create_db(path)时记录创建的数据库所在路径


def create_db(path):
    try:
        if os.path.exists(path):
            os.remove(path)
        global db_hw_db_path
        db_hw_db_path = path
        con = sqlite3.connect(db_hw_db_path)
        table_position = """
        CREATE TABLE Position(
            POSITIONID CHAR PRIMARY KEY, 
            SALARY INT );"""
        table_person = """
        CREATE TABLE Person(
            NAME CHAR(32),
            GENDER CHAR(2),
            BIRTH DATE,
            ID CHAR(18) PRIMARY KEY,
            POSITIONID CHAR,
            FOREIGN KEY (POSITIONID) REFERENCES Position(POSITIONID) );"""
        cur = con.cursor()
        cur.execute(table_position)
        cur.execute(table_person)
        con.close()
    except sqlite3.Error:
        return -1
    else:
        return 0

# 使用Insert语句
def new_employee(person,level):
    try:
        con = sqlite3.connect(db_hw_db_path)
        cur = con.cursor()
        l = [10000, 6000, 3000, 1000]
        cur.execute("INSERT INTO Person "
                    "('NAME', 'GENDER', 'BIRTH', 'ID','POSITIONID') VALUES (?,?,?,?,?)",
                    (person[0],person[1],person[2],person[3],level))
        cur.execute("INSERT INTO Position"
                    "('POSITIONID', 'SALARY') VALUES(?,?)",
                    (level, l[ord(level)- ord('A')]))

        con.commit()
        con.close()
    except sqlite3.Error:
        return -1
    else:
        return 0



# 使用Delete语句
def delete_employee(person):
    try:
        con = sqlite3.connect(db_hw_db_path)
        cur = con.cursor()
        cur.execute("DELETE FROM Person WHERE ID = ?", (person,))
        con.commit()
        con.close()
    except sqlite3.Error:
        return -1
    else:
        return 0



# 使用Update语句
def set_level_salary(level,salary):
    try:
        con = sqlite3.connect(db_hw_db_path)
        cur = con.cursor()
        cur.execute("UPDATE Position "
                    "SET SALARY = ? "
                    "WHERE POSITIONID = ?"
                    , (salary, level))
        con.commit()
        con.close()
    except sqlite3.Error:
        return -1
    else:
        return 0


# 使用Select查询语句
def get_total_salary():
    try:
        con = sqlite3.connect(db_hw_db_path)
        cur = con.cursor()
        cur.execute("""SELECT SUM(SALARY) FROM Position  
                    WHERE Position.POSITIONID IN (SELECT Person.POSITIONID FROM Person);""")
        sum_value = cur.fetchone()[0]
        con.commit()
        con.close()
    except sqlite3.Error:
        return -1
    else:
        return sum_value

"""def check():
    conn = sqlite3.connect('./test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Person")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute("SELECT * FROM Position")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()"""

if __name__ == "__main__":
    create_db('./test.db')
    new_employee(("tom","m","2018-09-01","123456789"),"A")
    new_employee(("too","f","2017-09-01","123456788"),"B")
    print(get_total_salary())
    delete_employee("123456788")
    print(get_total_salary())
    set_level_salary("A",2)
    print(get_total_salary())
