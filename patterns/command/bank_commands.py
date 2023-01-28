from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposites {amount}, '
              f'balance = {self.balance}')

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print((f'Withdraw {amount}, '
                   f'balance = {self.balance}'))
            return True
        return False

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)


if __name__ == '__main__':
    ba = BankAccount()
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )
    cmd.invoke()
    print(ba)
    cmd.undo()
    print(ba)
