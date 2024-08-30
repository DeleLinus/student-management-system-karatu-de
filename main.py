# import modules
from student_management_system import StudentManagementSystem
from person import Student, Instructor
from course import Course

def main():
    # initialize the Student Management System
    sms = StudentManagementSystem()
    
    # create some sample students
    student1 = Student(id_number=1, name="John Doe", major="Computer Science")
    student2 = Student(id_number=2, name="Jane Smith", major="Mathematics")

    # add students to the system
    sms.add_student(student1)
    sms.add_student(student2)
    
    # create some sample instructors
    instructor1 = Instructor(id_number=1, name="Dr. Brown", department="Computer Science")
    instructor2 = Instructor(id_number=2, name="Dr. Green", department="Mathematics")

    # add instructors to the system
    sms.add_instructor(instructor1)
    sms.add_instructor(instructor2)
    
    # create some sample courses
    course1 = Course(course_id="CS101", course_name="Introduction to Computer Science")
    course2 = Course(course_id="MATH101", course_name="Calculus I")
    course3 = Course(course_id="CS102", course_name="Python Programmaing")

    # add courses to the system
    sms.add_course(course1)
    sms.add_course(course2)
    sms.add_course(course3)
    
    # enroll students in courses
    sms.enroll_student(student1.id_number, course1.course_id)
    sms.enroll_student(student1.id_number, course3.course_id)
    sms.enroll_student(student2.id_number, course2.course_id)
    
    # assign grades to students
    sms.assign_grade(student1.id_number, course1.course_id, "A")
    sms.assign_grade(student2.id_number, course2.course_id, "B")

    # print all students in a course
    students_in_cs101 = sms.get_students_in_course("CS101")
    print("Students enrolled in CS101:")
    for student in students_in_cs101:
        print(f"{student.name} (ID: {student.id_number})")

    # print all courses of a student
    courses_of_student1 = sms.get_courses_of_student(student1.id_number)
    print(f"\nCourses enrolled by {student1.name}:")
    for course in courses_of_student1:
        print(f"{course.course_name} (ID: {course.course_id})")

if __name__ == "__main__":
    main()
