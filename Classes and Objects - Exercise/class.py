class Class:

    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = list()
        self.grades = list()

    def add_student(self, name, grade):
        if len(self.students) < 22:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):

        avg_grade = sum(self.grades) / len(self.grades)
        return f"{avg_grade:.2f}"

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {float((Class.get_average_grade(self))):.2f}"


