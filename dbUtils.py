import sqlite3

def create_tables():
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS Person (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS RegisteredStudent (
            student_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(id),
            FOREIGN KEY (course_id) REFERENCES Course(id)
        )
    ''')

    
    c.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            grade TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES Person(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS UndergraduateStudent (
            id INTEGER PRIMARY KEY,
            student_id INTEGER NOT NULL,
            major TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(id)
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS GraduateStudent (
            id INTEGER PRIMARY KEY,
            student_id INTEGER NOT NULL,
            advisor TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(id)
        )
    ''')        
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            instructor INTEGER NOT NULL,
            capacity INTEGER NOT NULL
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS Schedule (
            student_name TEXT NOT NULL,
            student_id INTEGER NOT NULL,
            course_name TEXT NOT NULL,
            course_id INTEGER NOT NULL,
            lecture_time TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(id),
            FOREIGN KEY (course_id) REFERENCES Course(id)
);

        
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS Instructor (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES Person(id)
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS Enrollment (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            grade TEXT,
            PRIMARY KEY (student_id, course_id),
            FOREIGN KEY (student_id) REFERENCES Student(id),
            FOREIGN KEY (course_id) REFERENCES Course(id)
        )
    ''')
    
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS Schedule (
            student_name TEXT NOT NULL,
            student_id INTEGER NOT NULL,
            course_name TEXT NOT NULL,
            course_id INTEGER NOT NULL,
            lecture_time TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(id),
            FOREIGN KEY (course_id) REFERENCES Course(id)
    )
    """
    )
    conn.commit()
    conn.close()

def add_person(name, age, email):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    c.execute('INSERT INTO Person (name, age, email) VALUES (?, ?, ?)', (name, age, email))
    person_id = c.lastrowid
    conn.commit()
    conn.close()
    return person_id

def add_student(name, grade):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    c.execute('INSERT INTO Student (name, grade) VALUES (?, ?)', (name, grade))
    student_id = c.lastrowid
    conn.commit()
    conn.close()
    return student_id

def add_undergraduate_student(name, age, email, major):
    person_id = add_person(name, age, email)
    student_id = add_student(name, 'Undergraduate')
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    c.execute('INSERT INTO UndergraduateStudent (student_id, major) VALUES (?, ?)', (student_id, major))
    conn.commit()
    conn.close()
    return person_id

def add_graduate_student(name, age, email, advisor):
    person_id = add_person(name, age, email)
    student_id = add_student(name, 'Graduate')
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    c.execute('INSERT INTO GraduateStudent (student_id, advisor) VALUES (?, ?)', (student_id, advisor))
    conn.commit()
    conn.close()
    return person_id

def add_instructor(name, age, email, department):
    person_id = add_person(name, age, email)
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    c.execute('INSERT INTO Instructor (id, name, department) VALUES (?, ?, ?)', (person_id, name, department))
    conn.commit()
    conn.close()
    return person_id

def add_course(name, instructor, capacity):
    if(is_instructor_exists(instructor)):
        conn = sqlite3.connect('student_db.db')
        c = conn.cursor()
        c.execute('INSERT INTO Course (name, instructor, capacity) VALUES (?, ?, ?)', (name, instructor, capacity))
        course_id = c.lastrowid
        conn.commit()
        conn.close()
        return course_id
    else:
        print("instructor not found ")

def displayall_student_info():
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM Student')
    students = c.fetchall()
    
    for student in students:
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Grade:", student[2])
        print("--------------------")
    
    conn.close()


def display_student_info(student_id):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM Student WHERE id = ?', (student_id,))
    student = c.fetchone()
    
    if student:
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Grade:", student[2])
        print("--------------------")
    else:
        print("Student not found.")
    
    conn.close()


def display_instructor_info(instructor_id):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Instructor WHERE id = ?', (instructor_id,))
    instructor = c.fetchone()

    if instructor:
        print("Instructor ID:", instructor[0])
        print("Name:", instructor[1])
        print("Department:", instructor[2])
        print("--------------------")
    else:
        print("Instructor not found.")

    conn.close()


def display_course_info(course_id):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Course WHERE id = ?', (course_id,))
    course = c.fetchone()

    if course:
        print("Course ID:", course[0])
        print("Name:", course[1])
        print("Instructor:", course[2])
        print("Capacity:", course[3])
        print("--------------------")
    else:
        print("Course not found.")

    conn.close()

def is_instructor_exists(instructor_name):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    c.execute('SELECT COUNT(*) FROM Instructor WHERE name = ?', (instructor_name,))
    count = c.fetchone()[0]

    conn.close()

    return count > 0


def register_student_to_course(student_id, course_id, student_name):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    # Check if the student exists
    c.execute("SELECT COUNT(*) FROM Student WHERE id = ?", (student_id,))
    student_count = c.fetchone()[0]

    # Check if the course exists
    c.execute("SELECT COUNT(*) FROM Course WHERE id = ?", (course_id,))
    course_count = c.fetchone()[0]

    if student_count == 0:
        print(f"Student with ID {student_id} not found.")
        conn.close()
        return

    if course_count == 0:
        print(f"Course with ID {course_id} not found.")
        conn.close()
        return

    # Register the student to the course
    c.execute("INSERT INTO RegisteredStudent (student_id, student_name, course_id) VALUES (?, ?, ?)", (student_id, student_name, course_id))
    conn.commit()
    conn.close()
    print(f"Student {student_name} registered for course with ID {course_id}.")




def remove_student_from_course(student_id, course_id):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    
    # بنشوف اذا مسجل اول
    c.execute("SELECT COUNT(*) FROM RegisteredStudent WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    count = c.fetchone()[0] #هون عم شوف اذا السليكت رجعتلي شي او لا 
    
    if count > 0:
        c.execute("DELETE FROM RegisteredStudent WHERE student_id = ? AND course_id = ?", (student_id, course_id))
        conn.commit()
        print(f"Removed student {student_id} from course {course_id}")
    else:
        print(f"Student {student_id} is not registered to course {course_id}")
    
    conn.close()

def schedule(student_id, course_id, lecture_time):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()
    
    # التحقق اذا الطالب موجوج
    c.execute("SELECT COUNT(*) FROM Student WHERE id = ?", (student_id,))
    student_exists = c.fetchone()[0]
    if not student_exists:
        print("Student does not exist.")
        conn.close()
        return
    
    # عم شوف اذا الكورس موجود ومالو فاضي
    c.execute("SELECT capacity FROM Course WHERE id = ?", (course_id,))
    course_info = c.fetchone()
    if course_info is None:
        print("Course does not exist.")
        conn.close()
        return
    capacity = course_info[0]
    
    c.execute("SELECT COUNT(*) FROM RegisteredStudent WHERE course_id = ?", (course_id,))
    enrolled = c.fetchone()[0]
    if enrolled >= capacity:
        print("Course is full.")
        conn.close()
        return
    
    # عم شوف اذا مافي تعارض بالاوقات
    c.execute("SELECT COUNT(*) FROM Schedule WHERE student_id = ? AND lecture_time = ?", (student_id, lecture_time))
    time_conflict = c.fetchone()[0]
    if time_conflict:
        print("Time conflict with another course.")
        conn.close()
        return
    
    # بعج ما اتاأكد من كل شي بضيفو هون
    c.execute('''
        SELECT name FROM Student WHERE id = ?
    ''', (student_id,))
    student_name = c.fetchone()[0]

    c.execute('''
        SELECT name FROM Course WHERE id = ?
    ''', (course_id,))
    course_name = c.fetchone()[0]
    
    c.execute('''
        INSERT INTO Schedule (student_name, student_id, course_name, course_id, lecture_time)
        VALUES (?, ?, ?, ?, ?)
    ''', (student_name, student_id, course_name, course_id, lecture_time))
    
    c.execute('''
        INSERT INTO RegisteredStudent (student_id, student_name, course_id)
        VALUES (?, ?, ?)
    ''', (student_id, student_name, course_id))

    conn.commit()
    conn.close()
    print(f"Student {student_name} registered for course {course_name} at {lecture_time}.")


def display_all_schedule():
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Schedule')
    schedules = c.fetchall()

    if not schedules:
        print("No schedules found.")
    else:
        for schedule in schedules:
            print("Student Name:", schedule[0])
            print("Student ID:", schedule[1])
            print("Course Name:", schedule[2])
            print("Course ID:", schedule[3])
            print("Lecture Time:", schedule[4])
            print("--------------------")

    conn.close()


def finish_course(student_id, course_id):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    # عم اتأكد اذا الطالب مسجل بالكورس
    c.execute("SELECT COUNT(*) FROM RegisteredStudent WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    count = c.fetchone()[0]
    
    if count == 0:
        print("Error: Student is not registered in the course.")
        conn.close()
        return

    
    final_grade = input("Enter the final grade for the student: ")

    c.execute("INSERT INTO Enrollment (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, final_grade))
    conn.commit()
    
    print("Final grade saved successfully.")
    
    conn.close()



def display_average_grade_for_course(course_id):
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    
    c.execute("SELECT AVG(CAST(grade AS FLOAT)) FROM Enrollment WHERE course_id = ?", (course_id,))
    average_grade = c.fetchone()[0]

    if average_grade is not None:
        print(f"Average grade for course with ID {course_id}: {average_grade:.2f}")
    else:
        print(f"No grades found for course with ID {course_id}")

    conn.close()




import sqlite3

def average_grades_for_all_courses():
    conn = sqlite3.connect('student_db.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(DISTINCT course_id) FROM Enrollment")
    total_courses = c.fetchone()[0]

    if total_courses > 0:
        c.execute("SELECT SUM(avg_grade) FROM (SELECT AVG(CAST(grade AS FLOAT)) AS avg_grade FROM Enrollment GROUP BY course_id) AS avg_grades")
        sum_of_avg_grades = c.fetchone()[0]
        
        average_grade = sum_of_avg_grades / total_courses

        print(f"Average grades for all courses: {average_grade:.2f}")
    else:
        print("No grades found for any course.")

    conn.close()




