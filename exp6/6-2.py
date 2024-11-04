class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(Person):
    def __init__(self, name, age, sex, title, quality, salary, prize):
        super().__init__(name, age, sex)
        self.title = title
        self.quality = quality
        self.salary = salary
        self.prize = prize


def main():
    teacher = Teacher("羽生咲", 24, "male", "Associate Professor", "excellent", 12000, 5000)
    print(teacher.name)
    print(teacher.age)
    print(teacher.sex)
    print(teacher.title)
    print(teacher.quality)
    print(teacher.salary)
    print(teacher.prize)
    income = teacher.prize + teacher.salary
    print(income)


if __name__ == "__main__":
    main()