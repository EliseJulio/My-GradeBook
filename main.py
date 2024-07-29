#!/usr/bin/python3
import json

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            total_credits = sum(course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = self._find_student_by_email(student_email)
        course = self._find_course_by_name(course_name)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_GPA(self, student_email):
        student = self._find_student_by_email(student_email)
        if student:
            student.calculate_GPA()
            return student.GPA
        return None

    def calculate_ranking(self):
        self.student_list.sort(key=lambda student: student.GPA, reverse=True)
        return [(student.names, student.GPA) for student in self.student_list]

    def search_by_grade(self, course_name, grade):
        course = self._find_course_by_name(course_name)
        if not course:
            return []
        students_with_grade = []
        for student in self.student_list:
            for registered_course in student.courses_registered:
                if registered_course['course'].name == course_name and registered_course['grade'] == grade:
                    students_with_grade.append(student)
                    break
        return students_with_grade

    def generate_transcript(self, student_email):
        student = self._find_student_by_email(student_email)
        if not student:
            return None
        transcript = f"Transcript for {student.names} ({student.email}):\n"
        transcript += "Courses Registered:\n"
        for course in student.courses_registered:
            transcript += f"  - {course['course'].name} (Grade: {course['grade']}, Credits: {course['credits']})\n"
        transcript += f"GPA: {student.GPA}\n"
        return transcript

    def _find_student_by_email(self, email):
        for student in self.student_list:
            if student.email == email:
                return student
        return None

    def _find_course_by_name(self, name):
        for course in self.course_list:
            if course.name == name:
                return course
        return None


def main():
    gradebook = GradeBook()
    while True:
        print("Grade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif choice == "4":
            student_email = input("Enter student email: ")
            gpa = gradebook.calculate_GPA(student_email)
            if gpa is not None:
                print(f"GPA for {student_email}: {gpa}")
            else:
                print("Student not found.")
        elif choice == "5":
            ranking = gradebook.calculate_ranking()
            print("Student Ranking:")
            for rank, (names, gpa) in enumerate(ranking, start=1):
                print(f"{rank}. {names} - GPA: {gpa}")
        elif choice == "6":
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            students = gradebook.search_by_grade(course_name, grade)
            if students:
                print(f"Students with grade {grade} in course {course_name}:")
                for student in students:
                    print(f"  - {student.names} ({student.email})")
            else:
                print("No students found with that grade in the specified course.")
        elif choice == "7":
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(transcript)
            else:
                print("Student not found.")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
