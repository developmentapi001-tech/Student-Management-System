import sqlite3


#===============================
#DATABASE CREATE
#===============================

#Database se Connection
conn=sqlite3.connect("students.db")

#Cursor create
cursor= conn.cursor()

#Student table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
course TEXT,
phone TEXT
)
""")

#Chnages save
conn.commit

#Connection close
conn.close

#=======================
#ADD STUDENT
#=======================
def add_student():
    name = input("Enter student name:")
    age = int(input("Enter student age:"))
    course = input("Enter course:")
    phone = input("Enter phone number :")

    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute("""
    INSERT INTO students(name,age,course,phone)
    values(?,?,?,?)
    """,(name,age,course,phone))

    conn.commit()
    conn.close()

    print("Student added successfully")

    #=======================
    #PROGRAM START
    #=======================

print("===================================")
print("   STUDENT MANAGEMENT SYSTEM")
print("===================================")


#============================
#VIEW ALL STUDENTS
#============================

def view_students():
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()

    conn.close

    print("\n=====ALL STUDENTS=====")

    if not students:
        print("No students found")
        return

    for student in students:
        print("ID:",student[0])
        print("Name:",student[1])
        print("Age:",student[2])
        print("Course:",student[3])
        print("Phone:",student[4])
        print("---------------------")


# ==============================
# SEARCH STUDENT
# ==============================

def search_student():
    student_id = int(input("\nEnter Student ID: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    if student:
        print("\n===== STUDENT FOUND =====")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Phone:", student[4])
    else:
        print("\nStudent not found!")

#======================================
#UPDATE STUDENTS DETAILS
#======================================

def update_student():

    student_id = input("Enter student ID to update: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nCurrent Student Details:")
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Phone:", student[4])

        name = input("\nEnter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")
        phone = input("Enter new phone number: ")

        cursor.execute(
            """UPDATE students
               SET name = ?, age = ?, course = ?, phone = ?
               WHERE id = ?""",
            (name, age, course, phone, student_id)
        )

        conn.commit()
        print("\nStudent updated successfully!")

    else:
        print("\nStudent not found!")

    conn.close()

#===================================
#DELETE STUDENTS
#===================================
def delete_student():

    student_id = input("Enter student ID to delete: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Phone:", student[4])

        confirm = input("\nAre you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":

            cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

            conn.commit()
            print("\nStudent deleted successfully!")

        else:
            print("\nDelete cancelled!")

    else:
        print("\nStudent not found!")

    conn.close()
        

#=======================
#MAIN MENU
#=======================

while True:

    print("\n===================================")
    print("     STUDENTS MANAGEMENT SYSTEM      ")
    print("=====================================")
    print("1.Add Student")
    print("2.View All Students")
    print("3.Search student by ID")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
            update_student()
    elif choice=="5":
                delete_student()
    elif choice=="6":
        print("\nThanku you for using Students Management System!")
        break
    else:
        print("\nInvalid choice! Please try again")

