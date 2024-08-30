from person import Student

class Course:
    """
    A class used to represent a course in the Student Management System.

    Attributes
    ----------
    course_name : str
        The name of the course.
    course_id : str
        The ID of the course.
    enrolled_students : list[Student]
        A list to keep track of students enrolled in the course.
    """

    def __init__(self, course_name: str, course_id: str) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def __str__(self) -> str:
        students = ', '.join(student.name for student in self.enrolled_students)  # List student names for clarity
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}, Enrolled Students: [{students}]"

    def enroll_student(self, student: Student) -> None:
        """
        Enrolls a student in the course if they are not already enrolled.

        Parameters
        ----------
        student : Student
            The Student object to be enrolled in the course.
        """
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def unenroll_student(self, student: Student) -> None:
        """
        Unenrolls a student from the course if they are currently enrolled.

        Parameters
        ----------
        student : Student
            The Student object to be unenrolled from the course.
        """
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)


class Enrollment:
    """
    A class used to represent the enrollment of a student in a course in the Student Management System.

    Attributes
    ----------
    student : Student
        The student enrolled.
    course : Course
        The course in which the student is enrolled.
    grade : str, optional
        The grade assigned to the student (default is None).

    Methods
    -------
    set_grade(grade: str)
        Assigns a grade to the student for this enrollment.
    """

    def __init__(self, student: Student, course: Course, grade: str = None) -> None:
        self.student = student
        self.course = course
        self.grade = grade

    def __str__(self) -> str:
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}"

    def __eq__(self, other: object) -> bool:
        """
        Checks equality between two Enrollment objects based on student, course, and grade.

        Parameters
        ----------
        other : Enrollment
            Another enrollment object to compare with.

        Returns
        -------
        bool
            True if both enrollments have the same student, course, and grade, False otherwise.
        """
        if not isinstance(other, Enrollment):
            return False
        return self.student == other.student and self.course == other.course and self.grade == other.grade

    def set_grade(self, grade: str) -> None:
        """
        Assigns a grade to the student for this enrollment.

        Parameters
        ----------
        grade : str
            The grade to assign to the student.
        """
        self.grade = grade
