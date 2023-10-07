import unittest
from unittest.mock import patch
from hw_18 import Bank, Account, SavingsAccount


class TestBankMethods(unittest.TestCase):
    def test_open_account(self):
        bank = Bank()
        account = Account(account_number=1011, balance=100)
        bank.open_account(account)
        self.assertIn(account, bank.accounts)
        self.assertGreater(account.get_balance(), 0)

    @patch("builtins.print")
    def test_update(self, mock_print):
        bank = Bank()
        account = SavingsAccount(1001, 1000, 2.5)
        bank.open_account(account)
        balance_before_upd = account.get_balance()
        result = bank.update()
        balance_after_upd = account.get_balance()
        self.assertNotEqual(balance_before_upd, balance_after_upd)
        mock_print.assert_called_with(result)


if __name__ == "__main__":
    unittest.main()
