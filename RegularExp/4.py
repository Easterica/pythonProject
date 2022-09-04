class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old"


class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __repr__(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old and I am teaching {self.subject}"


human = Human("Gosho", 23)
print(human)
teacher = Teacher("Pesho", 25, "matematika")
print(teacher)