class person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
person1 = person("Alex","male",18)
person2 = person("Brian","female",20)
print(person1.name,person1.gender,person1.age)
print(person2.name,person2.gender,person2.age)

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = Employee("Alex",19,40000)
emp2 = Employee("Brian",20,30000)
print(emp1.name,emp1.age,emp1.salary)
print(emp2.name,emp2.age,emp2.salary)

class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
student1 = Student("Raymond",18,"male")
student2 = Student("Malachi",30,"male")
print(student1.name,student1.age,student1.gender)
print(student2.name,student2.age,student2.gender)

class PersonInfo:
    def __init__(self,name,gender,age,salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
p1 = PersonInfo("Bmax","male",18,500000)
p2 = PersonInfo("Cate","female",20,300000)
print(p1.name,p1.gender,p1.age,p1.salary)
print(p2.name,p2.gender,p2.age,p2.salary)
