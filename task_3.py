import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('student.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS student (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sub_1_marks INTEGER CHECK(sub_1_marks BETWEEN 0 AND 100),
    sub_2_marks INTEGER CHECK(sub_2_marks BETWEEN 0 AND 100),
    sub_3_marks INTEGER CHECK(sub_3_marks BETWEEN 0 AND 100)
)''')
conn.commit()

def is_valid_roll_no(roll_no):
    return roll_no.isdigit()

def is_valid_marks(marks):
    return marks.isdigit() and 0 <= int(marks) <= 100

def is_valid_name(name):
    return name.strip() != ""

def add_student():
    def submit():
        roll = roll_no.get()
        student_name = name.get()
        marks1 = sub1.get()
        marks2 = sub2.get()
        marks3 = sub3.get()

        if not is_valid_roll_no(roll):
            messagebox.showerror("Error", "Roll No must be an integer!")
        elif not is_valid_name(student_name):
            messagebox.showerror("Error", "Name cannot be empty!")
        elif not (is_valid_marks(marks1) and is_valid_marks(marks2) and is_valid_marks(marks3)):
            messagebox.showerror("Error", "Marks must be integers between 0 and 100!")
        else:
            try:
                c.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)", 
                          (roll, student_name, marks1, marks2, marks3))
                conn.commit()
                messagebox.showinfo("Success", "Student record added successfully!")
                add_win.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Roll No already exists!")

    add_win = Toplevel()
    add_win.title("Add Student Record")
    add_win.config(bg="#f4f4f4")
    
    Label(add_win, text="Roll No", font=("Arial", 20)).pack(pady=10)
    roll_no = Entry(add_win, font=("Arial", 20))
    roll_no.pack(pady=5)

    Label(add_win, text="Name", font=("Arial", 20)).pack(pady=10)
    name = Entry(add_win, font=("Arial", 20))
    name.pack(pady=5)

    Label(add_win, text="Sub 1 Marks", font=("Arial", 20)).pack(pady=10)
    sub1 = Entry(add_win, font=("Arial", 20))
    sub1.pack(pady=5)

    Label(add_win, text="Sub 2 Marks", font=("Arial", 20)).pack(pady=10)
    sub2 = Entry(add_win, font=("Arial", 20))
    sub2.pack(pady=5)

    Label(add_win, text="Sub 3 Marks", font=("Arial", 20)).pack(pady=10)
    sub3 = Entry(add_win, font=("Arial", 20))
    sub3.pack(pady=5)

    Button(add_win, text="Submit", font=("Arial", 20), command=submit, bg="#4CAF50", fg="white").pack(pady=20)

def display_students():
    display_win = Toplevel()
    display_win.title("Display Student Records")
    display_win.config(bg="#f4f4f4")

    c.execute("SELECT * FROM student")
    records = c.fetchall()
    
    text_area = Text(display_win, height=30, width=80, font=("Arial", 20), bg="#fff", fg="#333")
    text_area.pack(pady=20)

    if records:
        for record in records:
            text_area.insert(END, f"Roll No: {record[0]}, Name: {record[1]}, Sub_1: {record[2]}, Sub_2: {record[3]}, Sub_3: {record[4]}\n")
    else:
        text_area.insert(END, "No records found!")

def update_student():
    def submit():
        roll = roll_no.get()
        student_name = name.get()
        marks1 = sub1.get()
        marks2 = sub2.get()
        marks3 = sub3.get()

        if not is_valid_roll_no(roll):
            messagebox.showerror("Error", "Roll No must be an integer!")
        elif not is_valid_name(student_name):
            messagebox.showerror("Error", "Name cannot be empty!")
        elif not (is_valid_marks(marks1) and is_valid_marks(marks2) and is_valid_marks(marks3)):
            messagebox.showerror("Error", "Marks must be integers between 0 and 100!")
        else:
            # Check if record exists
            c.execute("SELECT * FROM student WHERE roll_no=?", (roll,))
            if c.fetchone() is None:
                messagebox.showerror("Error", "No record found with this Roll No!")
            else:
                c.execute('''UPDATE student SET name=?, sub_1_marks=?, sub_2_marks=?, sub_3_marks=? WHERE roll_no=?''', 
                          (student_name, marks1, marks2, marks3, roll))
                conn.commit()
                messagebox.showinfo("Success", "Student record updated successfully!")
                update_win.destroy()

    update_win = Toplevel()
    update_win.title("Update Student Record")
    update_win.config(bg="#f4f4f4")

    Label(update_win, text="Roll No", font=("Arial", 20)).pack(pady=10)
    roll_no = Entry(update_win, font=("Arial", 20))
    roll_no.pack(pady=5)

    Label(update_win, text="Name", font=("Arial", 20)).pack(pady=10)
    name = Entry(update_win, font=("Arial", 20))
    name.pack(pady=5)

    Label(update_win, text="Sub 1 Marks", font=("Arial", 20)).pack(pady=10)
    sub1 = Entry(update_win, font=("Arial", 20))
    sub1.pack(pady=5)

    Label(update_win, text="Sub 2 Marks", font=("Arial", 20)).pack(pady=10)
    sub2 = Entry(update_win, font=("Arial", 20))
    sub2.pack(pady=5)

    Label(update_win, text="Sub 3 Marks", font=("Arial", 20)).pack(pady=10)
    sub3 = Entry(update_win, font=("Arial", 20))
    sub3.pack(pady=5)

    Button(update_win, text="Submit", font=("Arial", 20), command=submit, bg="#4CAF50", fg="white").pack(pady=20)

def delete_student():
    def submit():
        roll = roll_no.get()
        if not is_valid_roll_no(roll):
            messagebox.showerror("Error", "Roll No must be an integer!")
        else:
           
            c.execute("SELECT * FROM student WHERE roll_no=?", (roll,))
            if c.fetchone() is None:
                messagebox.showerror("Error", "No record found with this Roll No!")
            else:
                c.execute("DELETE FROM student WHERE roll_no=?", (roll,))
                conn.commit()
                messagebox.showinfo("Success", "Student record deleted successfully!")
                delete_win.destroy()

    delete_win = Toplevel()
    delete_win.title("Delete Student Record")
    delete_win.config(bg="#f4f4f4")

    Label(delete_win, text="Roll No", font=("Arial", 20)).pack(pady=20)
    roll_no = Entry(delete_win, font=("Arial", 20))
    roll_no.pack(pady=10)

    Button(delete_win, text="Delete", font=("Arial", 20), command=submit, bg="#f44336", fg="white").pack(pady=20)

root = Tk()
root.title("Student Records")
root.config(bg="#e0e0e0")

Label(root, text="Student Records", font=("Arial", 30, "bold"), bg="#e0e0e0", fg="#333").pack(pady=30)
Button(root, text="Add Student", font=("Arial", 20), width=20, command=add_student, bg="#2196F3", fg="white").pack(pady=45)
Button(root, text="Display Students", font=("Arial", 20), width=20, command=display_students, bg="#009688", fg="white").pack(pady=45)
Button(root, text="Update Student", font=("Arial", 20), width=20, command=update_student, bg="#FFC107", fg="black").pack(pady=45)
Button(root, text="Delete Student", font=("Arial", 20), width=20, command=delete_student, bg="#f44336", fg="white").pack(pady=45)


root.mainloop()
conn.close()
