from student import Student

class StudentList:
    def __init__(self):
        self.students = []
        
    def print_all(self):
        for elem in self.students:
            str_for_print = (
                "Student name is {}, phone is {}, age is {}, city is {}".format(elem.name, elem.phone, elem.age, elem.city))
            print(str_for_print)

    def add_new_element(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        city = input("Please enter student city: ")

        new_item = Student(name, phone, age, city)
        insert_position = 0
        for item in self.students:
            if name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, new_item)
        print("New element has been added")

    def delete_element(self):
        name = input("Please enter name to be deleted: ")
        delete_position = -1
        for item in self.students:
            if name == item.name:
                delete_position = self.students.index(item)
                break
        if delete_position == -1:
            print("Element was not found")
        else:
            print("Delete position " + str(delete_position))
            del self.students[delete_position]

    def update_element(self):
        name = input("Please enter name to be updated: ")
        user_position = -1

        for i, item in enumerate(self.students):
            if name == item.name:
                user_position = i
                break

        if user_position == -1:
            print("Student not found")
        else:
            print(f"Student found:")
            updated_fields = {
                "name": input("Enter the new name: "),
                "phone": input("Enter the new phone: "),
                "age": input("Enter the new age: "),
                "city": input("Enter the new city: "),
            }

            del self.students[user_position]

            insert_position = 0
            for i, elem in enumerate(self.students):
                if updated_fields["name"] > elem.name:
                    insert_position += 1
                else:
                    break

            updated_student = Student(**updated_fields)
            self.students.insert(insert_position, updated_student)
            print("Student information updated")

