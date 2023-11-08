## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "age": "18", "city" : "Chernihiv"},
    {"name":"Emma", "phone":"0631234567", "age": "19", "city" : "Bila Tserkva"},
    {"name":"Jon",  "phone":"0631234567", "age": "18", "city" : "Chernihiv"},
    {"name":"Zak",  "phone":"0631234567", "age": "20", "city" : "Chernihiv"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", age is " + elem["age"] + ", city is " + elem["city"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    city = input("Please enter student city: ")

    newItem = {"name": name, "phone": phone, "age" : age, "city" : city}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    userPosition  = -1
    
    for i, item in enumerate(list):
        if name == item["name"]:
            userPosition = i
            break
    
    if userPosition == -1:
        print("Student not found")
    else:
        print(f"Student found: {list[userPosition]}")
        updated_fields = {
            "name": input("Enter the new name : "),
            "phone": input("Enter the new phone : "),
            "age": input("Enter the new age : "),
            "city": input("Enter the new city : ")
        }
        del list[userPosition]
        insertPosition = 0
        for i, elem in enumerate(list):
            if updated_fields["name"] > elem["name"]:
                insertPosition += 1
            else:
                break

        list.insert(insertPosition, updated_fields)
        print("Student information updated")
    
    
    
def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()