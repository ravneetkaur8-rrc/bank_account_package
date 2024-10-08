"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: RavneetKaur 
Date: 08-10-2024 
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account import BankAccount  

class TestBankAccount(unittest.TestCase):

    def test_init(self):
        account = BankAccount(12345, 1001, 500.0, '2024-01-01')
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 1001)
        self.assertEqual(account.balance, 500.0)
        self.assertEqual(account.date_created, '2024-01-01')

    def test_str(self):
        account = BankAccount(12345, 1001, 500.0, '2024-01-01')
        expected_output = "Account Number: 12345\nClient Number: 1001\nBalance: 500.0\nDate Created: 2024-01-01"
        self.assertEqual(str(account), expected_output)

if __name__ == '__main__':
    unittest.main()
