def average_rating(list_student, name_course, attribute_name):
    all_values = []

    for student in list_student:
        if name_course in getattr(student, attribute_name):
            for value in getattr(student, attribute_name)[name_course]:
                all_values.append(value)

    if not all_values:
        return 0

    return sum(all_values) / len(all_values)


def average_homework_grade(list_student, name_course):
    return average_rating(list_student, name_course, 'grades')


def average_lecture_rating(list_lecture, name_course):
    return average_rating(list_lecture, name_course, 'lecture_evaluations')
