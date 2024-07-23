#!/usr/bin/python3
from student import Student
from course import Course
from gradebook import GradeBook

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
