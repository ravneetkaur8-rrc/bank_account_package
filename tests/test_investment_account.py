"""
Description: Unit tests for the InvestmentAccount class.
Author: ACE Faculty
Modified by: RavneetKaur 
Date: 08-10-2024 
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def test_init(self):
        account = InvestmentAccount(13579, 1004, 20000.0, '2010-01-01', 500.0)
        self.assertEqual(account.management_fee, 500.0)

    def test_invalid_management_fee(self):
        with self.assertRaises(TypeError):
            InvestmentAccount(13579, 1004, 20000.0, '2010-01-01', 'invalid')

    def test_get_service_charges_old_account(self):
        account = InvestmentAccount(13579, 1004, 20000.0, '2000-01-01', 500.0)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_get_service_charges_recent_account(self):
        account = InvestmentAccount(13579, 1004, 20000.0, '2015-01-01', 500.0)
        self.assertEqual(account.get_service_charges(), 500.50)

    def test_str(self):
        account = InvestmentAccount(13579, 1004, 20000.0, '2015-01-01', 500.0)
        expected_output = "Account Number: 13579\nClient Number: 1004\nBalance: 20000.0\nManagement Fee: 500.0"
        self.assertEqual(str(account), expected_output)

if __name__ == '__main__':
    unittest.main()
