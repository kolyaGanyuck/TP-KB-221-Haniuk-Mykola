def add_item_to_dict(my_dict, key, value):
    my_dict[key] = value
    return my_dict

def remove_item_from_dict(my_dict, key):
    if key in my_dict:
        del my_dict[key]
    return my_dict

def get_value_from_dict(my_dict, key):
    return my_dict.get(key)

def update_dict(my_dict, other_dict):
    my_dict.update(other_dict)
    return my_dict

def keys_of_dict(my_dict):
    return list(my_dict.keys())

def values_of_dict(my_dict):
   return list(my_dict.values())

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)

# Тести і виведення результатів
result = add_item_to_dict(my_dict, 'd', 4)
print("add_item_to_dict:", result)

result = remove_item_from_dict(my_dict, 'b')
print("remove_item_from_dict:", result)

result = get_value_from_dict(my_dict, 'c')
print("get_value_from_dict:", result)

other_dict = {'e': 5, 'f': 6}
result = update_dict(my_dict, other_dict)
print("update_dict:", result)

result = keys_of_dict(my_dict)
print("keys_of_dict:", result)

result = values_of_dict(my_dict)
print("values_of_dict:", result)    