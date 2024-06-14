from person import Person
import sqlite3

class Student(Person):
    def __init__(self,id,name, age, email, grade):
        super().__init__(id,name, age, email)
        self.grade = grade
        self.courses = []

    def get_grade(self):
        return self.grade

    def enroll_course(self, course):
        if course not in [c['name'] for c in self.courses]:
            self.courses.append({'name': course, 'grade': None})
            print(f"Enrolled in {course}")
        else:
            print(f"Already enrolled in {course}")

    def withdraw_course(self, course_name):
        for course in self.courses:
            if course['name'] == course_name:
                self.courses.remove(course)
                print(f"Withdrew from {course_name}")
                return
        print(f"Not enrolled in {course_name}")

    def calculate_gpa(self):
        if not self.courses:
            return 0.0
        total_points = sum([course['grade'] for course in self.courses if course['grade'] is not None])
        return total_points / len([course for course in self.courses if course['grade'] is not None])

    def list_courses(self):
        return [course['name'] for course in self.courses]

    def display_info(self):
        base_info = super().display_info()
        courses_info = ", ".join(self.list_courses())
        return f"{base_info}, Grade: {self.grade}, Courses: {courses_info}"