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
            all_values.extend(values_list)

        if not all_values:
            return 0

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


def average_homework_grade(list_student, name_course):
    all_values = []

    for student in list_student:
        if name_course in student.grades:
            for value in student.grades[name_course]:
                all_values.append(value)

    return sum(all_values) / len(all_values)


def average_lecture_rating(list_lecture, name_course):
    all_values = []

    for lecture in list_lecture:
        if name_course in lecture.lecture_evaluations:
            for value in lecture.lecture_evaluations[name_course]:
                all_values.append(value)

    return sum(all_values) / len(all_values)


if __name__ == "__main__":
    # Создаем экземпляры класса Student
    student1 = Student("Иван", "Иванов", "Мужской")
    student1.courses_in_progress = ["Python", "Js"]
    student1.finished_courses = ["Git"]
    student2 = Student("Мария", "Петрова", "Женский")
    student2.courses_in_progress = ["Python", "Js"]
    student2.finished_courses = ["Java"]

    # Создаем экземпляры класса Lecturer
    lecturer1 = Lecturer("Профессор", "Смирнов")
    lecturer1.courses_attached = ["Python", "Js"]
    lecturer2 = Lecturer("Доктор", "Джонсон")
    lecturer2.courses_attached = ["Python", ]

    # Создаем экземпляры класса Reviewer
    reviewer1 = Reviewer("Рецензент", "Джонс")
    reviewer1.courses_attached = ["Python", "Js"]
    reviewer2 = Reviewer("Рецензент", "Смит")
    reviewer2.courses_attached = ["Python", "Js"]

    # Оцениваем домашние задания студентов
    reviewer1.rate_hw(student1, "Python", 9)
    reviewer1.rate_hw(student1, "Js", 8)
    reviewer2.rate_hw(student2, "Python", 7)
    reviewer2.rate_hw(student2, "Js", 10)

    # Оцениваем лекции лекторов
    student1.rate_hw(lecturer1, "Python", 9)
    student1.rate_hw(lecturer1, "Js", 8)
    student2.rate_hw(lecturer2, "Python", 7)

    # Выводим информацию о студентах, лекторах и рецензентах
    print("\nИнформация о студентах:")
    print(student1)
    print("\n")
    print(student2)

    print("\nИнформация о лекторах:")
    print(lecturer1)
    print("\n")
    print(lecturer2)

    print("\nИнформация о практик:")
    print(reviewer1)
    print("\n")
    print(reviewer2)

    # Вычисляем и выводим среднюю оценку за домашние задания по конкретному курсу
    name_course = "Python"
    ahg = average_homework_grade([student1, student2], name_course)
    print(f"\nСредняя оценка за домашние задания по курсу {name_course}: {ahg}")

    # Вычисляем и выводим среднюю оценку за лекции всех лекторов по конкретному курсу
    name_course = "Js"
    ahg = average_lecture_rating([lecturer1, lecturer2], name_course)
    print(f"\nСредняя оценка за лекции по курсу {name_course}: {ahg}")
