# Oracle

import cx_Oracle

try:
    con = cx_Oracle.connect("system/root@localhost")
    cursor = con.cursor()
    cursor.execute(
        "create table employees(eno number, ename varchar2(10),esal number(10,2),eaddr varchar2(10))"
    )
    print("Table created successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

import cx_Oracle

try:
    con = cx_Oracle.connect("system/root@localhost")
    cursor = con.cursor()
    cursor.execute("insert into employees values(100,'Durga',1000,'Hyd')")
    con.commit()
    print("Record Inserted Successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

import cx_Oracle

try:
    con = cx_Oracle.connect("system/root@localhost")
    cursor = con.cursor()
    cursor.execute("insert into employees values(2,'Prasad',20000,'Banglore')")
    con.commit()
    print("Record Inserted Successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

import cx_Oracle

try:
    con = cx_Oracle.connect("system/root@localhost")
    cursor = con.cursor()
    sql = "insert into employees values(:eno, :ename, :esal, :eaddr)"
    records = [
        (3, "Hari", 30000, "Mumbai"),
        (4, "Hema", 40000, "BZA"),
        (5, "Mohan", 50000, "Banglore"),
    ]
    cursor.executemany(sql, records)
    con.commit()
    print("Record Inserted Successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

import cx_Oracle

try:
    con = cx_Oracle.connect("system/root@localhost")
    cursor = con.cursor()
    while True:
        eno = int(input("Enter Employee Number:"))
        ename = input("Enter Employee Name:")
        esal = float(input("Enter Employee Salary:"))
        eaddr = input("Enter Employee Address:")
        sql = "insert into employees values(%d, '%s', %f, '%s')"
        cursor.execute(sql % (eno, ename, esal, eaddr))
        print("Record Inserted Successfully")
        option = input("Do you want to insert one more record[Yes| No] :")
        if option == "No":
            con.commit()
            break
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


import cx_Oracle

try:
    con = cx_Oracle.connect("system/root@localhost")
    cursor = con.cursor()
    increment = float(input("How much amount need to Increment:"))
    salrange = float(input("Enter Salary Range:"))
    sql = "update employees set esal=esal+%f where esal<%f"
    cursor.execute(sql % (increment, salrange))
    print("Records Updated Successfully")
    con.commit()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

import cx_Oracle
try:
   con=cx_Oracle.connect('system/root@localhost')
   cursor=con.cursor()
   cursor.execute("select * from employees")
   row=cursor.fetchone()
   while row is not None:
       print(row)
       row=cursor.fetchone()
except cx_Oracle.DatabaseError as e:
   if con:
       con.rollback()
       print(e)
finally:
   if cursor:
       cursor.close()
   if con:
       con.close()

import cx_Oracle
try:
   con=cx_Oracle.connect('system/root@localhost')
   cursor=con.cursor()
   cursor.execute("select * from employees")
   n=int(input("Enter the number of required rows:"))
   data=cursor.fetchmany(n)
   for row in data:
       print(row)
except cx_Oracle.DatabaseError as e:
   if con:
       con.rollback()
       print(e)
finally:
   if cursor:
       cursor.close()
   if con:
       con.close()

import cx_Oracle
try:
   con=cx_Oracle.connect('system/root@localhost')
   cursor=con.cursor()
   cursor.execute("select * from employees")
   data=cursor.fetchall()
   print(data)
except cx_Oracle.DatabaseError as e:
   if con:
       con.rollback()
       print(e)
finally:
   if cursor:
       cursor.close()
   if con:
       con.close()

import cx_Oracle
try:
   con=cx_Oracle.connect('system/root@localhost')
   cursor=con.cursor()
   cursor.execute("select * from employees")
   data=cursor.fetchall()
   print(data[0][0])
   print(data[0][1])  
except cx_Oracle.DatabaseError as e:
   if con:
       con.rollback()
       print(e)
finally:
   if cursor:
       cursor.close()
   if con:
       con.close()

