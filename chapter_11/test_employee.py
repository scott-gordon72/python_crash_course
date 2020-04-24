"""Unit test for employee.py"""
import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests for employee.py"""

    def setUp(self):
        self.emp = Employee('Joe', 'Isuzu', 40000)

    def test_give_default_raise(self):
        """Default raise amount should be 5000"""
        self.emp.give_raise()
        self.assertEqual(self.emp.annual_salary, 45000)

    def test_give_custom_raise(self):
        """Set custom raise amount"""
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.annual_salary, 50000)

if __name__ == '__main__':
    unittest.main()
