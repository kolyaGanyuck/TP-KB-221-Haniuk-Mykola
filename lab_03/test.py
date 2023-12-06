import unittest
import os
import csv
from unittest.mock import patch
from utils import *
from main import *
from utils import *

class TestPhoneDirectory(unittest.TestCase):
    def setUp(self):
        self.csv_filename = 'test_data.csv'
        self.students_list = []  
        Utils.saveToCSV(self.csv_filename, self.students_list)

    def test_add_new_element(self):
        with patch('builtins.input', side_effect=['John', '123456789', '25', 'New York']):
            addNewElement(self.students_list)

        self.assertEqual(self.students_list[0]["name"], "John")

    def test_delete_element(self):
        with patch('builtins.input', return_value='Anna'):
            deleteElement(self.students_list)

        self.assertNotIn('Anna', [student['name'] for student in self.students_list])

    def test_update_element(self):
        with patch('builtins.input', side_effect=['Anna', 'NewAnna', '987654321', '30', 'London']):
            updateElement(self.students_list)

        updated_student_names = [student['name'] for student in self.students_list]
        self.assertIn('NewAnna', updated_student_names)

    def test_read_from_csv(self):
        self.students_list.clear()
        with open(self.csv_filename, 'a') as file:
            file.write('Invalid Data\n')
        with self.assertRaises(Exception): 
            loaded_students_list = Utils.loadFromCSV(self.csv_filename)

        self.assertEqual(len(self.students_list), 0)

    def tearDown(self):
        os.remove(self.csv_filename)

if __name__ == '__main__':
    unittest.main()