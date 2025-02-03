import database_connect 
mycursor = database_connect.mydb.cursor()

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print('หัวข้อทั้งหมด')
    for i in table:
        print(i)

def select():
    show_table()
    table = input("ใส่หัวข้อที่ต้องการจะค้นหา : ")
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

def select_all(table):
    # show_table()
    # table = input("ใส่หัวข้อที่ต้องการจะค้นหา : ")
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    return table

def colum(table):
    mycursor.execute(f"SHOW COLUMNS FROM {table};")
    table = mycursor.fetchall()
    print('ชื่อคอลัมน์ทั้งหมด')
    for i in table:
        print(i)

def select_nametable():
    name = input('ป้อนชื่อนักเรียน : ')
    mycursor.execute(f"SELECT * FROM student where name like '%{name}%' ")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)


def ins_subject():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง subject')
    a = input('ใส่ id : ')
    b = input('ใส่ name : ')
    sql = " INSERT INTO subject VALUES ( %s , %s ) "
    val = (a,b)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')


def ins_student():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง student')
    a = input('ใส่ studentID : ')
    b = input('ใส่ name : ')
    c = float(input('ใส่ grade : '))
    sql = " INSERT INTO student VALUES ( %s , %s , %s ) "
    val = (a,b,c)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

def insert():
    show_table()
    ch = input('เลือกตารางที่จะเพิ่มข้อมูล : ')
    if ch == 'student':
        ins_student()
        select_table(ch)
    elif ch == 'subject':
        ins_subject()
        select_table(ch)

def ins_subject():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง subject')
    a = input('ใส่ id : ')
    b = input('ใส่ name : ')
    sql = " INSERT INTO subject VALUES ( %s , %s ) "
    val = (a,b)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

def ins_student():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง student')
    a = input('ใส่ studentID : ')
    b = input('ใส่ name : ')
    c = float(input('ใส่ grade : '))
    sql = " INSERT INTO student VALUES ( %s , %s , %s ) "
    val = (a,b,c)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')


def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

def insert_all():
    show_table()
    ch = input('เลือกตารางที่จะแก้ไข : ')
    if ch == 'student':
        ins_student()
        select_table(ch)
    elif ch == 'subject':
        ins_subject()
        select_table(ch)

def delete():
    print('ฟังค์ชั่นการลบข้อมูลในตาราง')
    show_table()
    a = input('ใส่ชื่อตารางที่จะลบ: ')
    colum(a)
    b = input('ใส่ชื่อคอลัมที่จะลบ : ')
    select_all(a)
    c = input('ใส่ข้อมูลที่จะลบ : ')
    sql = f" DELETE FROM {a} WHERE {b} = {c} "
    mycursor.execute(sql)
    database_connect.mydb.commit()
    print('ลบข้อมูลสำเร็จ')
    select_all(a)
