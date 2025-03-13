
import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="website"
    )

# @@@@@@@@@@@@@@@@@ CREATE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def read_single_dept(department_id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM department where department_id= {department_id}")
        return cur.fetchall()

def read_all_dept():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM department")
        return cur.fetchall()

def insert_dept(dept_name,hod_id):
    with get_connection() as con:
        cur = con.cursor()
        mysql = f"Insert into Department (department_name,hod_id) Values('{dept_name}',{hod_id})"
        print(mysql)
        cur.execute(mysql)
        con.commit()
        cur.close()
        return ("INSERTED SUCCESSFULLY")

#print(insert_dept('IT',1))

# print(read_all_dept())

# print(read_single_dept(3))

# DELETE
def delete_single_dept_detail(department_id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"Delete from department where department_id = {department_id}")
        con.commit()
        cur.close()
        return f"Department ID {department_id} has been Deleted Successfully"

# print(delete_single_dept_detail(1))

def delete_all_dept_details():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"truncate table department")
        con.commit()
        cur.close()
        return "All Department Details has been Deleted Successfully"

# print(delete_all_dept_details())



def dept_update(*args):
    with get_connection() as con:
        cur = con.cursor()
        sql=f"update department set department_name='{args[1]}',hod_id={args[2]} where department_id={args[0]}"
        print(sql)
        cur.execute(sql)
        con.commit()
        cur.close()
    return "Department Details has been successfully Updated"

# print(dept_update(4,'B.COM[ISM]',2))





