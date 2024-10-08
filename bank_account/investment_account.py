# investment_account.py
from .bank_account import BankAccount
from datetime import date

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today().replace(year=date.today().year - 10)

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._management_fee = management_fee

    def get_service_charges(self) -> float:
        if self._date_created < self.TEN_YEARS_AGO:
            return super().get_service_charges() + self._management_fee
        return super().get_service_charges()

    def __str__(self) -> str:
        return f"Investment {super().__str__()}, Management Fee: {self._management_fee}"
