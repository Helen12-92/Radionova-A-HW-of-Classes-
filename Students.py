class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_from_student(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grades(self):
        every_grades = []
        all_grades = list(self.grades.values())
        for val in all_grades:
            every_grades += val
        every_grades_int = []
        for grade in every_grades:
            grade_int = int(grade)
            every_grades_int.append(grade_int)
        average_grade = round(sum(every_grades_int) / len(every_grades_int), 1)
        return average_grade

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершённые курсы: {', '.join(self.finished_courses)}")

    def __it__(self, other):
        return self.average_grades() < other.average_grads()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grades_lect(self):
        every_grades = []
        all_grades = list(self.grades.values())
        for val in all_grades:
            every_grades += val
        every_grades_int = []
        for grade in every_grades:
            grade_int = int(grade)
            every_grades_int.append(grade_int)
        average_grade_lect = round(sum(every_grades_int) / len(every_grades_int), 1)
        return average_grade_lect

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_lect()}")

    def __it__(self, other):
        return self.average_grades_lect() < other.average_grades_lect()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")

def average_grade_of_course(student_1, student_2, course):
    grades = []
    if isinstance(student_1, Student) and course in student_1.courses_in_progress:
        for grade in student_1.grades[course]:
            grades.append(grade)
    if isinstance(student_2, Student) and course in student_2.courses_in_progress:
        for grade in student_2.grades[course]:
            grades.append(grade)
    all_grades_int = []
    for number in grades:
        number_int = int(number)
        all_grades_int.append(number_int)
        ag_of_course = round(sum(all_grades_int)/len(all_grades_int),1)
    return (f"Средняя оценка за домашние задания по курсу {course}: {ag_of_course}")

def lecturers_ag_of_course(lecturer_1, lecturer_2, course):
    grades = []
    if isinstance(lecturer_1, Lecturer) and course in lecturer_1.courses_attached:
        for grade in lecturer_1.grades[course]:
            grades.append(grade)
    if isinstance(lecturer_2, Lecturer) and course in lecturer_2.courses_attached:
        for grade in lecturer_2.grades[course]:
            grades.append(grade)
    all_grades_int = []
    for number in grades:
        number_int = int(number)
        all_grades_int.append(number_int)
        lect_ag_of_course = round(sum(all_grades_int)/len(all_grades_int),1)
    return (f"Средняя оценка за лекции по курсу {course}: {lect_ag_of_course}")

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

another_reviewer= Reviewer('Jon', 'Dou')
another_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

another_reviewer.rate_hw(some_student, 'Git', 2)
another_reviewer.rate_hw(some_student, 'Git', 8)
another_reviewer.rate_hw(some_student, 'Git', 10)

another_student = Student('Boy', 'Bad', 'some_gender')
another_student.courses_in_progress += ['Python']
another_student.courses_in_progress += ['Git']
another_student.finished_courses += ['Введение в программирование']

some_reviewer.rate_hw(another_student, 'Python', 10)
some_reviewer.rate_hw(another_student, 'Python', 9)
some_reviewer.rate_hw(another_student, 'Python', 10)
another_reviewer.rate_hw(another_student, 'Git', 10)
another_reviewer.rate_hw(another_student, 'Git', 9)
another_reviewer.rate_hw(another_student, 'Git', 8)

some_lecturer = Lecturer('John', 'Snow')
some_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Tirion', 'Lunister')
another_lecturer.courses_attached += ['Git']

some_student.rate_from_student(some_lecturer, 'Python', 10)
some_student.rate_from_student(some_lecturer, 'Python', 8)
some_student.rate_from_student(some_lecturer, 'Python', 10)
another_student.rate_from_student(some_lecturer, 'Python', 10)
another_student.rate_from_student(some_lecturer, 'Python', 10)
another_student.rate_from_student(some_lecturer, 'Python', 10)

some_student.rate_from_student(another_lecturer, 'Git', 10)
some_student.rate_from_student(another_lecturer, 'Git', 9)
some_student.rate_from_student(another_lecturer, 'Git', 9)
another_student.rate_from_student(another_lecturer, 'Git', 7)
another_student.rate_from_student(another_lecturer, 'Git', 8)
another_student.rate_from_student(another_lecturer, 'Git', 8)

print(some_student)
print('\n')
print(another_student)
print('\n')
print(some_lecturer)
print('\n')
print(another_lecturer)
print('\n')
print(some_reviewer)
print('\n')
print(another_reviewer)
print('\n')
print(another_student.average_grades() < some_student.average_grades())
print(some_lecturer.average_grades_lect() < another_lecturer.average_grades_lect())
print('\n')
print(average_grade_of_course(some_student, another_student, 'Python'))
print(lecturers_ag_of_course(some_lecturer, another_lecturer, 'Python'))