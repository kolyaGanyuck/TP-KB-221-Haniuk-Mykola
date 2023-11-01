import os
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Створення об'єктів класу Student
students = [
    Student("John", 17),
    Student("Alice", 18),
    Student("Bob", 19),
    Student("Eva", 20),
    Student("Oleg", 21)
]

# Запитати користувача за яким параметром сортувати
sort_parameter = input("Введіть параметр сортування (name або age): ")

if sort_parameter not in ["name", "age"]:
    print("Невірний параметр сортування")
else:
    # Відсортувати студентів за вибраним параметром
    if sort_parameter == "name":
        sorted_students = sorted(students, key=lambda student: student.name)
    else:
        sorted_students = sorted(students, key=lambda student: student.age)

    # Вивести відсортований список студентів
    for student in sorted_students:
        print(f"Name: {student.name}, Age: {student.age}")
        
        

    script_directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(script_directory, "sorted_students.txt")
    
    with open(file_path, "w") as file:
        for student in sorted_students:
            file.write(f"Name: {student.name}, Age: {student.age}\n")
        print(f"Дані були записані у файл '{file_path}'")