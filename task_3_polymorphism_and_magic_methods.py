class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        average_grade = self.average_student_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        result = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {average_grade}\n"
            f"Курсы в процессе изучения: {courses_in_progress_str}\n"
            f"Завершенные курсы: {finished_courses_str}"
        )

        return result

    def __lt__(self, other):
        return self.average_student_grade() < other.average_lecture_grade()

    def __le__(self, other):
        return self.average_student_grade() <= other.average_lecture_grade()

    def __eq__(self, other):
        return self.average_student_grade() == other.average_lecture_grade()

    def __ne__(self, other):
        return self.average_student_grade() != other.average_lecture_grade()

    def __gt__(self, other):
        return self.average_student_grade() > other.average_lecture_grade()

    def __ge__(self, other):
        return self.average_student_grade() >= other.average_lecture_grade()

    def rate_hw(self, lecturer, course, grade):
        is_valid_lecturer = isinstance(lecturer, Lecturer)
        is_valid_course = course in self.courses_in_progress and course in lecturer.courses_attached
        is_valid_grade = 0 <= grade <= 10

        if is_valid_lecturer and is_valid_course and is_valid_grade:
            lecturer.lecture_evaluations.setdefault(course, []).append(grade)

            return f'Оценка {grade} успешно добавлена по курсу {course}'
        else:
            return 'Ошибка'

    def average_student_grade(self):
        all_values = []

        for values_list in self.grades.values():
            for value in values_list:
                all_values.append(value)

        return sum(all_values) / len(all_values)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_evaluations = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_lecture_grade()}"

    def __lt__(self, other):
        return self.average_lecture_grade() < other.average_student_grade()

    def __le__(self, other):
        return self.average_lecture_grade() <= other.average_student_grade()

    def __eq__(self, other):
        return self.average_lecture_grade() == other.average_student_grade()

    def __ne__(self, other):
        return self.average_lecture_grade() != other.average_student_grade()

    def __gt__(self, other):
        return self.average_lecture_grade() > other.average_student_grade()

    def __ge__(self, other):
        return self.average_lecture_grade() >= other.average_student_grade()

    def average_lecture_grade(self):
        all_values = []

        for values_list in self.lecture_evaluations.values():
            for value in values_list:
                all_values.append(value)

        return sum(all_values) / len(all_values)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

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

    print(cool_reviewer)
    print(student1)
    print(student2)

    lecturer = Lecturer("Reno", "Logan")
    lecturer.courses_attached += ['Python', 'Java']

    student1.rate_hw(lecturer, 'Python', 7)
    student1.rate_hw(lecturer, 'Java', 6)
    student2.rate_hw(lecturer, 'Python', 8)
    student2.rate_hw(lecturer, 'Java', 9)

    print(lecturer)

    print(lecturer < student1)
    print(lecturer == student2)
