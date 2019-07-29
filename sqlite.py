import sqlite3

# sample department entries to submit into department db
department_names = ['Administrative',
                    'Product Development',
                    'Sales']


# sample employee entries to submit into employee db
new_hires = [('Jane', 'Doe', 1, None, 175,000),
             ('John', 'Smith', 1, 1, 85,000),
             ('Samantha', 'Stevens', 1, 1, 85,000),
             ('Paul', 'Reitgard', 2, None, 110,000),
             ('Noah', 'Shapiro', 2, 4, 70,000),
             ('Lena', 'Hernandez', 2, 4, 65,000),
             ('Julia', 'Syndergaard', 2, 4, 50,000),
             ('Ashley', 'Wu', 3, None, 125,000),
             ('Richard', 'Wilder', 3, 8, 95,000),
             ('Sarah', 'Stone', 3, 8, 95,000)]


# create connections to dbs
conn_d = sqlite3.connect('department.db')
cur_d = conn_d.cursor()

conn_e = sqlite3.connect('employee.db')
cur_e = conn_e.cursor()


# departments table creation and value entry
cur_d.execute("""CREATE TABLE IF NOT EXISTS departments (
                 department_id integer PRIMARY KEY,
                 department_name text NOT NULL,
                 FOREIGN KEY (department_id)
                    REFERENCES employees (department_id))""")

cur_d.executemany("INSERT INTO departments (department_name) VALUES (?)", department_names)


# creating a table to store employee data
# cur_e.execute("""CREATE TABLE employees (
#              employee_id integer PRIMARY KEY,
#              first text NOT NULL,
#              last text NOT NULL,
#              department_id integer NOT NULL,
#              manager_id integer,
#              pay integer NOT NULL,
#              FOREIGN KEY (department_id)
#                 REFERENCES departments(department_id))""")
#
# # inserting employees into employees table
# cur_e.executemany("INSERT INTO employee(first, last,
#                                     department_id,
#                                     manager_id,
#                                     pay)
#                    VALUES (?, ?, ?, ?, ?)", new_hires)

conn_d.commit()
conn_d.close()
conn_e.commit()
conn_e.close()
