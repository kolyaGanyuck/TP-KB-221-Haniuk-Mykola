from sys import argv
from utils import Utils

class StudentList(list):
    def print_all(self):
        for elem in self:
            str_for_print = (
                "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", age is " + elem["age"] + ", city is " + elem["city"]
            )
            print(str_for_print)

    def add_new_element(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        city = input("Please enter student city: ")

        new_item = {"name": name, "phone": phone, "age": age, "city": city}
        insert_position = 0
        for item in self:
            if name > item["name"]:
                insert_position += 1
            else:
                break
        self.insert(insert_position, new_item)
        print("New element has been added")

    def delete_element(self):
        name = input("Please enter name to be deleted: ")
        delete_position = -1
        for item in self:
            if name == item["name"]:
                delete_position = self.index(item)
                break
        if delete_position == -1:
            print("Element was not found")
        else:
            print("Delete position " + str(delete_position))
            del self[delete_position]

    def update_element(self):
        name = input("Please enter name to be updated: ")
        user_position = -1

        for i, item in enumerate(self):
            if name == item["name"]:
                user_position = i
                break

        if user_position == -1:
            print("Student not found")
        else:
            print(f"Student found: {self[user_position]}")
            updated_fields = {
                "name": input("Enter the new name: "),
                "phone": input("Enter the new phone: "),
                "age": input("Enter the new age: "),
                "city": input("Enter the new city: "),
            }
            del self[user_position]
            insert_position = 0
            for i, elem in enumerate(self):
                if updated_fields["name"] > elem["name"]:
                    insert_position += 1
                else:
                    break

            self.insert(insert_position, updated_fields)
            print("Student information updated")

def main():
    if len(argv) != 2:
        print("Usage: python script.py filename.csv")
        return

    filename = argv[1]
    students_list = StudentList(Utils.load_from_csv(filename))

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                students_list.add_new_element()
                students_list.print_all()
            case "u":
                print("Existing element will be updated")
                students_list.update_element()
            case "d":
                print("Element will be deleted")
                students_list.delete_element()
            case "p":
                print("List will be printed")
                students_list.print_all()
            case "x":
                print("Saving to CSV and exiting...")
                Utils.save_to_csv(filename, students_list)
                return
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
