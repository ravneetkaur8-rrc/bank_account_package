# bank_account.py
from datetime import date

class BankAccount:
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
        self._date_created = date_created

    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def client_number(self) -> int:
        return self._client_number

    @property
    def balance(self) -> float:
        return self._balance

    def update_balance(self, amount: float) -> None:
        self._balance += amount

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self.update_balance(-amount)
        else:
            raise ValueError("Insufficient balance.")

    def get_service_charges(self) -> float:
        return self.BASE_SERVICE_CHARGE

    def __str__(self) -> str:
        return f"Account {self.account_number}, Client {self.client_number}, Balance {self.balance}"
