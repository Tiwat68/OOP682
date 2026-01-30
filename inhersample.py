from models.Person import Person
from models.staff import staff
from models.students import student
        
        
student = student(123456789,"halo",20,"s123")
aff = staff(123546548,"bob",35,"s12545")

print(f"{student.name} {student.age} {student.student_id}")
print(f"{aff.name} {aff.age} {aff.staff_id}")


def get_person_info(person):
    print(isinstance(person, Person))
    return f"name: {Person.name}, age:{Person.age}"

get_person_info(student)
get_person_info(staff)

class employee:
    pass
