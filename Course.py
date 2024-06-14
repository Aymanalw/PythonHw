import sqlite3
class Course:
    # next_id = 1

    def __init__(self, id,name, instructor, capacity):
        self.name = name
        self.id_number = id
        # Course.next_id += 1
        self.instructor = instructor
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            student.enroll_course(self.name)
            print(f"Added {student.name} to {self.name}")
        else:
            print(f"Course {self.name} is full.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            student.withdraw_course(self.name)
            print(f"Removed {student.name} from {self.name}")
        else:
            print(f"{student.name} is not in this course.")

    def is_full(self):
        return len(self.students) >= self.capacity

    def display_info(self):
        student_names = ", ".join([student.name for student in self.students])
        return f"Course Name: {self.name}, ID: {self.id_number}, Instructor: {self.instructor}, Capacity: {self.capacity}, Students: {student_names}"