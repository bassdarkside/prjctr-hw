class Account:
    def __init__(self, account_number, balance):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Amount must be positive")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return (
            f"Account number: {self._account_number}, balance: {self._balance}"
        )


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * (self.interest_rate / 100)
        self.deposit(interest)
        return f"Added {interest} to balance."


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f"Overdraft notice sent for account {self.account_number}")


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account._account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} has been closed.")

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                result = account.add_interest()
                print(result)
                return result
            elif isinstance(account, CurrentAccount):
                if account._balance < 0:
                    account.send_overdraft_letter()


if __name__ == "__main__":
    bank = Bank()

    savings_account = SavingsAccount(1001, 1000, 2.5)
    current_account = CurrentAccount(2001, 2000, -1000)
    account = Account(3001, 3000)

    bank.open_account(savings_account)
    bank.open_account(current_account)
    bank.open_account(account)

    bank.update()

    bank.pay_dividend(100)

    bank.close_account(3001)
