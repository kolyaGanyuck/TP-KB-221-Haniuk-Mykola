import unittest
from unittest.mock import patch
import csv
from io import StringIO
from lab_02 import *
class TestPhoneDirectory(unittest.TestCase):

    def setUp(self):
        # Initialize an empty list before each test
        students_list = []

    def test_add_new_element(self):
        with patch('builtins.input', side_effect=['John', '123456789', '25', 'New York']):
            addNewElement()
        self.assertEqual(students_list, [{"name": "John", "phone": "123456789", "age": "25", "city": "New York"}])

    def test_delete_element(self):
        # Adding a student to the list for testing
        students_list.append({"name": "Alice", "phone": "987654321", "age": "22", "city": "Los Angeles"})
        with patch('builtins.input', return_value='Alice'):
            deleteElement()
        self.assertEqual(students_list, [])

    def test_update_element(self):
        # Adding a student to the list for testing
        students_list.append({"name": "Bob", "phone": "111111111", "age": "30", "city": "Chicago"})

        with patch('builtins.input', side_effect=['Bob', 'Updated Bob', '222222222', '25', 'San Francisco']):
            updateElement()

        self.assertEqual(students_list, [{"name": "Updated Bob", "phone": "222222222", "age": "25", "city": "San Francisco"}])

    def test_load_from_csv(self):
        # Create a temporary file with CSV data
        with open('temp.csv', 'w', newline='') as file:
            fieldnames = ["name", "phone", "age", "city"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"name": "Alice", "phone": "987654321", "age": "22", "city": "Los Angeles"})

        loadFromCSV('temp.csv')
        self.assertEqual(students_list, [{"name": "Alice", "phone": "987654321", "age": "22", "city": "Los Angeles"}])

    def test_save_to_csv(self):
        # Adding a student to the list for testing
        students_list.append({"name": "Charlie", "phone": "333333333", "age": "28", "city": "Houston"})

        # Create a temporary file and save data to it
        saveToCSV('temp.csv')
        
        with open('temp.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        self.assertEqual(data, [{"name": "Charlie", "phone": "333333333", "age": "28", "city": "Houston"}])

    def tearDown(self):
        # Clean up after each test
        students_list.clear()


if __name__ == '__main__':
    unittest.main()