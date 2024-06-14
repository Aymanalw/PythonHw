import re

def input_course_id():
    id = input("Enter course id: ")
    while not id.isdigit() or int(id) <= 0:
        print("id must be a positive number.")
        id = input("Enter id: ")
    return int(id)

def input_id():
    id = input("Enter id: ")
    while not id.isdigit() or int(id) <= 0:
        print("id must be a positive number.")
        id = input("Enter id: ")
    return int(id)

def input_name():
    name = input("Enter student name: ")
    while not name:
        print("Name cannot be empty.")
        name = input("Enter name: ")
    return name

def input_age():
    age = input("Enter age: ")
    while not age.isdigit() or int(age) <= 0:
        print("Age must be a positive number.")
        age = input("Enter age: ")
    return int(age)

def input_email():
    email = input("Enter email: ")
    while not validate_email(email):
        print("Invalid email format.")
        email = input("Enter email: ")
    return email

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

def input_grade():
    grade = input("Enter grade: ")
    while not grade:
        print("Grade cannot be empty.")
        grade = input("Enter grade: ")
    return grade

def input_major():
    major = input("Enter major: ")
    while not major:
        print("Major cannot be empty.")
        major = input("Enter major: ")
    return major

def input_advisor():
    advisor = input("Enter advisor name: ")
    while not advisor:
        print("Advisor name cannot be empty.")
        advisor = input("Enter advisor name: ")
    return advisor

def input_department():
    department = input("Enter department: ")
    while not department:
        print("Department cannot be empty.")
        department = input("Enter department: ")
    return department

def input_course_name():
    name = input("Enter course name: ")
    while not name:
        print("Name cannot be empty.")
        name = input("Enter name: ")
    return name


def input_instructor_name():
    name = input("Enter instructor name: ")
    while not name:
        print("Name cannot be empty.")
        name = input("Enter name: ")
    return name

def input_lecTime():
    valid_times = ["8:00 AM", "10:00 AM", "12:00 PM", "2:00 PM"]
    while True:
        lecture_time = input("Enter lecture time (8:00 AM, 10:00 AM, 12:00 PM, 2:00 PM): ")
        if lecture_time in valid_times:
            return lecture_time
        else:
            print("Invalid time. Please choose from 8:00 AM, 10:00 AM, 12:00 PM, or 2:00 PM.")