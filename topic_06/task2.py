data = [
    {"name": "Anna", "Grade": 80},
    {"name": "Peter", "Grade": 90},
    {"name": "Maria", "Grade": 75},
    {"name": "John", "Grade": 41},
]

sort_by = input("Sort by name (name) or grade (grade)? ")

if sort_by == "name":
    sorted_data = sorted(data, key=lambda x: x['name'])
    print("Sorted list by name:")
elif sort_by == "grade":
    order = input("Sort by grade in descending order (highest to lowest)? (yes/no) ")
    if order == "yes":
        sorted_data = sorted(data, key=lambda x: x['Grade'], reverse=True)
        print("Sorted list by grade (from highest to lowest):")
    elif order == "no":
        sorted_data = sorted(data, key=lambda x: x['Grade'])
        print("Sorted list by grade (from lowest to highest):")
    else:
        print("Invalid choice. Enter 'yes' or 'no' for sorting order.")
        sorted_data = []
else:
    print("Invalid choice. Enter 'name' or 'grade'.")
    sorted_data = []

for item in sorted_data:
    print(f"Name: {item['name']}, Grade: {item['Grade']}")