from sys import argv
from utils import Utils
from student_list import StudentList

def main():
    if len(argv) != 2:
        print("Usage: python script.py filename.csv")
        return

    filename = argv[1]
    students_list = Utils.load_from_csv(filename)

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                students_list.add_new_element()
                
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
