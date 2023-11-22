import csv

students_list = []

def printAllList():
    for elem in students_list:
        strForPrint = (
            "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", age is " + elem["age"] + ", city is " + elem["city"]
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    city = input("Please enter student city: ")

    newItem = {"name": name, "phone": phone, "age": age, "city": city}
    # find insert position
    insertPosition = 0
    for item in students_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students_list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students_list:
        if name == item["name"]:
            deletePosition = students_list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del students_list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    userPosition = -1

    for i, item in enumerate(students_list):
        if name == item["name"]:
            userPosition = i
            break

    if userPosition == -1:
        print("Student not found")
    else:
        print(f"Student found: {students_list[userPosition]}")
        updated_fields = {
            "name": input("Enter the new name: "),
            "phone": input("Enter the new phone: "),
            "age": input("Enter the new age: "),
            "city": input("Enter the new city: "),
        }
        del students_list[userPosition]
        insertPosition = 0
        for i, elem in enumerate(students_list):
            if updated_fields["name"] > elem["name"]:
                insertPosition += 1
            else:
                break

        students_list.insert(insertPosition, updated_fields)
        print("Student information updated")


def loadFromCSV(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_list.append(row)


def saveToCSV(filename):
    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "phone", "age", "city"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_list)


def main():
    loadFromCSV("lab2.csv")

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "u":
                print("Existing element will be updated")
                updateElement()
            case "d":
                print("Element will be deleted")
                deleteElement()
            case "p":
                print("List will be printed")
                printAllList()
            case "x":
                print("Saving to CSV and exiting...")
                saveToCSV("lab2.csv")
                break
            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()