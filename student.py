from lecturer import Lecturer


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
            all_values.extend(values_list)

        if not all_values:
            return 0

        return sum(all_values) / len(all_values)
