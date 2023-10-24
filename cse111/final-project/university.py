# Dylan Butterfield, CSE 111, 3:15 Class
import mysql.connector


# 1. Establish Database Connection
def establish_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="squal23dev1/!",
        database="university"
    )


# 2. Retrieve Data Functions
def retrieve_college():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM college"
        cursor.execute(query)
        college = cursor.fetchall()
        cursor.close()
        conn.close()
        return college
    except mysql.connector.Error as error:
        print(f"Error retrieving {college} data:", error)
        return []


def retrieve_course():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM course"
        cursor.execute(query)
        course = cursor.fetchall()
        cursor.close()
        conn.close()
        return course
    except mysql.connector.Error as error:
        print(f"Error retrieving {course} data:", error)
        return []


def retrieve_department():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM department"
        cursor.execute(query)
        department = cursor.fetchall()
        cursor.close()
        conn.close()
        return department
    except mysql.connector.Error as error:
        print(f"Error retrieving {department} data:", error)
        return []


def retrieve_person():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM person"
        cursor.execute(query)
        person = cursor.fetchall()
        cursor.close()
        conn.close()
        return person
    except mysql.connector.Error as error:
        print(f"Error retrieving {person} data:", error)
        return []


def retrieve_section():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM section"
        cursor.execute(query)
        section = cursor.fetchall()
        cursor.close()
        conn.close()
        return section
    except mysql.connector.Error as error:
        print(f"Error retrieving {section} data:", error)
        return []


def retrieve_term():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM term"
        cursor.execute(query)
        term = cursor.fetchall()
        cursor.close()
        conn.close()
        return term
    except mysql.connector.Error as error:
        print(f"Error retrieving {term} data:", error)
        return []


def retrieve_enrollment():
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM enrollment"
        cursor.execute(query)
        enrollment = cursor.fetchall()
        cursor.close()
        conn.close()
        return enrollment
    except mysql.connector.Error as error:
        print(f"Error retrieving {enrollment} data:", error)
        return []


# 3. Data Presentation Functions
def display_college(college):
    for college in college:
        print("College ID:", college[0])
        print("College Name:", college[1])
        print("------------------------")


def display_department(department):
    for department in department:
        print("Department ID:", department[0])
        print("Department Name:", department[1])
        print("Department Code:", department[2])
        print("College ID:", department[3])
        print("------------------------")


def display_course(course):
    for course in course:
        print("Course ID:", course[0])
        print("Course Name:", course[1])
        print("Course Code:", course[2])
        print("Department ID:", course[3])
        print("------------------------")


def display_person(person):
    for person in person:
        print("Person ID:", person[0])
        print("First Name:", person[1])
        print("Last Name:", person[2])
        print("Gender:", person[3])
        print("City:", person[4])
        print("State:", person[5])
        print("Birthdate:", person[6])
        print("------------------------")


def display_section(section):
    for section in section:
        print("Section ID:", section[0])
        print("Section Number:", section[1])
        print("Capacity:", section[2])
        print("Course ID:", section[3])
        print("Term ID:", section[4])
        print("------------------------")


def display_term(term):
    for term in term:
        print("Term ID:", term[0])
        print("Term Name:", term[1])
        print("Term Year:", term[2])
        print("------------------------")


def display_enrollment(enrollment):
    for record in enrollment:
        print("Section ID:", record[0])
        print("Person ID:", record[1])
        print("Person Type:", record[2])
        print("Department ID:", record[3])
        print("------------------------")


def main():
    # 4. Retrieve data for each table
    college = retrieve_college()
    course = retrieve_course()
    department = retrieve_department()
    person = retrieve_person()
    section = retrieve_section()
    term = retrieve_term()
    enrollment = retrieve_enrollment()

    # 5. Display the retrieved data for each table
    print("College:")
    display_college(college)
    print()

    print("Course:")
    display_course(course)
    print()

    print("Department:")
    display_department(department)
    print()

    print("Person:")
    display_person(person)
    print()

    print("Section:")
    display_section(section)
    print()

    print("Term:")
    display_term(term)
    print()

    print("Enrollment:")
    display_enrollment(enrollment)
    print()


if __name__ == "__main__":
    main()
