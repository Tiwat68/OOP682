class Person:
    def __init__(self, pid,  name, age):
        self.pid = pid
        self.name = name 
        self.age = age
        
    def __str__(self):
        return f"Person_ID: {self.pid} name: {self.name} age:{self.age}"