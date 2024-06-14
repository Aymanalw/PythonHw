from student import Student

class UndergraduateStudent(Student):
    def __init__(self, id,name, age, email, major,grade):
        super().__init__(id,name, age, email, grade)
        self.major = major

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Major: {self.major}"