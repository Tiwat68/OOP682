from models.classroom import Classroom
from models.students import student

oop = Classroom = "OOP"
oop.add_student(student(1,"a",20,"s01"))
oop.add_student(student(2,"v", 22, "s02"))
print(f"{oop.name} regis {len(oop)} student")
oop.add_student(student(3,"T",21,"S03"))

print(len(oop))

print("student class")
for i in range(len(oop)):
    print(oop[i])