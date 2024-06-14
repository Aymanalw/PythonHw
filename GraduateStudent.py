from student import Student
import sqlite3

class GraduateStudent(Student):
    def __init__(self, id,name, age, email, advisor):
        super().__init__(id,name, age, email, "Graduate")
        self.advisor = advisor

    def set_advisor(self, advisor):
        self.advisor = advisor

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Advisor: {self.advisor}"