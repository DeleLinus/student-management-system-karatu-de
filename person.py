class Person:
    """
    A base class used to represent a person involved in the Student Management System,
    such as Students and Instructors.

    Attributes
    ----------
    name : str
        The name of the person.
    id_number : int
        The ID number of the person.
    """
    def __init__(self, name: str, id_number: int) -> None:
        self.name = name
        self.id_number = id_number

    def __str__(self) -> str:
        return f"{self.name}, {self.id_number}"


class Student(Person):
    """
    A class used to represent a student in the Student Management System.

    Inherits from the Person class and adds a specific attribute for the student's course major.

    Attributes
    ----------
    name : str
        The name of the student.
    id_number : int
        The ID number of the student.
    major : str
        The major or field of study of the student.
    """
    def __init__(self, name: str, id_number: int, major: str) -> None:
        # Person.__init__(self, name, id_number) # doesn't follow MRO and the not the best approach
        super().__init__(name, id_number) # follows MRO and the best approach as it maintains class heirarchy
        self.major = major

    def __str__(self) -> str:
        return super().__str__() + f", {self.major}"


class Instructor(Person):
    """
    A class used to represent an instructor in the Student Management System.

    Inherits from the Person class and adds a specific attribute for the instructor's department.

    Attributes
    ----------
    name : str
        The name of the instructor.
    id_number : int
        The ID number of the instructor.
    department : str
        The department of the instructor.
    """
    def __init__(self, name: str, id_number: int, department: str) -> None:
        super().__init__(name, id_number)
        self.department = department

    def __str__(self) -> str:
        return super().__str__() + f", {self.department}"
