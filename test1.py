class child:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender

class teacher:
    def __init__(self,subject,age,gender,salary):
        super().__init__(subject,age,gender,salary)
        self.subject = subject
        self.age = age
        self.gender = gender
        self.salary = salary
teacher1 = teacher("Mathematics", "35", 'male', 200000)
teacher2 = teacher("English", "30", 'female', 100000)
teacher3 = teacher("Kiswahili", "20", 'male', 500000)
print(teacher1.subject, teacher1.age, teacher1.gender, teacher1.salary)
print(teacher2.subject, teacher2.age, teacher2.gender,teacher2.salary)
print(teacher3.subject, teacher3.age, teacher3.gender,teacher3.salary)
