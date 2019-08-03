import sqlite3
from employee import Employee

# sample department entries to submit into department db
department_names = [('Administrative',),
                    ('Product Development',),
                    ('Sales',)]


# sample employee entries to submit into employee db
current_staff = [('Jane', 'Doe', 1, None, 175000),
                 ('John', 'Smith', 1, 1, 85000),
                 ('Samantha', 'Stevens', 1, 1, 85000),
                 ('Paul', 'Reitgard', 2, None, 110000),
                 ('Noah', 'Shapiro', 2, 4, 70000),
                 ('Lena', 'Hernandez', 2, 4, 65000),
                 ('Julia', 'Syndergaard', 2, 4, 50000),
                 ('Ashley', 'Wu', 3, None, 125000),
                 ('Richard', 'Wilder', 3, 8, 95000),
                 ('Sarah', 'Stone', 3, 8, 95000)]


# create connections to db
def create_conn_and_cur(db_file):
    """ create a db connection and cursor to SQLite database
    -param db_file: database db_file
    -return: connection object or None, cursor object or None
    """

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        return conn, c
    except Error as e:
        print(e)

    return None, None


# table creation
def create_table(cur, create_table_sql):
    """ create a table in current connection using a cursor and sql prompt as
        input
    -param cur: cursor object of current connection
           create_table_sql: string object of sql code to create a table
    -return:
    """
    try:
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


# data entry
def insert_departments_table(cur, entries_sql):
    """ inserts entries into the departments tableself.
    -param cur: cursor object of current connection
           entries_sql: either a single tuple or list of tuples to insert
    -return:
    """

    if isinstance(entries_sql, tuple):
        cur.execute("INSERT INTO departments (department_name) VALUES (?)",
                         entries_sql)
    elif isinstance(entries_sql, list):
        cur.executemany("INSERT INTO departments (department_name) VALUES (?)",
                             entries_sql)
    else:
        print("Entries are not of proper format")


def insert_employees_table(cur, entries_sql):
    """ inserts entries into the departments tableself.
    -param cur: cursor object of current connection
           entries_sql: either a single tuple or list of tuples to insert
    -return:
    """

    if isinstance(entries_sql, tuple):
        cur.execute("""INSERT INTO employees (first,
                                              last,
                                              department_id,
                                              manager_id,
                                              pay)
                                VALUES (?, ?, ?, ?, ?)
                        """, entries_sql)
    elif isinstance(entries_sql, list):
        cur.executemany("""INSERT INTO employees (first,
                                                  last,
                                                  department_id,
                                                  manager_id,
                                                  pay)
                                VALUES (?, ?, ?, ?, ?)
                        """, entries_sql)
    else:
        print("Entries are not of proper format")




def main():
    database = '/Users/bemiste1/Desktop/sqlite_example/employee.db'

    # sql_create_departments_table = """CREATE TABLE IF NOT EXISTS departments (
    #                                       department_id integer PRIMARY KEY,
    #                                       department_name text NOT NULL
    #                                    );"""
    #
    # sql_create_employees_table = """CREATE TABLE IF NOT EXISTS employees (
    #                                     employee_id integer PRIMARY KEY,
    #                                     first text NOT NULL,
    #                                     last text NOT NULL,
    #                                     department_id integer,
    #                                     manager_id integer,
    #                                     pay integer NOT NULL,
    #                                     FOREIGN KEY (department_id)
    #                                       REFERENCES departments (department_id)
    #                                 );"""

    # establish connection and cursor
    conn, c = create_conn_and_cur(database)

    # create tables
    if conn is not None:
        # create departments table
        create_table(c, sql_create_departments_table)
        # create employee table
        create_table(c, sql_create_employees_table)
    else:
        print("Error! Failure to create database connection")

    # insert initial entries
    insert_departments_table(c, department_names)
    insert_employees_table(c, current_staff)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
