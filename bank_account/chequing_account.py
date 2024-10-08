# chequing_account.py
from .bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def get_service_charges(self) -> float:
        if self.balance < -self._overdraft_limit:
            return super().get_service_charges() + (self._overdraft_rate * abs(self.balance))
        return super().get_service_charges()

    def __str__(self) -> str:
        return f"Chequing {super().__str__()}, Overdraft Limit: {self._overdraft_limit}, Overdraft Rate: {self._overdraft_rate}"
