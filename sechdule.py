import sqlite3

class Schedule:
    def __init__(self):
        self.courses = []
        self.timeslots = {}

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def schedule_course(self, course, timeslot):
        if timeslot in self.timeslots:
            print(f"Timeslot {timeslot} is already occupied.")
        else:
            self.timeslots[timeslot] = course

    def create_schedule(self):
        for timeslot, course in self.timeslots.items():
            print(f"{timeslot}: {course.name}")

    def display_schedule(self):
        for timeslot, course in self.timeslots.items():
            print(f"{timeslot}: {course.name}")
