numbers = [2, 4, 6, 8]

while True:
    print("list:", numbers)
    new_number = input("Enter a new number, or enter 'Exit' if you want to exit: ")

    if new_number == 'Exit':
        break

    new_number = int(new_number) 

    insert_index = 0

    for num in numbers:
        if new_number > num:
            insert_index += 1

    numbers.insert(insert_index, new_number)