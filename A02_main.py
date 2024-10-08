"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: RavneetKaur
Date: 08-10-2024
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(12345, 1001, -50.0, date.today(), 100.0, 0.05)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
print(f"Service Charges: {chequing_account.get_service_charges()}")
# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(200.0)
# 4b. Print the ChequingAccount
print(chequing_account)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: {chequing_account.get_service_charges()}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(67890, 1002, 1500.0, date.today(), 1000.0)

# 6. Print the SavingsAccount created in step 5.
print(savings_account)
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: {savings_account.get_service_charges()}")


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_account.withdraw(600.0)
# 7b. Print the SavingsAccount.
print(savings_account)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: {savings_account.get_service_charges()}")



print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account_recent = InvestmentAccount(24680, 1003, 10000.0, date.today(), 250.0)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account_recent)
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Service Charges: {investment_account_recent.get_service_charges()}")


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_old = InvestmentAccount(13579, 1004, 20000.0, InvestmentAccount.TEN_YEARS_AGO, 500.0)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_old)
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Service Charges: {investment_account_old.get_service_charges()}")


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
# 12. Withdraw service charges from each account
for account in [chequing_account, savings_account, investment_account_recent, investment_account_old]:
    try:
        account.withdraw(account.get_service_charges())
    except ValueError as e:
        print(f"Error with {account}: {e}")



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

for account in [chequing_account, savings_account, investment_account_recent, investment_account_old]:
    print(account)