# these should be the only imports you need
import sys
import sqlite3
from sqlite3 import Error
from sqlite3 import connect

#Name: John Robert Lint
#Umich uniqname: jrlint


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_cust(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM 'customer'")

    rows = cur.fetchall()
    print("ID     ", end='')
    print("Customer Name")
    for row in rows:
        print(row[0], '   ', end='', sep='')
        print(row[1])

def select_all_emp(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM 'employee'")
    rows = cur.fetchall()
    print("ID       ", end='')
    print("Employee Name")
    for row in rows:
        print(row[0], '        ', end='', sep='')
        print(row[2], ' ', end='', sep='')
        print(row[1])

def select_cust_order(conn, cust):
    cur = conn.cursor()
    cur.execute("SELECT OrderDate FROM 'order' WHERE CustomerId=?", (cust,))
    rows = cur.fetchall()
    print("Order dates")
    for row in rows:
        for x in row:
            print(x, end='', sep=' ')
        print()


def select_emp_orders(conn, emp):
    cur = conn.cursor()
    cur.execute("SELECT id FROM 'employee' WHERE LastName =?", (emp,))
    rows = cur.fetchall()
    empid = ''
    for row in rows:
        empid = row[0]


    cur.execute("SELECT OrderDate FROM 'order' WHERE EmployeeId=?", (empid,))
    rows = cur.fetchall()
    print("Order dates")
    for row in rows:
        for x in row:
            print(x, end='', sep=' ')
        # print(row[0], '        ', sep='', end='')
        # print(row[1], end='')
        # print(row[2])
        print()


# write your code here
def main():
    val = sys.argv[1]
    db = "Northwind_small.sqlite"
    connection = create_connection(db)
    if val == 'customers':
        select_all_cust(connection)
    if val == 'employees':
        select_all_emp(connection)
    if val == 'orders':
        val2 = sys.argv[2]
        v = val2[:4]
        if v == 'cust':
            select_cust_order(connection, val2[5:])
        elif v == 'emp=':
            select_emp_orders(connection, val2[4:])
if __name__ == "__main__":
        main()

# usage should be
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

