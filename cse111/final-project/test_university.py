from university import establish_connection, retrieve_college, retrieve_course, retrieve_department, retrieve_person, retrieve_section, retrieve_term, retrieve_enrollment, display_college, display_department, display_course, display_person, display_section, display_term, display_enrollment

def test_establish_connection():
    # Test database connection
    connection = establish_connection()
    assert connection is not None
    print("Connection test passed.")

def test_retrieve_college():
    # Test retrieve_college function
    college = retrieve_college()
    assert len(college) > 0
    print("retrieve_college test passed.")

def test_retrieve_course():
    # Test retrieve_course function
    course = retrieve_course()
    assert len(course) > 0
    print("retrieve_course test passed.")

def test_retrieve_department():
    # Test retrieve_department function
    department = retrieve_department()
    assert len(department) > 0
    print("retrieve_department test passed.")

def test_retrieve_person():
    # Test retrieve_person function
    person = retrieve_person()
    assert len(person) > 0
    print("retrieve_person test passed.")

def test_retrieve_section():
    # Test retrieve_section function
    section = retrieve_section()
    assert len(section) > 0
    print("retrieve_section test passed.")

def test_retrieve_term():
    # Test retrieve_term function
    term = retrieve_term()
    assert len(term) > 0
    print("retrieve_term test passed.")

def test_retrieve_enrollment():
    # Test retrieve_enrollment function
    enrollment = retrieve_enrollment()
    assert len(enrollment) > 0
    print("retrieve_enrollment test passed.")

def test_display_college():
    # Test display_college function
    college = [("1", "College A"), ("2", "College B")]
    print("Displaying college:")
    display_college(college)

def test_display_department():
    # Test display_department function
    department = [("1", "Department A", "DPTA", "1"), ("2", "Department B", "DPTB", "2")]
    print("Displaying department:")
    display_department(department)

def test_display_course():
    # Test display_course function
    course = [("1", "Course A", "CRSA", "1"), ("2", "Course B", "CRSB", "2")]
    print("Displaying course:")
    display_course(course)

def test_display_person():
    # Test display_person function
    person = [("1", "John", "Doe", "Male", "City A", "State A", "1990-01-01")]
    print("Displaying person:")
    display_person(person)

def test_display_section():
    # Test display_section function
    section = [("1", "Section A", "50", "1", "1"), ("2", "Section B", "30", "2", "2")]
    print("Displaying section:")
    display_section(section)

def test_display_term():
    # Test display_term function
    term = [("1", "Term A", "2023"), ("2", "Term B", "2024")]
    print("Displaying term:")
    display_term(term)

def test_display_enrollment():
    # Test display_enrollment function
    enrollment = [("1", "1", "Student", "1"), ("2", "2", "Instructor", "2")]
    print("Displaying enrollment:")
    display_enrollment(enrollment)

def run_tests():
    test_establish_connection()
    test_retrieve_college()
    test_retrieve_course()
    test_retrieve_department()
    test_retrieve_person()
    test_retrieve_section()
    test_retrieve_term()
    test_retrieve_enrollment()
    test_display_college()
    test_display_department()
    test_display_course()
    test_display_person()
    test_display_section()
    test_display_term()
    test_display_enrollment()

if __name__ == "__main__":
    run_tests()