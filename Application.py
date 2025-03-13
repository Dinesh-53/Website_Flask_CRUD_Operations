from My_Website.CRUD_Operations.CRUD_Student_table import *
from My_Website.CRUD_Operations.CRUD_Department_table import *
from My_Website.CRUD_Operations.CRUD_HOD_table import *
from flask import *

app = Flask(__name__)  # app - application

@app.route('/')  # Entry point
def open_home_page():
    name = "Dinesh"
    return render_template('home.html',name = name)

# --------------------------------- INSERT DATAS ----------------------------------

# STUDENTS_DETAILS

@app.route('/addstudent')
def open_stud_page():
    return render_template('student.html')

@app.route('/savestudenttodb',methods=['POST','GET'])
def insert_student():
    if request.method=='POST':
        try:
            sn = request.form["sname"]
            sm1 = request.form["sm1"]
            sm2 = request.form["sm2"]
            sm3 = request.form["sm3"]
            sd = request.form["dname"]
            sl = request.form["locations"]
            sg = request.form["gender"]
            sp = request.form["sphone"]
            sdo = request.form["sdob"]
            print(f"Student Detail {sn, sm1, sm2, sm3, sd, sl, sg, sp, sdo} has been Successfully Added")
            msg = insertstudent(sn, sm1, sm2, sm3, sd, sl, sg, sp, sdo)
            #return render_template("sucesspage.html", msg=msg)
        except:
            msg = "Not Successful"
            #return render_template("sucesspage.html",msg = msg)
        else:
            print("I will run whenever try runs")
        finally:
            return render_template("sucesspage.html",msg = msg)

# DEPARTMENTS_DETAILS

@app.route('/add_department')
def open_dept_page():
    return render_template('department.html')

@app.route('/savedepttodb',methods=['POST','GET'])
def insertdepartment():
    if request.method=='POST':
        dn=request.form['departments']
        hi=request.form['hiname']
        print(f"Department Detail {dn,hi} has been Inserted Successfully")
        msg=insert_dept(dn,hi)
    return render_template("sucesspage.html",msg=msg)

# HOD_DETAILS

@app.route('/add_hod')
def open_hod_page():
    return render_template('hod.html')

@app.route('/savehodtodb',methods=['POST','GET'])
def inserthod():
    if request.method=='POST':
        h=request.form['hname']
        p=request.form['hphone']
        print(f"HOD Detail {h,p} has been Inserted Successfully")
        msg=insert_hod_details(h,p)
    return render_template("sucesspage.html",msg=msg)

# ------------------------READ DATAS ------------------------------------------
@app.route('/read_student_details')
def fetchallstudent():
    rows = read_allstudent()
    # for a in o:  # o = read_allstudent()
    #     print(a)
    return render_template("view_student.html",rows=rows)

@app.route('/read_dept_details')
def fetchalldepartment():
    rows = read_all_dept()
    # for a in o:
    #     print(a)
    return render_template("view_department.html",rows=rows)


@app.route('/read_hod_details')
def fetchallhod():
    rows = read_all_hod_details()
    # for a in o:
    #     print(a)
    return render_template("view_hod.html",rows=rows)

# --------------------------  DELETE SINGLE DATAS -------------------------

# Student_Delate
@app.route('/<id>/sdelete')
def studentdelete(id):
    print(f"Student ID {id} has been Deleted Successfully")
    msg = delete_singlestudent(id)
    return render_template("sucesspage.html",msg = msg)

# Department_Delete
@app.route('/<department_id>/ddelete')
def departmentdelete(department_id):
    print(f"Department ID {department_id} has been Deleted Successfully")
    msg = delete_single_dept_detail(department_id)
    return render_template("sucesspage.html",msg = msg)

# HOD_Delete
@app.route('/<hod_id>/hdelete')
def hoddelete(hod_id):
    print(f"HOD ID {hod_id} has been Deleted Successfully")
    msg = delete_single_hod_detail(hod_id)
    return render_template("sucesspage.html",msg = msg)

# *********************************** DELETE ALL DATAS **************************************

@app.route('/sdeleteall')
def student_delete_all():
    print("All the Student's Details has been Deleted Successfully")
    msg = delete_allstudent()
    return render_template("sucesspage.html",msg = msg)

@app.route('/ddeleteall')
def department_delete_all():
    print("All the Department's Details has been Deleted Successfully")
    msg = delete_all_dept_details()
    return render_template("sucesspage.html",msg = msg)

@app.route('/hdeleteall')
def hod_delete_all():
    print("All the HOD's Details has been Deleted Successfully")
    msg = delete_all_hod_details()
    return render_template("sucesspage.html",msg = msg)

# *********************************** UPDATE DATAS ***************************************

# STUDENT EDIT/UPDATE
@app.route('/<id>/sedit')
def studentedit(id):
    print(f"Student ID : {id}")
    available_dept=['Civil','Mech','CSE','IT']
    available_options=['Chengalpattu','Chennai','Madurai','Dhanushkodi']
    gender_opt=['FEMALE','MALE']
    rows = read_singlestudent(id)
    print(rows)
    selected_Dept = rows[0][5] # Dept
    selected_value=rows[0][6]  # LOCATION
    gender_value=rows[0][7]  # GENDER
    # print(selected_value)
    # print(gender_value)
    msg = "hi"
    return render_template("update_student.html",rows = rows,available_dept=available_dept,
                           selected_Dept=selected_Dept,available_options=available_options,
                           selected_value=selected_value,gender_opt=gender_opt,gender_value=gender_value)

@app.route('/updatestudenttodb',methods=['POST','GET'])
def studentup():
    if request.method=='POST':
        i=request.form["sid"]
        sn=request.form["sname"]
        sm1=request.form["sm1"]
        sm2=request.form["sm2"]
        sm3=request.form["sm3"]
        sd=request.form["dname"]
        sl=request.form["locations"]
        sg=request.form["gender"]
        sp=request.form["sphone"]
        sdo=request.form["sdob"]
        print(f"Student Details {sn,sm1,sm2,sm3,sd,sl,sg,sp,sdo} has been Successfully Updated")
        msg = studentupdate(i,sn,sm1,sm2,sm3,sd,sl,sg,sp,sdo)
        return render_template("sucesspage.html",msg=msg)

# DEPARTMENT EDIT/UPDATE

@app.route('/<id>/dedit')
def departmentedit(id):
    print(f"Department ID : {id}")
    available_options=['Civil','Mech','CSE','IT']
    rows = read_single_dept(id)
    print(rows)
    selected_value=rows[0][1]
    msg = "hi"
    return render_template("update_department.html",rows = rows,available_options=available_options,
                           selected_value=selected_value)

@app.route('/updatedepartmenttodb',methods=['POST','GET'])
def departmentup():
    if request.method=='POST':
        i=request.form["did"]
        dn=request.form["departments"]
        hi=request.form["hiname"]
        print(f"Department Details {i,dn,hi} has been Successfully Upadated")
        msg = dept_update(i,dn,hi)
        return render_template("sucesspage.html",msg=msg)

# HOD EDIT/UPDATE
@app.route('/<id>/hedit')
def hodedit(id):
    print(f"HOD ID : {id}")
    rows = read_single_hod_details(id)
    print(rows)
    msg = "hi"
    return render_template("update_hod.html",rows = rows)

@app.route('/updatehodtodb',methods=['POST','GET'])
def hodup():
    if request.method=='POST':
        i=request.form["hid"]
        hn=request.form["hname"]
        hp=request.form["hphone"]
        print(f"HOD Detail {i,hn,hp} has been Successfully Updated")
        msg = hod_update(i,hn,hp)
        return render_template("sucesspage.html",msg=msg)


if __name__ == '__main__':
    app.run(port=8790)  # default port = 5000

