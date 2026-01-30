class classroom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []
    
    def add_student(self, student_name):
        if len(self.students) < self.capacity:
            self.students.append(student_name)
            return True
        return False
    
    def __len__(self):
        return len(self.students)
    
    def __getitem__(self, index):
        return self.students[index]