
import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="website"
    )

def read_single_hod_details(hod_id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM hod where hod_id= {hod_id}")
        return cur.fetchall()

def read_all_hod_details():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM hod")
        return cur.fetchall()

def insert_hod_details(hod_name,phonenumber):
    with get_connection() as con:
        cur = con.cursor()
        mysql = f"Insert into hod (hod_name,phonenumber) Values('{hod_name}','{phonenumber}')"
        print(mysql)
        cur.execute(mysql)
        con.commit()
        cur.close()
        return ("INSERTED SUCCESSFULLY")

# print(insert_hod_details('Kuruloviyan','7890543145'))

# print(read_all_hod_details())

# print(read_single_hod_details(1))

# DELETE
def delete_single_hod_detail(hod_id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"Delete from hod where hod_id = {hod_id}")
        con.commit()
        cur.close()
        return f"HOD ID {hod_id} has been Deleted Successfully"

# print(delete_single_hod_detail(3))


def delete_all_hod_details():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"truncate table hod")
        con.commit()
        cur.close()
        return "All HOD Details has been Deleted Successfully"

# print(delete_all_hod_details())


def hod_update(*args):
    with get_connection() as con:
        cur = con.cursor()
        sql=f"update hod set hod_name='{args[1]}',phonenumber={args[2]} where hod_id={args[0]}"
        print(sql)
        cur.execute(sql)
        con.commit()
        cur.close()
    return "HOD Details has been successfully Updated"

# print(hod_update(4,'Venkatesh',99876532456))
