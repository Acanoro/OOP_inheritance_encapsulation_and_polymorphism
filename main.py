from lecturer import Lecturer
from reviewer import Reviewer
from student import Student

from utils import *

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
