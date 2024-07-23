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
