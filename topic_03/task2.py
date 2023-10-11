def add_element_to_list(my_list, element):
    my_list.append(element)
    return my_list

def remove_element_from_list(my_list, element):
    if element in my_list:
        my_list.remove(element)
    return my_list

def find_index_of_element(my_list, element):
    if element in my_list:
        index = my_list.index(element)
        return index
    else:
        return None

def sort_list(my_list):
    my_list.sort()
    return my_list

def reverse_list(my_list):
    my_list.reverse()
    return my_list

def count_occurrences(my_list, element):
    count = my_list.count(element)
    return count

def insert_element(my_list, index, element):
    my_list.insert(index, element)
    return my_list

def slice_list(my_list, start, end):
    sliced = my_list[start:end]
    return sliced

def copy_list(my_list):
    copied = my_list.copy()
    return copied

my_list = [1, 2, 3]
element = 4

print("Original List:", my_list)

# Тести і виведення результатів
result = add_element_to_list(my_list, element)
print("add_element_to_list:", result)

result = remove_element_from_list(my_list, 3)
print("remove_element_from_list:", result)

result = find_index_of_element(my_list, 2)
print("find_index_of_element:", result)

result = sort_list(my_list)
print("sort_list:", result)

result = reverse_list(my_list)
print("reverse_list:", result)

result = count_occurrences(my_list, 2)
print("count_occurrences:", result)

result = insert_element(my_list, 1, 4)
print("insert_element:", result)

result = slice_list(my_list, 1, 2)
print("slice_list:", result)

result = copy_list(my_list)
print("copy_list:", result)