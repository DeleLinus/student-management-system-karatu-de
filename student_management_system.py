from person import Student, Instructor
from course import Course, Enrollment

class StudentManagementSystem:
    """
    A class to manage students, instructors, courses, and enrollments in a Student Management System.

    The `StudentManagementSystem` class provides functionality to add, update, and remove students, instructors, and courses.
    It also allows for enrolling students in courses, assigning grades, and retrieving information about student-course relationships.
    The class uses dictionaries and lists to maintain and manage data effectively.

    Methods
    -------
    add_student(student: Student) -> None
        Adds a new `Student` object to the system.

    remove_student(id_number: int) -> None
        Removes a `Student` object from the system based on the student's ID number.

    update_student_details(current_id_number: int, new_name: str = None, new_major: str = None, new_id_number: int = None) -> None
        Updates the details of an existing student in the system.

    add_instructor(instructor: Instructor) -> None
        Adds a new `Instructor` object to the system.

    remove_instructor(id_number: int) -> None
        Removes an `Instructor` object from the system based on the instructor's ID number.

    update_instructor_details(current_id_number: int, new_name: str = None, new_department: str = None, new_id_number: int = None) -> None
        Updates the details of an existing instructor in the system.

    add_course(course: Course) -> None
        Adds a new `Course` object to the system.

    remove_course(course_id: str) -> None
        Removes a `Course` object from the system based on the course ID.

    update_course_details(current_course_id: str, new_course_name: str = None, new_course_id: str = None) -> None
        Updates the details of an existing course in the system.

    unenroll_student(student_id: int, course_id: str) -> None
        Unenrolls a student from a course based on student and course IDs.

    enroll_student(student_id: int, course_id: str) -> None
        Enrolls a student in a course based on student and course IDs.

    assign_grade(student_id: int, course_id: str, grade: str) -> None
        Assigns a grade to a student for a specific course.

    get_students_in_course(course_id: str) -> list[Student]
        Retrieves a list of students enrolled in a specific course.

    get_courses_of_student(student_id: int) -> list[Course]
        Retrieves a list of courses in which a specific student is enrolled.
    get_all_students -> List[Student]
        Retrieve a list of all students in the system.
    get_all_instructors -> List[Instructor]
        Retrieve a list of all instructors in the system.
    get_all_courses -> List[Course]
        Retrieve a list of all courses in the system.
    get_all_enrollments() -> list[Enrollement]
        Retrieve a list of all enrollments in the system.

    """

    def __init__(self) -> None:
        
        self.students =  {} 
        self.instructors = {}
        self.courses = {} 
        self.enrollments = []

    def add_student(self, student: Student):
        """
        Adds a Student object to the students dictionary.

        Parameters
        ----------
        student : Student
            The Student object to be added to the system.
        """
        if student.id_number in self.students:
            raise ValueError(f"Student with ID {student.id_number} already exists.")
        self.students[student.id_number] = student

    def remove_student(self, id_number:int):
        """
        Removes a Student object from the students dictionary.

        Parameters
        ----------
        id_number : int
            The student id of the Student object to be removed from the system.
        """
        if id_number not in self.students:
            raise ValueError(f"Student with ID {id_number} doesn't exist.")
        
        # remove student object from course enrollment list
        for course_id in self.courses:
            if self.students[id_number] in self.courses[course_id].enrolled_students:
                 self.unenroll_student(id_number, course_id)
        # remove student object from students repo
        del self.students[id_number]
    
    def update_student_details(self, current_id_number:int, new_name:str = None, new_major:str = None, new_id_number:int = None) -> None:
        """
        Updates the student object attributes from the students dictionary.

        Parameters
        ----------
        current_id_number : int
            The student's existing id of the Student object to be updated in the system.
        new_name : str
            The student's new name to be changed into.
        new_major : str
            The student's new major to be updated on the student object in the system.
        new_id_number : int
            The student's existing id of the Student object to be updated in the system.
        """
        if current_id_number not in self.students:
            raise ValueError(f"Student with ID {current_id_number} doesn't exist.")
        
        student = self.students[current_id_number]

        if new_name:
            student.name = new_name

        if new_major:
            student.major = new_major

        if new_id_number:
            if new_id_number in self.students:
                raise ValueError(f"Student with ID {new_id_number} already exists.")
            self.students[new_id_number] = self.students.pop(current_id_number)
            student.id_number = new_id_number # student still references the same memory as self.students[new_id_number]

    
    def add_instructor(self, instructor: Instructor):
        """
        Adds an Instructor object to the instructors dictionary.

        Parameters
        ----------
        instructor : Instructor
            The Instructor object to be added to the system.
        """
        if instructor.id_number in self.instructors:
            raise ValueError(f"Instructor with ID {instructor.id_number} already exists.")
        self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, id_number:int):
        """
        Removes an Instructor object from the instructors dictionary.

        Parameters
        ----------
        id_number : int
            The instructor id of the Instructor object to be removed from the system.
        """
        if id_number not in self.instructors:
            raise ValueError(f"Instructor with ID {id_number} doesn't exist.")
        
        del self.instructors[id_number]
    
    def update_instructor_details(self, current_id_number:int, new_name:str = None, new_department:str = None, new_id_number:int = None) -> None:
        """
        Updates the Instructor object attributes from the instructors dictionary.

        Parameters
        ----------
        current_id_number : int
            The instructor's existing id of the Instructor object to be updated in the system.
        new_name : str
            The instructor's new name to be changed into.
        new_department : str
            The instructor's new department to be updated on the instructor object in the system.
        new_id_number : int
            The instructor's existing id of the Instructor object to be updated in the system.
        """
        if current_id_number not in self.instructors:
            raise ValueError(f"Instructor with ID {current_id_number} doesn't exist.")
        
        instructor = self.instructors[current_id_number]

        if new_name:
            instructor.name = new_name

        if new_department:
            instructor.department = new_department

        if new_id_number:
            if new_id_number in self.instructors:
                raise ValueError(f"Instructor with ID {new_id_number} already exists.")
            self.instructors[new_id_number] = self.instructors.pop(current_id_number)
            instructor.id_number = new_id_number # instructor still references the same memory as self.instructors[new_id_number]
             
    def add_course(self, course: Course):
        """
        Adds a Course object to the courses dictionary.

        Parameters
        ----------
        course : Course
            The Course object to be added to the system.
        """
        if course.course_id in self.courses:
            raise ValueError(f"Course with ID {course.course_id} already exists.")
        self.courses[course.course_id] = course

    def remove_course(self, course_id: str):
        """
        Removes a Course object from the courses dictionary.

        Parameters
        ----------
        course_id : str
            The course id of the Course object to be removed from the system.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} doesn't exist.")
        
        # remove course object from course enrollment list
        for enrollment in self.enrollments[:]:
            if enrollment.course.course_id == course_id:
                 self.enrollments.remove(enrollment)

        # remove course object from courses repo
        del self.courses[course_id]

    
    def update_course_details(self, current_course_id: str, new_course_name: str = None, new_course_id: str = None) -> None:
        """
        Updates the Course object attributes from the courses dictionary.

        Parameters
        ----------
        current_course_id : str
            The existing course id of the Course object to be updated in the system.
        new_course_name : str
            The new course name to be changed into.
        new_course_id : str
            The existing course id of the Course object to be updated in the system.

        Raises
        ------
        ValueError
            If the course ID does not exist in the system.
            If the course ID already exist in the system.
        """
        if current_course_id not in self.courses:
            raise ValueError(f"Course with ID {current_course_id} doesn't exist.")
        
        course = self.courses[current_course_id]

        if new_course_name:
            course.course_name = new_course_name    
        
        if new_course_id:
            if new_course_id in self.courses:
                raise ValueError(f"Course with ID {new_course_id} already exists.")
            self.courses[new_course_id] = self.courses.pop(current_course_id)
            course.course_id = new_course_id # course still references the same memory as self.courses[new_course_id]
    
    def unenroll_student(self, student_id: int, course_id:str):
        """
        Unenroll a student from a course.

        This method removes a student from a specified course based on the provided student ID and course ID. 
        If the student or course does not exist in the system, a ValueError is raised. 

        Parameters
        ----------
        student_id : int
            The ID of the student to be unenrolled from the course.
        course_id : str
            The ID of the course in which the student is to be unenrolled.

        Raises
        ------
        ValueError
            If the student ID does not exist in the system.
            If the course ID does not exist in the system.

        """
        if student_id not in self.students:
            raise ValueError(f"The Student with ID {student_id} doesn't exist!")
        if course_id not in self.courses:
            raise ValueError(f"The Course with ID {course_id} doesn't exist!")
        
        course = self.courses[course_id]
        student = self.students[student_id]

        course.unenroll_student(student) # unenroll_student() in Course class has a condition to ignore if it already exists
        # remove from Enrollment
        for enrollment in self.enrollments[:]:
            if (enrollment.course.course_id == course_id) and (enrollment.student.id_number == student_id):
                self.enrollments.remove(enrollment)
                break


    def enroll_student(self, student_id: int, course_id:str):
        """
        Enroll a student in a course.

        This method adds a student to a specified course based on the provided student ID and course ID. 
        If the student or course does not exist in the system, a ValueError is raised. 

        Parameters
        ----------
        student_id : int
            The ID of the student to be enrolled in the course.
        course_id : str
            The ID of the course in which the student is to be enrolled.

        Raises
        ------
        ValueError
            If the student ID does not exist in the system.
            If the course ID does not exist in the system.

        """
        if student_id not in self.students:
            raise ValueError(f"The Student with ID {student_id} doesn't exist!")
        if course_id not in self.courses:
            raise ValueError(f"The Course with ID {course_id} doesn't exist!")
        student = self.students[student_id]
        course = self.courses[course_id]
        enrollment = Enrollment(student, course)
        course.enroll_student(student) # enroll_student has a condition to ignore if it already exists
        if enrollment not in self.enrollments:
            self.enrollments.append(enrollment)
    
    def assign_grade(self, student_id: int, course_id: str, grade: str):
        """
        Assign a grade to a student for a specific course.

        Parameters
        ----------
        student_id : int
            The ID of the student to whom the grade is being assigned.
        course_id : str
            The ID of the course for which the grade is being assigned.
        grade : str
            The grade to assign to the student. This could be a letter grade (e.g., "A", "B", "C") 
            or any other grading scheme used by the institution.

        Raises
        ------
        ValueError
            If no matching enrollment is found for the given student ID and course ID.
        """
        
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id and enrollment.course.course_id == course_id:
                enrollment.set_grade(grade)
                return  # exit to avoid unnecessary iteration after the grade is assigned

        raise ValueError(f"No enrollment found for student ID {student_id} in course ID {course_id}.")
        
    def get_students_in_course(self, course_id: str):
        """
        Retrieve a list of students enrolled in a specific course.

        Parameters
        ----------
        course_id : str
            The ID of the course for which to retrieve the list of enrolled students.

        Returns
        -------
        List[Student]
            A list of `Student` objects representing the students enrolled in the specified course.

        Raises
        ------
        KeyError
            If the course ID does not exist in the system's course collection.

        Example
        -------
        students_in_course = sms.get_students_in_course(course_id="C001")
        for student in students_in_course:
            print(student)
        """
        if course_id not in self.courses:
            raise KeyError(f"The Course with ID {course_id} doesn't exist!")
        course = self.courses[course_id]
        return course.enrolled_students

    def get_courses_of_student(self, student_id: str):
        """
        Retrieve a list of courses a specific student is enrolled in.

        Parameters
        ----------
        student_id : int
            The ID of the student for whom to retrieve the list of enrolled courses.

        Returns
        -------
        List[Course]
            A list of `Course` objects representing the courses in which the specified student is enrolled.

        Example
        -------
        courses_of_student = sms.get_courses_of_student(student_id=1)
        for course in courses_of_student:
            print(course)
        """
        if student_id not in self.students:
            raise ValueError(f"The Student with ID {student_id} doesn't exist!")
        return [enrollment.course for enrollment in self.enrollments if enrollment.student.id_number == student_id]

    def get_all_students(self):
        """
        Retrieve a list of all students in the system.

        Returns
        -------
        List[Student]
            A list of `Student` objects representing all the students in the system.

        Example
        -------
        all_students = sms.get_all_students()
        for student in all_students:
            print(student)
        """
        return list(self.students.values())

    def get_all_instructors(self):
        """
        Retrieve a list of all instructors in the system.

        Returns
        -------
        List[Instructor]
            A list of `Instructor` objects representing all the instructors in the system.

        Example
        -------
        all_instructors = sms.get_all_instructors()
        for instructor in all_instructors:
            print(instructor)
        """
        return list(self.instructors.values())

    def get_all_courses(self):
        """
        Retrieve a list of all courses in the system.

        Returns
        -------
        List[Course]
            A list of `Course` objects representing all the courses in the system.

        Example
        -------
        all_courses = sms.get_all_courses()
        for course in all_courses:
            print(course)
        """
        return list(self.courses.values())

    def get_all_enrollments(self):
        """
        Retrieve a list of all enrollments in the system.

        Returns
        -------
        List[Enrollment]
            A list of `Enrollment` objects representing all the enrollments in the system.

        Example
        -------
        all_enrollments = sms.get_all_enrollments()
        for enrollment in all_enrollments:
            print(enrollment)
        """
        return self.enrollments.copy() # .copy() to ensure original enrollments list is not modified when the returned list is manipulated.