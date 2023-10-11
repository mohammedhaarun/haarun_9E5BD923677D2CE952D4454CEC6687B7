class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("John Doe", "1001", 3.8),
    Student("Jane Smith", "1002", 3.9),
    Student("Alex Johnson", "1003", 3.5),
    Student("Emily Wilson", "1004", 3.7)
]

sorted_students = sort_students(students)

for student in sorted_students:
    print("Name:", student.name)
    print("Roll Number:", student.roll_number)
    print("CGPA:", student.cgpa)
    print()

