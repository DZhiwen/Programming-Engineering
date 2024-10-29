class Student:
    def __init__(self, name, age, group_number, average_grade):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def display_info(self):
        return f"name: {self.name}, age: {self.age}"

    def scholarship_amount(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        else:
            return 0
        
    def display_scholarship(self):
        scholarship = self.scholarship_amount()
        return f"{self.name}'s scholarship: {scholarship}p"

    def compare_scholarship(self, other):
        if self.scholarship_amount()  >  other.scholarship_amount():
            print(f"{self.name}'s scholarship is higher than {other.name}.")
        elif self.scholarship_amount() < other.scholarship_amount():
            print(f"{self.name}'s scholarship is lower than {other.name}.")
        else:
            print(f"{self.name}'s scholarship is equal to {other.name}.")       

class GraduateStudent(Student):
    def __init__(self, name, age, group_number, average_grade, research_work):
        super().__init__(name, age, group_number, average_grade)#super调用父类的方法super вызывает метод родительского класса
        self.research_work = research_work

    def scholarship_amount(self):
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        else:
            return 0


# 示例使用Например:
Igor = Student("Igor", 19, "class1", 4)
Ivan = GraduateStudent("Ivan", 23, "class2", 4, "Hydroacoustics")
Li_Hua =Student("Li_Hua", 20, "class3", 5)

print(Igor.display_info())
print(Ivan.display_info())
print(Li_Hua.display_info())
print(Igor.display_scholarship())
print(Ivan.display_scholarship())
Igor.compare_scholarship(Ivan)
Li_Hua.compare_scholarship(Ivan)
