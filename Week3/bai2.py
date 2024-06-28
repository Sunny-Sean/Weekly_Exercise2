class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Docter(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Docter - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.list_doi_tuong = []

    def add_person(self, doi_tuong):
        self.list_doi_tuong.append(doi_tuong)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for i in self.list_doi_tuong:
            i.describe()

    def count_docter(self):
        docter = 0
        for i in self.list_doi_tuong:
            if hasattr(i, "specialist"):
                docter += 1
        print(f"Numbef of docter: {docter}")

    def sort_age(self):
        self.list_doi_tuong.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        tong = 0
        so_luong = 0
        for i in self.list_doi_tuong:
            if hasattr(i, "subject"):
                tong += getattr(i, "yob")
                so_luong += 1
        trungbinh = tong/so_luong
        return trungbinh


stu1 = Student("Sunny", 2004, 13)
teach1 = Teacher("teacherA", 1969, "Math")
teach3 = Teacher("teacherC", 1969, "Toan")
doc1 = Docter("DocterA", 1945, "Endocrinologists")
tech2 = Teacher("teacherB", 1995, "History")
doc2 = Docter("docterB", 1975, "Cardiologists")
doc3 = Docter("docter3", 1980, "Hihi")

ward1 = Ward("Ward1")
ward1.add_person(stu1)
ward1.add_person(teach1)
ward1.add_person(teach3)
ward1.add_person(doc1)
ward1.add_person(tech2)
ward1.add_person(doc2)
ward1.add_person(doc3)
ward1.describe()
ward1.sort_age()
ward1.describe()
print(ward1.compute_average())