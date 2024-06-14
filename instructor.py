from person import Person
import sqlite3

class Instructor(Person):
    def __init__(self, id,name, age, email, department):
        super().__init__(id,name, age, email)
        self.department = department

    def set_department(self, department):
        self.department = department

    def assign_grade(self, student, course_name, grade):
        for course in student.courses:
            if course['name'] == course_name:
                course['grade'] = grade
                print(f"Assigned grade {grade} to {student.name} for {course_name}")
                break

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Department: {self.department}"
    
    