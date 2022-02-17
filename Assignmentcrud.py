import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('crud.db')
        return conn
    except Error:
        print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE employee(emp_id n(5), name char(30), dept char(35), salary decimal(7,2));")
    #  # Insert records
    cursorObj.executescript("""
    INSERT INTO employee VALUES(5001,'James Hoog', 'design', 2000.15);
    INSERT INTO employee VALUES(5002,'Nail Knite', 'testing', 20000.25);
    INSERT INTO employee VALUES(5003,'Pit Alex', 'frontend', 30000.15);
    INSERT INTO employee VALUES(5004,'Mc Lyon', 'backend', 45000.35);
    INSERT INTO employee VALUES(5005,'Paul Adam', 'manager', 32100.45);
    """)
    conn.commit()
    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
    print("\ninsert the employee details:")
    cursorObj = conn.cursor()
    cursorObj.execute('''INSERT INTO employee (emp_id,name,dept,salary)VALUES(5006,'sam','hr',23100.50)''')
    cursorObj.execute("SELECT * FROM employee")
    conn.commit()
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
    print("update the employee details\n")
    cursorObj = conn.cursor()
    cursorObj.execute('''UPDATE employee SET name='deepak',dept='hr',salary=28000.02 WHERE emp_id=5002''')
    conn.commit()
    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
    print("\nDelete the employee details:")
    cursorObj = conn.cursor()
    cursorObj.execute('''DELETE FROM employee WHERE emp_id in (5005)''')
    conn.commit()
    cursorObj.execute("SELECT * FROM employee")
    # conn.commit()
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
sqllite_conn = sql_connection() #asscessment.db
sql_table(sqllite_conn) #assessment.db
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")