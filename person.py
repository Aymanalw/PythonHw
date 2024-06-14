import re
import sqlite3

class Person:
    # next_id = 1

    def __init__(self,id,name,age,email):
        self.id=id
        self.name = name
        self.age = age
        self.email = email

    # def generate_id(self):
    #     id_number = Person.next_id
    #     Person.next_id += 1
    #     return id_number

    def display_info(self):
             return {
            "email": self.email,
            "age": self.age,
            "ID_number": self.id_number,
            "name": self.name,
        }

    # def save_to_db(self):
    #     with sqlite3.connect('student_db.db') as conn:
    #         c = conn.cursor()
    #         c.execute('''
    #             INSERT INTO Person (id, name, age, email)
    #             VALUES (?, ?, ?, ?)
    #         ''', (self.id_number, self.name, self.age, self.email))
    #         conn.commit()
  

