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

####Main####

def main():
    create_tables()
    students = []
    instructors = []
    courses = []

    while True:
        print("Welcome to the School Management System!")
        print("1. Add Undergraduate Student")
        print("2. Add Graduate Student")
        print("3. Add Instructor")
        print("4. Add Course")
        print("5. Register Student to Course")
        print("6. Remove Student from Course")
        print("7. Display Student Information")
        print("8. Display Instructor Information")
        print("9. Display Course Information")
        print("10. Display Average Grade for Course")
        print("11. Display Average Grade for All Courses")
        print("12. Create your schedule")
        print("13. report")
        print("14. submitgrades")



        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id=input_id()
            name = input_name()
            age = input_age()
            email = input_email()
            major = input_major()
            grade=input_grade()
            student = UndergraduateStudent(id,name, age, email, major,grade)
            add_undergraduate_student(name,age,email,major)
            students.append(student)
            print("Undergraduate student added successfully.")
        
        elif choice == "2":
            id=input_id()
            name = input_name()
            age = input_age()
            email = input_email()
            advisor = input_advisor()
            student = GraduateStudent(id,name, age, email, advisor)
            students.append(student)
            add_graduate_student(name,age,email,advisor)
            print("Graduate student added successfully.")
        
        elif choice == "3":
            id=input_id()
            name = input_instructor_name()
            age = input_age()
            email = input_email()
            department = input_department()
            instructor = Instructor(id,name, age, email, department)
            instructors.append(instructor)
            add_instructor(name,age,email,department)
            print("Instructor added successfully.")
        
        elif choice == "4":
            id=input_course_id()
            name = input("Enter course name: ")
            instructor_name = input("Enter instructor name: ")
            capacity = int(input("Enter capacity: "))
            add_course(name,instructor_name,capacity)

        elif choice == "5":
            student_name= input_name()
            student_id = input_id()
            course_id = input_course_id()
            register_student_to_course(student_id,course_id,student_name)

        
        elif choice == "6":
            student_id = input_id()
            course_id = input_course_id()
            remove_student_from_course(student_id,course_id)

        elif choice == "7":
            student_id = input("Enter student id: ")
            display_student_info(student_id)

        elif choice == "8":
            instructor_id = input("Enter instructor id: ")
            display_instructor_info(instructor_id)

        elif choice == "9":
            course_id = input("Enter course id: ")
            display_course_info(course_id)
        
        elif choice == "10":
            course_id=input_course_id()
            display_average_grade_for_course(course_id)
        
        elif choice == "11":
            average_grades_for_all_courses()
        
        elif choice == "12":
            student_id=input_id()
            course_id=input_course_id()
            lectime=input_lecTime()
            schedule(student_id,course_id,lectime)

#تقرير لجداول جميع الطلاب
        elif choice == "13":
            display_all_schedule()

        elif choice == "14":
            student_id=input_id()
            course_id=input_course_id()
            finish_course(student_id,course_id)



            

        
        elif choice == "0":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()