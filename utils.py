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
