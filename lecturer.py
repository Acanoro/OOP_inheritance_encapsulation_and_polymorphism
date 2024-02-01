from mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_evaluations = {}

    def __str__(self):
        return super().__str__() + f"\nСредняя оценка за лекции: {self.average_lecture_grade()}"

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
