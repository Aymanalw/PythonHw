import customtkinter as ctk
import sqlite3
import re
from dbUtils import *
from person import Person
from student import Student
from GraduateStudent import GraduateStudent
from UndergraduateStudent import UndergraduateStudent
from Course import Course
from instructor import Instructor
from sechdule import Schedule
from utils import *

button_properties = {
    "hover_color": "#83B4FF",
    "corner_radius": 32,
    "fg_color": "#003285",
    "text_color": "#FDFFE2"
}




def main():
    def add_undergraduate_student_callback():
        def submit_callback():
            name = name_entry.get()
            age = int(age_entry.get())
            email = email_entry.get()
            major = major_entry.get()
            person_id = add_person(name, age, email)
            add_student(name, major) 
            add_undergraduate_student(name, age, email, major)
            result_label.configure(text="Undergraduate student added successfully.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Add Undergraduate Student")
        popup.geometry("400x400")  # النافذة التي تظهر بعد ما اختار

        name_entry = ctk.CTkEntry(popup, placeholder_text="Name")
        name_entry.pack(pady=10)
        age_entry = ctk.CTkEntry(popup, placeholder_text="Age")
        age_entry.pack(pady=10)
        email_entry = ctk.CTkEntry(popup, placeholder_text="Email")
        email_entry.pack(pady=10)
        major_entry = ctk.CTkEntry(popup, placeholder_text="Major")
        major_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def add_graduate_student_callback():
        def submit_callback():
            name = name_entry.get()
            age = int(age_entry.get())
            email = email_entry.get()
            advisor = advisor_entry.get()
            add_graduate_student(name, age, email, advisor)
            result_label.configure(text="Graduate student added successfully.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Add Graduate Student")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        name_entry = ctk.CTkEntry(popup, placeholder_text="Name")
        name_entry.pack(pady=10)
        age_entry = ctk.CTkEntry(popup, placeholder_text="Age")
        age_entry.pack(pady=10)
        email_entry = ctk.CTkEntry(popup, placeholder_text="Email")
        email_entry.pack(pady=10)
        advisor_entry = ctk.CTkEntry(popup, placeholder_text="Advisor")
        advisor_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def add_instructor_callback():
        def submit_callback():
            name = name_entry.get()
            age = int(age_entry.get())
            email = email_entry.get()
            department = department_entry.get()
            person_id = add_person(name, age, email)
            add_instructor(name, age, email, department)
            result_label.configure(text="Instructor added successfully.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Add Instructor")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        name_entry = ctk.CTkEntry(popup, placeholder_text="Name")
        name_entry.pack(pady=10)
        age_entry = ctk.CTkEntry(popup, placeholder_text="Age")
        age_entry.pack(pady=10)
        email_entry = ctk.CTkEntry(popup, placeholder_text="Email")
        email_entry.pack(pady=10)
        department_entry = ctk.CTkEntry(popup, placeholder_text="Department")
        department_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def add_course_callback():
        def submit_callback():
            name = course_name_entry.get()
            instructor = course_instructor_entry.get()
            capacity = int(course_capacity_entry.get())
            add_course(name, instructor, capacity)
            result_label.configure(text="Course added successfully.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Add Course")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        course_name_entry = ctk.CTkEntry(popup, placeholder_text="Course Name")
        course_name_entry.pack(pady=10)
        course_instructor_entry = ctk.CTkEntry(popup, placeholder_text="Course Instructor")
        course_instructor_entry.pack(pady=10)
        course_capacity_entry = ctk.CTkEntry(popup, placeholder_text="Course Capacity")
        course_capacity_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)
#############ناقص تابعين ريجستر وريموف
    def register_student_to_course_callback():
        def submit_callback():
            sid=student_id_entry.get()
            cid=course_id_entry.get()
            name=name_entry.get()
            register_student_to_course(sid,cid,name)
            result_label.configure(text="Student registerd successfully.")
            popup.destroy()

            
        popup = ctk.CTkToplevel(root)
        popup.title("Register student to  Specific Course")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة


        name_entry = ctk.CTkEntry(popup, placeholder_text="Name")
        name_entry.pack(pady=10)
        student_id_entry = ctk.CTkEntry(popup, placeholder_text="Student ID")
        student_id_entry.pack(pady=10)
        course_id_entry=ctk.CTkEntry(popup,placeholder_text="Corse ID")
        course_id_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)
        
            

    def remove_student_from_course_callback():
        def submit_callback():
            sid=student_id_entry.get()
            cid=course_id_entry.get()
            remove_student_from_course(sid,cid)
            result_label.configure(text="Student removed successfully.")
            popup.destroy()


        popup = ctk.CTkToplevel(root)
        popup.title("Remove Student from Course")
        popup.geometry("400x400") 

        student_id_entry = ctk.CTkEntry(popup, placeholder_text="Student ID")
        student_id_entry.pack(pady=10)
        course_id_entry=ctk.CTkEntry(popup,placeholder_text="Corse ID")
        course_id_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def display_student_info_callback():
        def submit_callback():
            student_id = int(student_id_entry.get())
            student = display_student_info(student_id)
            if student:
                result_label.configure(text=f"Student ID: {student[0]}\nName: {student[1]}\nGrade: {student[2]}")
            else:
                result_label.configure(text="Student not found.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Display Student Info")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        student_id_entry = ctk.CTkEntry(popup, placeholder_text="Student ID")
        student_id_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def display_instructor_info_callback():
        def submit_callback():
            instructor_id = int(instructor_id_entry.get())
            instructor = display_instructor_info(instructor_id)
            if instructor:
                result_label.configure(text=f"Instructor ID: {instructor[0]}\nName: {instructor[1]}\nDepartment: {instructor[2]}")
            else:
                result_label.configure(text="Instructor not found.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Display Instructor Info")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        instructor_id_entry = ctk.CTkEntry(popup, placeholder_text="Instructor ID")
        instructor_id_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def display_course_info_callback():
        def submit_callback():
            course_id = int(course_id_entry.get())
            course = display_course_info(course_id)
            if course:
                result_label.configure(text=f"Course ID: {course[0]}\nName: {course[1]}\nInstructor: {course[2]}\nCapacity: {course[3]}")
            else:
                result_label.configure(text="Course not found.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Display Course Info")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        course_id_entry = ctk.CTkEntry(popup, placeholder_text="Course ID")
        course_id_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def display_average_grade_for_course_callback():
        def submit_callback():
            course_id = int(course_id_entry.get())
            course = display_course_info(course_id)
            if course:
                conn = sqlite3.connect('student_db.db')
                c = conn.cursor()
                c.execute('SELECT AVG(grade) FROM Enrollment WHERE course_id = ?', (course_id,))
                avg_grade = c.fetchone()[0]
                result_label.configure(text=f"Average Grade for Course {course[1]}: {avg_grade}")
                conn.close()
            else:
                result_label.configure(text="Course not found.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Display Average Grade for Course")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        course_id_entry = ctk.CTkEntry(popup, placeholder_text="Course ID")
        course_id_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def display_average_grade_for_all_courses_callback():
        conn = sqlite3.connect('student_db.db')
        c = conn.cursor()
        c.execute('SELECT name, (SELECT AVG(grade) FROM Enrollment WHERE course_id = Course.id) FROM Course')
        avg_grades = c.fetchall()
        result_text = "Average Grades for All Courses:\n" + "\n".join([f"{course[0]}: {course[1]}" for course in avg_grades])
        result_label.configure(text=result_text)
        conn.close()

    def create_schedule_callback():
        def submit_callback():
            student_id = int(student_id_entry.get())
            course_id = int(course_id_entry.get())
            lecture_time = lecture_time_entry.get()
            conn = sqlite3.connect('student_db.db')
            c = conn.cursor()
            c.execute('SELECT name FROM Student WHERE id = ?', (student_id,))
            student_name = c.fetchone()[0]
            c.execute('SELECT name FROM Course WHERE id = ?', (course_id,))
            course_name = c.fetchone()[0]
            c.execute('INSERT INTO Schedule (student_name, student_id, course_name, course_id, lecture_time) VALUES (?, ?, ?, ?, ?)', 
                      (student_name, student_id, course_name, course_id, lecture_time))
            conn.commit()
            conn.close()
            result_label.configure(text="Schedule created successfully.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Create Schedule")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        student_id_entry = ctk.CTkEntry(popup, placeholder_text="Student ID")
        student_id_entry.pack(pady=10)
        course_id_entry = ctk.CTkEntry(popup, placeholder_text="Course ID")
        course_id_entry.pack(pady=10)
        lecture_time_entry = ctk.CTkEntry(popup, placeholder_text="Lecture Time")
        lecture_time_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    def generate_report_callback():
        display_all_schedule()


    def submit_grades_callback():
        def submit_callback():
            student_id = int(student_id_entry.get())
            course_id = int(course_id_entry.get())
            grade = grade_entry.get()
            conn = sqlite3.connect('student_db.db')
            c = conn.cursor()
            c.execute('UPDATE Enrollment SET grade = ? WHERE student_id = ? AND course_id = ?', (grade, student_id, course_id))
            conn.commit()
            conn.close()
            result_label.configure(text="Grade submitted successfully.")
            popup.destroy()

        popup = ctk.CTkToplevel(root)
        popup.title("Submit Grades")
        popup.geometry("400x400")  #للاعرف حجم النافذة بعد الاختيارة

        student_id_entry = ctk.CTkEntry(popup, placeholder_text="Student ID")
        student_id_entry.pack(pady=10)
        course_id_entry = ctk.CTkEntry(popup, placeholder_text="Course ID")
        course_id_entry.pack(pady=10)
        grade_entry = ctk.CTkEntry(popup, placeholder_text="Grade")
        grade_entry.pack(pady=10)

        submit_button = ctk.CTkButton(popup, text="Submit", command=submit_callback, **button_properties)
        submit_button.pack(pady=10)

    
    root = ctk.CTk()
    root.title("School Management System")
    root.geometry("600x700")

    
    welcome_label = ctk.CTkLabel(root, text="Welcome to the School Management System!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    button_frame = ctk.CTkFrame(root)
    button_frame.pack(pady=20)


    buttons = [
        ("Add Undergraduate Student", add_undergraduate_student_callback),
        ("Add Graduate Student", add_graduate_student_callback),
        ("Add Instructor", add_instructor_callback),
        ("Add Course", add_course_callback),
        ("Register Student to Course",register_student_to_course_callback),
        ("Remove Student from Course",remove_student_from_course_callback),
        ("Display Student Info", display_student_info_callback),
        ("Display Instructor Info", display_instructor_info_callback),
        ("Display Course Info", display_course_info_callback),
        ("Display Average Grade for Course", display_average_grade_for_course_callback),
        ("Display Average Grade for All Courses", display_average_grade_for_all_courses_callback),
        ("Create Schedule", create_schedule_callback),
        ("Generate Report", generate_report_callback),
        ("Submit Grades", submit_grades_callback)
    ]

    for text, command in buttons:
        button = ctk.CTkButton(button_frame, text=text, command=command, **button_properties)
        button.pack(pady=5)

    result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    create_tables()
    root.mainloop()

if __name__ == "__main__":
    main()

