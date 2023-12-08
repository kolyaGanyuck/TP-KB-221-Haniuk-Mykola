import unittest
from unittest.mock import patch
from io import StringIO
from student import Student
from student_list import StudentList
from utils import Utils
import os
class TestStudentListFunctions(unittest.TestCase):
    def setUp(self):
        self.sample_student_list = StudentList()
        self.sample_student_list.students = [
            Student("John", "1234567890", "20", "City1"),
            Student("Alice", "9876543210", "22", "City2"),
        ]

    def test_add_new_element(self):
        # Test the add_new_element function
        with patch('builtins.input', side_effect=["NewStudent", "5555555555", "25", "NewCity"]):
            self.sample_student_list.add_new_element()

        # Assert that the new student is added correctly
        self.assertEqual(len(self.sample_student_list.students), 3)  
        new_student = self.sample_student_list.students[-1]
        self.assertEqual(new_student.name, "NewStudent")
        self.assertEqual(new_student.phone, "5555555555")
        self.assertEqual(new_student.age, "25")
        self.assertEqual(new_student.city, "NewCity")

    def test_delete_element(self):
        with patch('builtins.input', return_value="John"):
            self.sample_student_list.delete_element()

        # Assert that the student "John" is deleted
        self.assertEqual(len(self.sample_student_list.students), 1)
        for student in self.sample_student_list.students:
            self.assertNotEqual(student.name, "John")

    def test_update_element(self):
        # Test the update_element function
        with patch('builtins.input', side_effect=["Alice", "UpdatedName", "5555555555", "25", "UpdatedCity"]):
            self.sample_student_list.update_element()

        # Assert that the student "Alice" is updated correctly
        updated_student = next(student for student in self.sample_student_list.students if student.name == "UpdatedName")
        self.assertEqual(updated_student.name, "UpdatedName")
        self.assertEqual(updated_student.phone, "5555555555")
        self.assertEqual(updated_student.age, "25")
        self.assertEqual(updated_student.city, "UpdatedCity")

    def test_save_and_load_csv(self):
        # Test the save_to_csv and load_from_csv functions
        with patch('builtins.input', side_effect=["John", "5555555555", "25", "NewCity"]):
            self.sample_student_list.add_new_element()

        # Save the sample_student_list to a CSV file
        script_directory = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_directory, "test_csv_file.csv")
        Utils.save_to_csv(filename, self.sample_student_list)

        # Load the saved CSV file into a new StudentList
        loaded_student_list = Utils.load_from_csv(filename)

        # Assert that the loaded student list is the same as the original sample_student_list
        self.assertEqual(len(loaded_student_list.students), len(self.sample_student_list.students))
        for loaded, original in zip(loaded_student_list.students, self.sample_student_list.students):
            self.assertEqual(loaded.name, original.name)
            self.assertEqual(loaded.phone, original.phone)
            self.assertEqual(loaded.age, original.age)
            self.assertEqual(loaded.city, original.city)

if __name__ == '__main__':
    unittest.main()
