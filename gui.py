import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


# ================= DATABASE =================

def get_total_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    conn.close()
    return total


# ================= DASHBOARD COUNT =================

def get_total_courses():
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute("SELECT COUNT(DISTINCT Course) FROM students")
    total=cursor.fetchall()[0]

    conn.close
    return total

def show_total():
    total_label.config(text=get_total_students())
    course_count_label.config(text=get_total_courses())


# ================= PROFESSIONAL ADD STUDENT =================

def add_student_window():

    window = tk.Toplevel(root)
    window.title("Add Student")
    window.geometry("550x600")
    window.configure(bg=BG_COLOR)
    window.resizable(False, False)

    # Heading
    tk.Label(
        window,
        text="ADD NEW STUDENT",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 24, "bold")
    ).pack(pady=(30, 5))

    tk.Label(
        window,
        text="Enter student information below",
        bg=BG_COLOR,
        fg=MUTED_COLOR,
        font=("Arial", 11)
    ).pack(pady=(0, 25))

    # Form Card
    form = tk.Frame(
        window,
        bg=CARD_COLOR,
        padx=35,
        pady=25
    )

    form.pack(
        padx=35,
        fill="both"
    )

    # Student Name
    tk.Label(
        form,
        text="Student Name",
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    name_entry = tk.Entry(
        form,
        width=42,
        font=("Arial", 11)
    )

    name_entry.pack(
        pady=(5, 15),
        ipady=5
    )

    # Age
    tk.Label(
        form,
        text="Age",
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    age_entry = tk.Entry(
        form,
        width=42,
        font=("Arial", 11)
    )

    age_entry.pack(
        pady=(5, 15),
        ipady=5
    )

    # Course
    tk.Label(
        form,
        text="Course",
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    course_entry = tk.Entry(
        form,
        width=42,
        font=("Arial", 11)
    )

    course_entry.pack(
        pady=(5, 15),
        ipady=5
    )

    # Phone
    tk.Label(
        form,
        text="Phone Number",
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    phone_entry = tk.Entry(
        form,
        width=42,
        font=("Arial", 11)
    )

    phone_entry.pack(
        pady=(5, 20),
        ipady=5
    )

    # Save Student
    def save_student():

        name = name_entry.get().strip()
        age = age_entry.get().strip()
        course = course_entry.get().strip()
        phone = phone_entry.get().strip()

        # Empty field validation
        if not name or not age or not course or not phone:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields!"
            )
            return

        # Age validation
        try:
            age = int(age)

        except ValueError:

            messagebox.showerror(
                "Invalid Age",
                "Age must be a number!"
            )
            return

        # Save to database
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO students
            (name, age, course, phone)
            VALUES (?, ?, ?, ?)
            """,
            (name, age, course, phone)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )

        window.destroy()

        

        # Update dashboard count
        show_total()

    tk.Button(
        form,
        text="💾  SAVE STUDENT",
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        relief="flat",
        font=("Arial", 11, "bold"),
        width=25,
        height=2,
        command=save_student
    ).pack(pady=(5, 5))


    # Cancel Button
    tk.Button(
        window,
        text="Cancel",
        bg="#E5E7EB",
        fg=TEXT_COLOR,
        relief="flat",
        font=("Arial", 10, "bold"),
        width=15,
        command=window.destroy
    ).pack(pady=15)

# ================= PROFESSIONAL VIEW STUDENTS =================

def view_students_window():

    window = tk.Toplevel(root)
    window.title("All Students")
    window.geometry("950x600")
    window.configure(bg=BG_COLOR)

    # Heading
    tk.Label(
        window,
        text="ALL STUDENTS",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 24, "bold")
    ).pack(anchor="w", padx=30, pady=(25, 5))

    tk.Label(
        window,
        text="View and search all registered students",
        bg=BG_COLOR,
        fg=MUTED_COLOR,
        font=("Arial", 11)
    ).pack(anchor="w", padx=30)

    # ================= SEARCH =================

    search_frame = tk.Frame(
        window,
        bg=BG_COLOR
    )

    search_frame.pack(
        fill="x",
        padx=30,
        pady=25
    )

    tk.Label(
        search_frame,
        text="Search:",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 11, "bold")
    ).pack(side="left")

    search_entry = tk.Entry(
        search_frame,
        width=35,
        font=("Arial", 11)
    )

    search_entry.pack(
        side="left",
        padx=10
    )

    # ================= TABLE =================

    table_frame = tk.Frame(
        window,
        bg=CARD_COLOR
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 25)
    )

    columns = (
        "ID",
        "Name",
        "Age",
        "Course",
        "Phone"
    )

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    # Headings
    for column in columns:
        table.heading(
            column,
            text=column
        )

    # Column sizes
    table.column(
        "ID",
        width=60,
        anchor="center"
    )

    table.column(
        "Name",
        width=200
    )

    table.column(
        "Age",
        width=80,
        anchor="center"
    )

    table.column(
        "Course",
        width=200
    )

    table.column(
        "Phone",
        width=180
    )

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=table.yview
    )

    table.configure(
        yscrollcommand=scrollbar.set
    )

    table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ================= LOAD DATA =================

    def load_students(search=""):

        # Remove old data
        for item in table.get_children():
            table.delete(item)

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        if search == "":

            cursor.execute(
                "SELECT * FROM students"
            )

        else:

            cursor.execute(
                """
                SELECT * FROM students
                WHERE id LIKE ?
                OR name LIKE ?
                OR course LIKE ?
                OR phone LIKE ?
                """,
                (
                    "%" + search + "%",
                    "%" + search + "%",
                    "%" + search + "%",
                    "%" + search + "%"
                )
            )

        students = cursor.fetchall()

        conn.close()

        # Insert data
        for student in students:

            table.insert(
                "",
                "end",
                values=student
            )

    # ================= SEARCH BUTTON =================

    tk.Button(
        search_frame,
        text="🔍 Search",
        bg="#2563EB",
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        width=12,
        command=lambda: load_students(
            search_entry.get()
        )
    ).pack(side="left")

    # ================= SHOW ALL BUTTON =================

    tk.Button(
        search_frame,
        text="Show All",
        bg="#E5E7EB",
        fg=TEXT_COLOR,
        relief="flat",
        font=("Arial", 10, "bold"),
        width=12,
        command=lambda: [
            search_entry.delete(0, tk.END),
            load_students()
        ]
    ).pack(side="left", padx=8)

    # Load students when window opens
    load_students()

# ================= SEARCH STUDENT =================

def search_student_window():

    window = tk.Toplevel(root)
    window.title("Search Student")
    window.geometry("500x400")
    window.resizable(False, False)

    tk.Label(
        window,
        text="SEARCH STUDENT",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(
        window,
        text="Enter Student ID",
        font=("Arial", 12)
    ).pack()

    id_entry = tk.Entry(
        window,
        width=30
    )
    id_entry.pack(pady=10)

    result_label = tk.Label(
        window,
        text="",
        font=("Arial", 12),
        justify="left"
    )
    result_label.pack(pady=20)

    def search():

        student_id = id_entry.get()

        if student_id == "":
            messagebox.showwarning(
                "Warning",
                "Please enter Student ID!"
            )
            return

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        conn.close()

        if student:

            result_label.config(
                text=
                f"ID: {student[0]}\n"
                f"Name: {student[1]}\n"
                f"Age: {student[2]}\n"
                f"Course: {student[3]}\n"
                f"Phone: {student[4]}"
            )

        else:

            result_label.config(
                text="Student not found!"
            )

    tk.Button(
        window,
        text="SEARCH",
        width=20,
        command=search
    ).pack(pady=10)

# ================= UPDATE STUDENT =================

def update_student_window():

    window = tk.Toplevel(root)
    window.title("Update Student")
    window.geometry("500x550")
    window.resizable(False, False)

    tk.Label(
        window,
        text="UPDATE STUDENT",
        font=("Arial", 22, "bold")
    ).pack(pady=20)

    tk.Label(window, text="Student ID").pack()

    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=5)

    tk.Label(window, text="New Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack(pady=5)

    tk.Label(window, text="New Age").pack()
    age_entry = tk.Entry(window, width=35)
    age_entry.pack(pady=5)

    tk.Label(window, text="New Course").pack()
    course_entry = tk.Entry(window, width=35)
    course_entry.pack(pady=5)

    tk.Label(window, text="New Phone").pack()
    phone_entry = tk.Entry(window, width=35)
    phone_entry.pack(pady=5)

    def update():

        student_id = id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        course = course_entry.get()
        phone = phone_entry.get()

        if (
            student_id == ""
            or name == ""
            or age == ""
            or course == ""
            or phone == ""
        ):
            messagebox.showwarning(
                "Warning",
                "Please fill all fields!"
            )
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Age must be a number!"
            )
            return

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            conn.close()

            messagebox.showerror(
                "Error",
                "Student not found!"
            )
            return

        cursor.execute(
            """
            UPDATE students
            SET name = ?, age = ?, course = ?, phone = ?
            WHERE id = ?
            """,
            (name, age, course, phone, student_id)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Student updated successfully!"
        )

        window.destroy()

    tk.Button(
        window,
        text="UPDATE STUDENT",
        width=20,
        command=update
    ).pack(pady=25)

# ================= DELETE STUDENT =================

def delete_student_window():

    window = tk.Toplevel(root)
    window.title("Delete Student")
    window.geometry("500x400")
    window.resizable(False, False)

    tk.Label(
        window,
        text="DELETE STUDENT",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(
        window,
        text="Enter Student ID",
        font=("Arial", 12)
    ).pack()

    id_entry = tk.Entry(
        window,
        width=35
    )
    id_entry.pack(pady=10)

    def delete():

        student_id = id_entry.get()

        if student_id == "":
            messagebox.showwarning(
                "Warning",
                "Please enter Student ID!"
            )
            return

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            conn.close()

            messagebox.showerror(
                "Error",
                "Student not found!"
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete\n"
            f"Student: {student[1]}?"
        )

        if confirm:

            cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Student deleted successfully!"
            )

            window.destroy()
            show_total()

        conn.close()

    tk.Button(
        window,
        text="DELETE STUDENT",
        width=20,
        command=delete
    ).pack(pady=25)

# ================= MODERN MAIN WINDOW =================

root = tk.Tk()

root.title("Student Management System | Dashboard")
root.iconname("Student Management System")
root.geometry("1100x650")
root.resizable(False, False)

# ================= COLORS =================

SIDEBAR_COLOR = "#172033"
BG_COLOR = "#F4F7FB"
CARD_COLOR = "#FFFFFF"
TEXT_COLOR = "#172033"
MUTED_COLOR = "#6B7280"


# ================= MAIN BACKGROUND =================

root.configure(bg=BG_COLOR)


# ================= SIDEBAR =================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR_COLOR,
    width=240,
    height=650
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# Logo / Title

tk.Label(
    sidebar,
    text="STUDENT",
    bg=SIDEBAR_COLOR,
    fg="white",
    font=("Arial", 22, "bold")
).pack(pady=(40, 0))

tk.Label(
    sidebar,
    text="MANAGEMENT",
    bg=SIDEBAR_COLOR,
    fg="#60A5FA",
    font=("Arial", 14, "bold")
).pack(pady=(0, 40))


# ================= SIDEBAR BUTTONS =================

tk.Button(
    sidebar,
    text="🏠   Dashboard",
    width=22,
    height=2,
    bg="#2563EB",
    fg="white",
    relief="flat",
    font=("Arial", 11, "bold")
).pack(pady=7)


tk.Button(
    sidebar,
    text="➕   Add Student",
    width=22,
    height=2,
    bg=SIDEBAR_COLOR,
    fg="white",
    relief="flat",
    font=("Arial", 11),
    command=add_student_window
).pack(pady=7)


tk.Button(
    sidebar,
    text="📋   View Students",
    width=22,
    height=2,
    bg=SIDEBAR_COLOR,
    fg="white",
    relief="flat",
    font=("Arial", 11),
    command=view_students_window
).pack(pady=7)


tk.Button(
    sidebar,
    text="🔍   Search Student",
    width=22,
    height=2,
    bg=SIDEBAR_COLOR,
    fg="white",
    relief="flat",
    font=("Arial", 11),
    command=search_student_window
).pack(pady=7)


tk.Button(
    sidebar,
    text="✏️   Update Student",
    width=22,
    height=2,
    bg=SIDEBAR_COLOR,
    fg="white",
    relief="flat",
    font=("Arial", 11),
    command=update_student_window
).pack(pady=7)


tk.Button(
    sidebar,
    text="🗑️   Delete Student",
    width=22,
    height=2,
    bg=SIDEBAR_COLOR,
    fg="white",
    relief="flat",
    font=("Arial", 11),
    command=delete_student_window
).pack(pady=7)


# ================= MAIN CONTENT =================

main_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

main_frame.pack(
    side="right",
    fill="both",
    expand=True
)


# ================= HEADER =================

header = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

header.pack(
    fill="x",
    padx=40,
    pady=(35, 10)
)


tk.Label(
    header,
    text="Dashboard",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 28, "bold")
).pack(anchor="w")


tk.Label(
    header,
    text="Welcome back! Manage your students easily.",
    bg=BG_COLOR,
    fg=MUTED_COLOR,
    font=("Arial", 12)
).pack(anchor="w", pady=(5, 0))


# ================= STATISTICS =================

stats_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

stats_frame.pack(
    fill="x",
    padx=40,
    pady=30
)


# Total Students Card

course_count_card = tk.Frame(
    stats_frame,
    bg=CARD_COLOR,
    width=230,
    height=140
)

course_count_card.pack(side="left", padx=20)
course_count_card.pack_propagate(False)

tk.Label(
    course_count_card,
    text="📚",
    bg=CARD_COLOR,
    font=("Arial", 25)
).pack(pady=(15, 0))

tk.Label(
    course_count_card,
    text="TOTAL COURSES",
    bg=CARD_COLOR,
    fg=MUTED_COLOR,
    font=("Arial", 10, "bold")
).pack()

course_count_label = tk.Label(
    course_count_card,
    text="0",
    bg=CARD_COLOR,
    fg="#2563EB",
    font=("Arial", 25, "bold")
)

course_count_label.pack()


student_card = tk.Frame(
    stats_frame,
    bg=CARD_COLOR,
    width=230,
    height=140
)

student_card.pack(
    side="left",
    padx=(0, 20)
)

student_card.pack_propagate(False)


tk.Label(
    student_card,
    text="👨‍🎓",
    bg=CARD_COLOR,
    font=("Arial", 25)
).pack(pady=(15, 0))


tk.Label(
    student_card,
    text="TOTAL STUDENTS",
    bg=CARD_COLOR,
    fg=MUTED_COLOR,
    font=("Arial", 10, "bold")
).pack()


total_label = tk.Label(
    student_card,
    text="0",
    bg=CARD_COLOR,
    fg="#2563EB",
    font=("Arial", 25, "bold")
)

total_label.pack()




# Courses Card

course_card = tk.Frame(
    stats_frame,
    bg=CARD_COLOR,
    width=230,
    height=140
)

course_card.pack(
    side="left",
    padx=20
)

course_card.pack_propagate(False)


tk.Label(
    course_card,
    text="📚",
    bg=CARD_COLOR,
    font=("Arial", 25)
).pack(pady=(15, 0))


tk.Label(
    course_card,
    text="MANAGEMENT",
    bg=CARD_COLOR,
    fg=MUTED_COLOR,
    font=("Arial", 10, "bold")
).pack()


tk.Label(
    course_card,
    text="STUDENTS",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 18, "bold")
).pack(pady=5)


# Database Card

database_card = tk.Frame(
    stats_frame,
    bg=CARD_COLOR,
    width=230,
    height=140
)

database_card.pack(
    side="left",
    padx=20
)

database_card.pack_propagate(False)


tk.Label(
    database_card,
    text="💾",
    bg=CARD_COLOR,
    font=("Arial", 25)
).pack(pady=(15, 0))


tk.Label(
    database_card,
    text="DATABASE",
    bg=CARD_COLOR,
    fg=MUTED_COLOR,
    font=("Arial", 10, "bold")
).pack()


tk.Label(
    database_card,
    text="SQLITE",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 18, "bold")
).pack(pady=5)


# ================= QUICK ACTION =================

quick_frame = tk.Frame(
    main_frame,
    bg=CARD_COLOR,
    height=170
)

quick_frame.pack(
    fill="x",
    padx=40,
    pady=10
)

quick_frame.pack_propagate(False)


tk.Label(
    quick_frame,
    text="Quick Actions",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 18, "bold")
).pack(
    anchor="w",
    padx=25,
    pady=(20, 10)
)


tk.Button(
    quick_frame,
    text="+  Add New Student",
    bg="#2563EB",
    fg="white",
    relief="flat",
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    command=add_student_window
).pack(
    side="left",
    padx=25
)


tk.Button(
    quick_frame,
    text="📋  View All Students",
    bg="#E5E7EB",
    fg=TEXT_COLOR,
    relief="flat",
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    command=view_students_window
).pack(
    side="left",
    padx=10
)

# ================= RECENT STUDENTS =================

recent_frame = tk.Frame(
    main_frame,
    bg=CARD_COLOR,
    height=150
)

recent_frame.pack(
    fill="x",
    padx=40,
    pady=(10, 20)
)

recent_frame.pack_propagate(False)

tk.Label(
    recent_frame,
    text="Recent Students",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 17, "bold")
).pack(
    anchor="w",
    padx=20,
    pady=(12, 5)
)

columns = ("ID", "Name", "Course", "Phone")

recent_table = ttk.Treeview(
    recent_frame,
    columns=columns,
    show="headings",
    height=4
)

recent_table.heading("ID", text="ID")
recent_table.heading("Name", text="Name")
recent_table.heading("Course", text="Course")
recent_table.heading("Phone", text="Phone")

recent_table.column("ID", width=60)
recent_table.column("Name", width=220)
recent_table.column("Course", width=180)
recent_table.column("Phone", width=180)

recent_table.pack(
    fill="x",
    padx=20
)


def load_recent_students():

    for item in recent_table.get_children():
        recent_table.delete(item)

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, course, phone
        FROM students
        ORDER BY id DESC
        LIMIT 5
    """)

    students = cursor.fetchall()

    conn.close()

    for student in students:
        recent_table.insert(
            "",
            "end",
            values=student
        )


load_recent_students()

# ================= TOTAL UPDATE =================

show_total()


# ================= RUN =================

root.mainloop()