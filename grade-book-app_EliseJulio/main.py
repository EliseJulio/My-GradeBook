#!/usr/bin/env python3

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
            total_credits = sum(course.credits for course in self.courses_registered)
            total_points = sum(course.credits * self.get_grade_point(course) for course in self.courses_registered)
            self.GPA = total_points / total_credits

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def get_grade_point(self, course):
        # Placeholder method to determine grade points for a course.
        # Implement the logic based on your grading system.
        return 4.0  # Assuming full points for each course for simplicity.

    def to_dict(self):
        return {
            "email": self.email,
            "names": self.names,
            "courses_registered": [course.name for course in self.courses_registered],
            "GPA": self.GPA
        }

    @classmethod
    def from_dict(cls, data, courses):
        student = cls(data["email"], data["names"])
        student.courses_registered = [next((c for c in courses if c.name == name), None) for name in data["courses_registered"]]
        student.GPA = data["GPA"]
        return student

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def to_dict(self):
        return {
            "name": self.name,
            "trimester": self.trimester,
            "credits": self.credits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["trimester"], data["credits"])

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        new_student = Student(email, names)
        self.student_list.append(new_student)
        print(f"  Student {names} added successfully! ")

    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)
        print(f"  Course {name} added successfully!  ")

    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")

        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        if student and course:
            student.register_for_course(course)
            print(f"  Student {student.names} registered for course {course.name} successfully!  ")
        else:
            print("Student or course not found.")

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()
            print(f"Student {student.names} has GPA: {student.GPA:.2f}")

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        print("Student rankings by GPA:")
        for i, student in enumerate(self.student_list, start=1):
            print(f"{i}. {student.names} - GPA: {student.GPA:.2f}")

    def search_by_grade(self):
        min_gpa = float(input("Enter minimum GPA: "))
        max_gpa = float(input("Enter maximum GPA: "))
        filtered_students = [s for s in self.student_list if min_gpa <= s.GPA <= max_gpa]
        if filtered_students:
            print(f"Students with GPA between {min_gpa} and {max_gpa}:")
            for student in filtered_students:
                print(f"{student.names} - GPA: {student.GPA:.2f}")
        else:
            print("No students found in the specified GPA range.")

    def generate_transcript(self):
        student_email = input("Enter student email: ")
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"\n  Transcript for {student.names}: ")
            for course in student.courses_registered:
                print(f"Course: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}")
            print(f"GPA: {student.GPA:.2f}\n")
        else:
            print("Student not found.")

    def save_to_file(self, filename="gradebook.json"):
        data = {
            "students": [student.to_dict() for student in self.student_list],
            "courses": [course.to_dict() for course in self.course_list]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("  Data saved successfully!  ")

    def load_from_file(self, filename="gradebook.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.course_list = [Course.from_dict(c) for c in data["courses"]]
            self.student_list = [Student.from_dict(s, self.course_list) for s in data["students"]]
            print("  Data loaded successfully!  ")
        except FileNotFoundError:
            print("No saved data found.")

def main():
    gradebook = GradeBook()
    gradebook.load_from_file()

    while True:
        print("\n" + "*" * 60)
        print("       THE GRADEBOOK       ")
        print("*" * 60)
        print("1. Add Student")
        print("   " + "-" * 56 )
        print("2. Add Course")
        print("   " + "-" * 56 )
        print("3. Register Student for Course")
        print("   " + "-" * 56 )
        print("4. Calculate GPA")
        print("   " + "-" * 56 )
        print("5. Calculate Ranking")
        print("   " + "-" * 56 )
        print("6. Search by Grade")
        print("   " + "-" * 56 )
        print("7. Generate Transcript")
        print("   " + "-" * 56 )
        print("8. Save Data")
        print("   " + "-" * 56 )
        print("9. Exit")
        print("*" * 60)

        choice = input("Select an option (1-9): ")

        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.add_course()
        elif choice == '3':
            gradebook.register_student_for_course()
        elif choice == '4':
            gradebook.calculate_GPA()
        elif choice == '5':
            gradebook.calculate_ranking()
        elif choice == '6':
            gradebook.search_by_grade()
        elif choice == '7':
            gradebook.generate_transcript()
        elif choice == '8':
            gradebook.save_to_file()
        elif choice == '9':
            gradebook.save_to_file()
            print("Exit ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
