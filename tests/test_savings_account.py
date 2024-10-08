"""
Description: Unit tests for the SavingsAccount class.
Author: ACE Faculty
Modified by: RavneetKaur 
Date: 08-10-2024 
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_saving_account.py
"""

import unittest
from savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def test_init(self):
        account = SavingsAccount(67890, 1002, 1500.0, '2024-01-01', 1000.0)
        self.assertEqual(account.minimum_balance, 1000.0)

    def test_invalid_minimum_balance(self):
        with self.assertRaises(TypeError):
            SavingsAccount(67890, 1002, 1500.0, '2024-01-01', 'invalid')

    def test_get_service_charges_above_minimum(self):
        account = SavingsAccount(67890, 1002, 1500.0, '2024-01-01', 1000.0)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_get_service_charges_below_minimum(self):
        account = SavingsAccount(67890, 1002, 500.0, '2024-01-01', 1000.0)
        self.assertEqual(account.get_service_charges(), 2.50)

    def test_str(self):
        account = SavingsAccount(67890, 1002, 1500.0, '2024-01-01', 1000.0)
        expected_output = "Account Number: 67890\nClient Number: 1002\nBalance: 1500.0\nMinimum Balance: 1000.0"
        self.assertEqual(str(account), expected_output)

if __name__ == '__main__':
    unittest.main()
