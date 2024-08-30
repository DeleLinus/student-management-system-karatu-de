## Student Management System

The **Student Management System** is a Python-based application designed to manage students, instructors, courses, and enrollments efficiently. It provides an easy-to-use interface for adding, updating, and removing entities, enrolling students in courses, assigning grades, and retrieving information about students and courses.


## Table of Contents

- [Student Management System](#student-management-system)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)


## Features

- **Add, Update, and Remove** students, instructors, and courses.
- **Enroll and Unenroll** students in courses.
- **Assign Grades** to students for specific courses.
- **Retrieve Information** about students enrolled in a course and courses a student is enrolled in.
- **Administrative Utilities**: Easily retrieve all students, instructors, courses, and enrollments in the system.

## Installation

To get started with the Student Management System, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DeleLinus/student-management-system-karatu-de.git
   cd student-management-system
   ```

2. **Install the required dependencies**:

    This project does not have any external dependencies. Ensure you have Python Python 3.12.3 installed.

3. **Run the application**:

    Navigate to the project directory and run the main module:
    ```bash
    python main.py
    ```
## Usage
**Creating a New Student Management System**

1. **Initialize the System**: You can start by creating an instance of the `StudentManagementSystem` class.

    ```python
    from student_management_system import StudentManagementSystem

    sms = StudentManagementSystem()
    ```
2. **Add Entities**: Create `Student`, `Instructor`, and `Course` objects, and add them to the system.

    ```python
    from person import Student, Instructor
    from course import Course

    # Create Students
    student1 = Student(id_number=1, name="John Doe", major="Computer Science")
    student2 = Student(id_number=2, name="Jane Smith", major="Mathematics")

    # Add Students
    sms.add_student(student1)
    sms.add_student(student2)

    # Similarly, add instructors and courses
    ```
3. **Enroll Students in Courses**:
    ```python
    sms.enroll_student(student_id=1, course_id="CS101")
    sms.enroll_student(student_id=2, course_id="MATH101")
    ```

4. **Assign Grades**:
    ```python
    sms.assign_grade(student_id=1, course_id="CS101", grade="A")
    ```
5. **Retrieve Information:**
    ```python
    students_in_course = sms.get_students_in_course("CS101")
    print(students_in_course)
    ```
6. **Run the provided `main.py` to see a sample usage scenario**:
    ```bash
    python main.py
    ```


## Modules
    Modular structure
    ├── main.py
    ├── student_management_system.py
    ├── person.py
    └── course.py

Aside the  `main.py` which is a sample usage file, this project consists of three key modules:

- `student_management_system.py`: Core module that manages the system's functionalities, including adding/removing students, instructors, and courses; enrolling students in courses; and assigning grades.

- `person.py`: Defines the Student and Instructor classes, representing individuals in the system.

- `course.py`: Defines the Course and Enrollment classes, representing courses and student enrollments.


