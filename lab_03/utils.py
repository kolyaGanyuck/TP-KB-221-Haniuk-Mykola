import csv
from student import Student
from student_list import StudentList

class Utils:
    @staticmethod
    def load_from_csv(filename):
        students_list = StudentList()
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["name"], row["phone"], row["age"], row["city"])
                students_list.students.append(student)
        return students_list

    @staticmethod
    def save_to_csv(filename, students_list):
        with open(filename, "w", newline='') as csvfile:
            fieldnames = ["name", "phone", "age", "city"]  # Include "city" in the fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in students_list.students:
                writer.writerow({"name": row.name, "phone": row.phone, "age": row.age, "city": row.city})
                