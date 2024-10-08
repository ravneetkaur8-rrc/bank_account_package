# savings_account.py
from .bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._minimum_balance = minimum_balance

    def get_service_charges(self) -> float:
        if self.balance < self._minimum_balance:
            return super().get_service_charges() + self.SERVICE_CHARGE_PREMIUM
        return super().get_service_charges()

    def __str__(self) -> str:
        return f"Savings {super().__str__()}, Minimum Balance: {self._minimum_balance}"
