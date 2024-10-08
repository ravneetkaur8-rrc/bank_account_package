"""
Description: Unit tests for the ChequingAccount class.
Author: ACE Faculty
Modified by: RavneetKaur 
Date: 08-10-2024 
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):

    def test_init(self):
        account = ChequingAccount(12345, 1001, 500.0, '2024-01-01', 100.0, 0.05)
        self.assertEqual(account.overdraft_limit, 100.0)
        self.assertEqual(account.overdraft_rate, 0.05)

    def test_invalid_overdraft_limit(self):
        with self.assertRaises(TypeError):
            ChequingAccount(12345, 1001, 500.0, '2024-01-01', 'invalid', 0.05)

    def test_invalid_overdraft_rate(self):
        with self.assertRaises(TypeError):
            ChequingAccount(12345, 1001, 500.0, '2024-01-01', 100.0, 'invalid')

    def test_get_service_charges(self):
        account = ChequingAccount(12345, 1001, 50.0, '2024-01-01', 100.0, 0.05)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_str(self):
        account = ChequingAccount(12345, 1001, 500.0, '2024-01-01', 100.0, 0.05)
        expected_output = "Account Number: 12345\nClient Number: 1001\nBalance: 500.0\nOverdraft Limit: 100.0\nOverdraft Rate: 0.05"
        self.assertEqual(str(account), expected_output)

if __name__ == '__main__':
    unittest.main()
