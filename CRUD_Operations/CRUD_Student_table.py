import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="website"
    )

def read_singlestudent(id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM student where id= {id}")
        return cur.fetchall()

def read_allstudent():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM student")
        return cur.fetchall()

def insertstudent(a,b,c,d,e,f,g,h,i):
    with get_connection() as con:
        cur = con.cursor()
        sql = (f"Insert into Student (name,m1,m2,m3,dept,location,gender,phonenumber,"
               f"dob) values('{a}',{b},{c},{d},'{e}','{f}','{g}','{h}','{i}')")
        # print(sql)
        inserted_data = (f"Insertes as Student_Name:{a},m1:{b},m2:{c},m3:{d},Dept:{e},Location:{f},Gender:{g},"
                         f"Phone_Number:{h},DOB:{i}")
        print(inserted_data)
        cur.execute(sql)
        con.commit()
        cur.close()
        return ("Insert Successfully")



# o = insertstudent('Gowtham',56,78,76,'COMMERCE','Chengalpattu','Male','7708167760','2003-05-24')
# print(o)


# i = read_allstudent()
# print(i)

# i = read_singlestudent(7)
# print(i)

# DELETE
def delete_singlestudent(id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"Delete from student where id = {id}")
        con.commit()
        cur.close()
        return "Deleted Successfully"
# delete = delete_singlestudent(1)
# print(delete)

def delete_allstudent():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(f"truncate table student")
        con.commit()
        cur.close()
        return "Deleted Successfully"
# o = delete_allstudent()
# print(o)


def studentupdate(*args):
    with get_connection() as con:
        cur = con.cursor()
        sql=f"Update Student Set Name ='{args[1]}',m1={args[2]},m2={args[3]},m3={args[4]},dept='{args[5]}',location='{args[6]}',gender='{args[7]}',phonenumber='{args[8]}',dob='{args[9]}' where id={args[0]}"
        print(sql)
        cur.execute(sql)
        con.commit()
        cur.close()
    return "student successfully updated"

# update = studentupdate(7,'KUMAR',99,23,12,'B.com','Chennai','Male','7708167760','1971-05-02')
# print(update)