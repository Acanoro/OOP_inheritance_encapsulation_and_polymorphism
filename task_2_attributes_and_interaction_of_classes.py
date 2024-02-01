class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        is_valid_lecturer = isinstance(lecturer, Lecturer)
        is_valid_course = course in self.courses_in_progress and course in lecturer.courses_attached
        is_valid_grade = 0 <= grade <= 10

        if is_valid_lecturer and is_valid_course and is_valid_grade:
            lecturer.lecture_evaluations.setdefault(course, []).append(grade)

            return f'Оценка {grade} успешно добавлена по курсу {course}'
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_evaluations = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


if __name__ == "__main__":
    student1 = Student('Ruoy', 'Eman', 'ваш_пол_1')
    student1.courses_in_progress += ['Python']

    student2 = Student('John', 'Doe', 'ваш_пол_2')
    student2.courses_in_progress += ['Java']
    student2.courses_in_progress += ['Python']

    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.courses_attached += ['Python', 'Java']

    cool_reviewer.rate_hw(student1, 'Python', 10)
    cool_reviewer.rate_hw(student1, 'Python', 9)
    cool_reviewer.rate_hw(student2, 'Java', 8)
    cool_reviewer.rate_hw(student2, 'Java', 7)

    print(student1.grades)
    print(student2.grades)

    lecturer = Lecturer("Reno", "Logan")
    lecturer.courses_attached += ['Python', 'Java']

    student1.rate_hw(lecturer, 'Python', 7)
    student1.rate_hw(lecturer, 'Java', 6)
    student2.rate_hw(lecturer, 'Python', 8)
    student2.rate_hw(lecturer, 'Java', 9)

    print(lecturer.lecture_evaluations)
