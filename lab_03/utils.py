import csv

class Utils:
    @staticmethod
    def load_from_csv(filename):
        students_list = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_list.append(row)
        return students_list

    @staticmethod
    def save_to_csv(filename, students_list):
        with open(filename, "w", newline="") as file:
            fieldnames = ["name", "phone", "age", "city"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students_list)